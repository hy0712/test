# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/hiero/excel_import_jpg.ui'
#
# Created: Thu Feb 23 19:51:02 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PIL import Image
import sys
import os
import os.path

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))


class Ui_ImgToExcel(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_ImgToExcel, self).__init__(parent)
        self.delete_version = []
        self.setupUi(self)
        self.spinBox.setRange(0, 99)
        self.spinBox.setValue(0)
        self.spinBox_scale.setRange(0, 999)
        self.spinBox_scale.setValue(10)
        self.img_list = []

    def setupUi(self, ImgToExcel):
        ImgToExcel.setObjectName("ImgToExcel")
        ImgToExcel.resize(369, 284)
        self.verticalLayout = QtGui.QVBoxLayout(ImgToExcel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ImgToExcel)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(ImgToExcel)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 4)
        self.openButton = QtGui.QPushButton(ImgToExcel)
        self.openButton.setObjectName("openButton")
        self.gridLayout.addWidget(self.openButton, 0, 5, 1, 1)
        self.label_2 = QtGui.QLabel(ImgToExcel)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(ImgToExcel)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(ImgToExcel)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.spinBox_scale = QtGui.QSpinBox(ImgToExcel)
        self.spinBox_scale.setObjectName("spinBox_scale")
        self.gridLayout.addWidget(self.spinBox_scale, 1, 4, 1, 1)
        self.printButton = QtGui.QPushButton(ImgToExcel)
        self.printButton.setObjectName("printButton")
        self.gridLayout.addWidget(self.printButton, 1, 5, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(ImgToExcel)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 2, 0, 1, 6)
        self.label_4 = QtGui.QLabel(ImgToExcel)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(ImgToExcel)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(ImgToExcel)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), ImgToExcel.close)
        QtCore.QObject.connect(self.openButton, QtCore.SIGNAL("clicked()"), ImgToExcel.openpath)
        QtCore.QObject.connect(self.printButton, QtCore.SIGNAL("clicked()"), ImgToExcel.printinfo)
        QtCore.QMetaObject.connectSlotsByName(ImgToExcel)

    def retranslateUi(self, ImgToExcel):
        ImgToExcel.setWindowTitle(
            QtGui.QApplication.translate("ImgToExcel", "Excel表批量插入图片生成信息", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ImgToExcel", "缩略图路径", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setText(QtGui.QApplication.translate("ImgToExcel", "打开", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ImgToExcel", "每几格插入", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ImgToExcel", "图片缩放比例", None, QtGui.QApplication.UnicodeUTF8))
        self.printButton.setText(
            QtGui.QApplication.translate("ImgToExcel", "复制到剪贴板", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(
            QtGui.QApplication.translate("ImgToExcel", "只支持jpeg序列哦", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(
            QtGui.QApplication.translate("ImgToExcel", "关闭", None, QtGui.QApplication.UnicodeUTF8))

    def openpath(self):
        s = QtGui.QFileDialog.getExistingDirectory(self, u"路径")
        if s:
            self.lineEdit.setText(str(s))

    def printinfo(self):
        self.plainTextEdit.setPlainText(self.tr(''))
        jpg_path = self.lineEdit.text()
        scale = self.spinBox_scale.value()
        line_num = self.spinBox.value()
        if os.path.isdir(jpg_path):
            jpg_path = jpg_path.replace('\\', '/')
            jpg_list = [jpg_path + '/' + j for j in os.listdir(jpg_path) if os.path.isfile(jpg_path + '/' + j)]
            imgext = ['.jpg', '.JPG', '.jpeg', '.JPEG']
            from Tkinter import Tk
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            # self.plainTextEdit.insertPlainText("<table>")
            for jpg in jpg_list:
                if os.path.splitext(jpg)[-1] in imgext:
                    img = Image.open(jpg)
                    img_width = img.size[0] * scale * 0.01
                    img_height = img.size[1] * scale * 0.01
                    img_name = jpg.replace('/', '\\')
                    if line_num == 0:
                        val = '<table><img src="%s" width="%d" height="%d">\r' % (
                            img_name, img_width, img_height)
                    else:
                        val = '%s<img src="%s" width="%d" height="%d">\r' % (
                            '<table>' * (line_num + 1), img_name, img_width, img_height)
                    self.plainTextEdit.insertPlainText(val)
                    r.clipboard_append(val)
                    # self.plainTextEdit.setPlainText(str(jpg_list)[1:-1])
                    # self.plainTextEdit.setPlainText(self.tr('asdasdasdasdasdasd'))
            r.destroy()
        else:
            QtGui.QMessageBox.warning(self, self.tr("提示"), self.tr("请给一个有效路径"))


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Ui_ImgToExcel()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
