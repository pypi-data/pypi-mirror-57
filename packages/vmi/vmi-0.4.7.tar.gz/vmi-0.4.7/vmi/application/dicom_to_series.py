import hashlib
import json
import pathlib
import pickle
import threading
from typing import Dict, Any

import gridfs
import pydicom
import pymongo
import vtk

import vmi


def local_open_dicom():
    global series_list
    dcmdir = vmi.askDirectory('DICOM')

    if dcmdir is not None:
        series_list = vmi.sortSeries(dcmdir)
        local_select_series()


def local_select_series():
    global series_dict
    series = vmi.askSeries(series_list)
    if series is not None:
        series_dict = series.toKeywordValue()
        input_image(series.read())


def input_image(image: vtk.vtkImageData):
    series_volume.setData(image)
    series_view.setCamera_FitAll()
    series_view.updateAtOnce()
    vmi.appupdate()


def update_series_opcity():
    series_volume.setOpacityScalar({series_opacity_range[0] - 1: 0,
                                    series_opacity_range[0]: 1,
                                    series_opacity_range[1]: 1,
                                    series_opacity_range[1] + 1: 0})
    series_volume.setColor({series_opacity_range[0]: [1, 1, 0.9],
                            series_opacity_range[1]: [1, 1, 0.1]})


def local_save_nifti():
    vmi.imSaveFile_NIFTI(series_volume.data())


def upload(image: vtk.vtkImageData, kw_value: Dict[str, Any]):
    # 删除已有数据
    uid = {'SeriesInstanceUID': kw_value['SeriesInstanceUID']}

    for one in file_db.find(uid):
        file_db.delete(one._id)

    for one in data_db.find(uid):
        data_db.delete_one(one)

    # 图像序列化为文件，计算特征码，上传文件项
    vmi.setPickleNIFTI_gz(False)
    image_bytes = pickle.dumps(image)
    file_id = file_db.put(image_bytes,
                          fileType='.nii',
                          scalarType=image.GetScalarTypeAsString(),
                          SeriesInstanceUID=kw_value['SeriesInstanceUID'])

    # 检查上传结果是否与本地一致
    if file_db.find_one({'_id': file_id}).md5 != hashlib.md5(image_bytes).hexdigest():
        file_db.delete(file_id)
        return print('远端MD5校验失败 {}'.format(repr(kw_value)))

    # 上传数据项
    data_db.insert_one(kw_value)


def remote_auto_upload():
    global data_db, file_db
    client = pymongo.MongoClient('mongodb://root:medraw123@192.168.11.122:27017/admin', 27017)
    data_db = client.testDB.get_collection('spinePelvis')
    file_db = gridfs.GridFS(client.testDB, collection='spinePelvis')

    # 远端清空
    data_db.delete_many({})
    for i in file_db.find():
        file_db.delete(i._id)
    chunks_db: pymongo.collection.Collection = client.testDB.get_collection('spinePelvis.chunks')
    chunks_db.delete_many({})

    p = vmi.askDirectory('DICOM根目录')
    if p is None:
        return

    # 本地排序
    save_json = pathlib.Path(p) / 'filenames_list.json'
    if save_json.exists():
        filenames_list = json.loads(save_json.read_text())
    else:
        filenames_list = vmi.sortFilenames(p)
        pathlib.Path(str(save_json)).write_text(json.dumps(filenames_list))

    # 本地过滤
    save_json = pathlib.Path(p) / 'filenames_list_1.json'
    if save_json.exists():
        filenames_list = json.loads(save_json.read_text())
    else:
        new_list, i = {}, 0
        for filenames in filenames_list:
            i = i + 1

            ds = pydicom.dcmread(filenames[0])

            if 'PatientID' not in ds or 'StudyInstanceUID' not in ds or 'SeriesInstanceUID' not in ds:
                continue
            if 'Modality' not in ds or ds['Modality'].value != 'CT':
                continue
            if 'BitsStored' not in ds or ds['BitsStored'].value != 12:
                continue
            if 'StudyDescription' in ds and 'Spine' in ds['StudyDescription'].value:
                continue
            if 'SliceThickness' not in ds or ds['SliceThickness'].value == '' or float(ds['SliceThickness'].value) > 1:
                continue
            if 'SliceLocation' not in ds or len(filenames) < 2:
                continue

            kw = str(ds['StudyInstanceUID'].value)
            if kw in new_list and len(filenames) < len(new_list[kw]):
                continue

            ds1 = pydicom.dcmread(filenames[1])
            delta = abs(float(ds['SliceLocation'].value) - float(ds1['SliceLocation'].value))
            if delta != float(ds['SliceThickness'].value):
                continue

            new_list[kw] = filenames.copy()
            print('本地过滤 {}/{}'.format(len(new_list), i))
        filenames_list = new_list.copy()
        pathlib.Path(str(save_json)).write_text(json.dumps(filenames_list))

    # 图像过滤
    save_json = pathlib.Path(p) / 'filenames_list_2.json'
    if save_json.exists():
        filenames_list = json.loads(save_json.read_text())
    else:
        new_list = []
        for kw in filenames_list:
            filenames = filenames_list[kw]

            series = vmi.SeriesData(filenames)
            image = series.read()

            tags = series.toKeywordValue()
            t = threading.Thread(target=upload, args=[image, tags])
            t.start()
            vmi.appwait(t)

            input_image(image)
            save_snapshot = pathlib.Path(p) / kw
            series_view.snapshot_PNG(str(save_snapshot))

            new_list.append(tags['SeriesInstanceUID'])
            print('上传成功 {}/{}'.format(len(new_list), len(filenames_list)))
        filenames_list = new_list.copy()
        pathlib.Path(str(save_json)).write_text(json.dumps(filenames_list))


