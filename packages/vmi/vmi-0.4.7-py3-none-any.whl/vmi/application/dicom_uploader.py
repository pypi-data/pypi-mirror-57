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

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QInputDialog

SizePolicyMinimum = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)


def input_dicom():
    global series_list
    dcmdir = vmi.askDirectory('DICOM')

    if dcmdir is not None:
        series_list = vmi.sortSeries(dcmdir)
        input_series()


def input_series():
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


def output_nifti():
    if series_dict:
        vmi.imSaveFile_NIFTI(series_volume.data())


def upload(image: vtk.vtkImageData, kw_value: Dict[str, Any]):
    data_id = ''

    def func():
        # 图像序列化为文件，计算特征码
        vmi.setPickleNIFTI_gz(False)
        image_bytes = pickle.dumps(image)
        image_md5 = hashlib.md5(image_bytes).hexdigest()

        # 上传文件，避免重复上传完全一样的文件
        if not file_db.exists({'SeriesInstanceUID': kw_value['SeriesInstanceUID']}):
            file_id = file_db.put(image_bytes,
                                  fileType='.nii',
                                  scalarType=image.GetScalarTypeAsString(),
                                  SeriesInstanceUID=kw_value['SeriesInstanceUID'])
            # 检查上传结果是否与本地一致
            if file_db.find_one({'_id': file_id}).md5 != image_md5:
                file_db.delete(file_id)
                return print('远端MD5校验失败 {}'.format(repr(kw_value)))

        # 数据项，引用图像文件特征码
        data_dict = {**kw_value}

        # 上传数据项，避免重复上传完全一样的数据项
        nonlocal data_id
        data_one = data_db.find_one(data_dict)
        if data_one is None:
            data_one = data_db.insert_one(data_dict)
            data_id = data_one.inserted_id
        else:
            data_id = data_one['_id']

    t = threading.Thread(target=func)
    t.start()
    vmi.appwait(t)
    return data_id


def output_upload():
    if series_dict:
        dialog = QDialog()
        dialog.setSizePolicy(SizePolicyMinimum)
        dialog.setWindowTitle('Upload')
        dialog.setLayout(QVBoxLayout())
        dialog.setMinimumWidth(200)

        label = [QLabel('医生姓名:'), QLabel('联系方式:'), QLabel('销售姓名:'), QLabel('手术时间:')]
        text = [QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit()]

        for i in range(4):
            dialog.layout().addWidget(label[i])
            dialog.layout().addWidget(text[i])

        button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
        button.setSizePolicy(SizePolicyMinimum)
        button.accepted.connect(dialog.accept)
        button.rejected.connect(dialog.reject)
        dialog.layout().addWidget(button)

        if dialog.exec_() == QDialog.Accepted:
            # 上传数据
            data_id = upload(series_volume.data(), series_dict)
            # 上传键值
            key_data_dict = data_db.find_one({'SeriesInstanceUID': series_dict['SeriesInstanceUID']})
            value_data_dict = {**key_data_dict, 'DoctorName': text[0].text(),
                               'ContactInformation': text[1].text(),
                               'SalesName': text[2].text(), 'OperationTime': text[3].text()}
            data_db.find_one_and_replace(key_data_dict, value_data_dict)

            # 记录上传的id
            if vmi.askYesNo('上传成功 {} 复制到剪贴板？'.format(str(data_id))):
                vmi.app.clipboard().setText(str(data_id))


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
    client = pymongo.MongoClient('mongodb://root:medraw123@192.168.11.122:27017/admin', 27017)
    data_db: pymongo.collection.Collection = client.xj_testDB.data
    file_db = gridfs.GridFS(client.xj_testDB, collection='file')

    main = vmi.Main(return_globals)
    main.setAppName('dicom_uoloader')
    main.setAppVersion(vmi.version)
    main.excludeKeys += ['main']

    menu_input = main.menuBar().addMenu('输入')
    menu_input.addAction('DICOM').triggered.connect(input_dicom)
    menu_input.addAction('Series').triggered.connect(input_series)

    menu_output = main.menuBar().addMenu('输出')
    menu_output.addAction('NIFTI').triggered.connect(output_nifti)
    menu_output.addAction('上传').triggered.connect(output_upload)

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
