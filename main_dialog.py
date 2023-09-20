import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *
from qgis.PyQt import uic
from qgis.utils import iface


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(
            os.path.join(os.path.dirname(__file__), "main_dialog.ui"), self
        )

        self.ui.pushButton_run.clicked.connect(self.make_mklink)
        self.ui.pushButton_cancel.clicked.connect(self.close)

    def make_mklink(self):
        print(iface)
        # テキストボックス値取得
        plugin_folder = self.ui.qgs_plugin_folder.filePath()
        dev_folder = self.ui.qgs_dev_folder.filePath()
        # テキストボックス値をメッセージ表示
        QMessageBox.information(None, "Result", plugin_folder + "\n" + dev_folder)