def LeftButtonPressRelease(**kwargs):
    global series_opacity_range
    if kwargs['picked'] is series_opacity_range_box[0]:
        v = vmi.askInt(-10000, series_opacity_range[0], series_opacity_range[1])
        if v is not None:
            series_opacity_range[0] = v
        series_opacity_range_box[0].draw_text('min {:.0f}'.format(series_opacity_range[0]))
        update_series_opcity()
    elif kwargs['picked'] is series_opacity_range_box[1]:
        v = vmi.askInt(series_opacity_range[0], series_opacity_range[0], 10000)
        if v is not None:
            series_opacity_range[1] = v
        series_opacity_range_box[1].draw_text('min {:.0f}'.format(series_opacity_range[1]))
        update_series_opcity()


def NoButtonWheel(**kwargs):
    global series_opacity_range
    if kwargs['picked'] is series_opacity_range_box[0]:
        series_opacity_range[0] = min(max(series_opacity_range[0] + kwargs['delta'],
                                          -10000), series_opacity_range[1])
        series_opacity_range_box[0].draw_text('min {:.0f}'.format(series_opacity_range[0]))
        update_series_opcity()
    elif kwargs['picked'] is series_opacity_range_box[1]:
        series_opacity_range[1] = min(max(series_opacity_range[1] + kwargs['delta'],
                                          series_opacity_range[0]), 10000)
        series_opacity_range_box[1].draw_text('max {:.0f}'.format(series_opacity_range[1]))
        update_series_opcity()


def return_globals():
    return globals()


if __name__ == '__main__':
    main = vmi.Main(return_globals)
    main.setAppName('dicom_to_series')
    main.setAppVersion(vmi.version)
    main.excludeKeys += ['main']

    menu_local = main.menuBar().addMenu('本地')
    menu_local.addAction('打开DICOM').triggered.connect(local_open_dicom)
    menu_local.addAction('载入Series').triggered.connect(local_select_series)
    menu_local.addAction('保存NIFTI').triggered.connect(local_save_nifti)

    menu_remote = main.menuBar().addMenu('远端')
    menu_remote.addAction('载入Series').triggered.connect(remote_get_series)
    menu_remote.addAction('自动上传').triggered.connect(remote_auto_upload)

    series_list, series_dict = [], {}
    series_view = vmi.View()
    series_view.setCamera_Coronal()
    series_volume = vmi.ImageVolume(series_view)

    series_opacity_range = [200, 3000]
    update_series_opcity()

    series_opacity_range_box = [vmi.TextBox(series_view, text='min {:.0f}'.format(series_opacity_range[0]),
                                            size=[0.1, 0.03], pos=[0, 0.03], anchor=[0, 0], pickable=True),
                                vmi.TextBox(series_view, text='max {:.0f}'.format(series_opacity_range[1]),
                                            size=[0.1, 0.03], pos=[0.1, 0.03], anchor=[0, 0], pickable=True)]
    for box in series_opacity_range_box:
        box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

    main.layout().addWidget(series_view, 0, 0, 1, 1)
    vmi.appexec(main)
    vmi.appexit()
