from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMainWindow, QFileDialog
from Qt import QtCompat
from PySide2.QtCore import QDir
import six

from pipeline.engine import handler

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path

ui_path = Path(__file__).parent / 'qt' / 'abc_import_ue.ui'


class ToolWindow(QMainWindow):

    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.loadUi(str(ui_path), self)
        self.handle_inputs()
        self.handler = handler.choose_handler()
        self.line_destination_path_display.setText('/Game/')

    def handle_inputs(self):
        self.btn_choose_file.clicked.connect(self.choose_import_directory)
        self.btn_choose_destination.clicked.connect(self.choose_destination_dir)
        self.btn_import_alembic.clicked.connect(self.import_asset_ue)

    def import_asset_ue(self):
        print(f'In Import Asset UE in Import_Window.py')
        self.handler.import_asset_ue(self.line_import_directory_display.text(),
                                     self.line_destination_path_display.text(), self.line_dcc_file_name.text(),
                                     self.check_save_after_every_import.isChecked(),
                                     self.check_replace_existing.isChecked())

    def choose_import_directory(self):
        # import_file_name = QFileDialog.getOpenFileName(self, "Open a file", "D://")
        import_file_directory = QFileDialog.getExistingDirectory(self, "QFileDialog.GetExistingDirectory()",
                                                                 QDir.homePath(),
                                                                 QFileDialog.ShowDirsOnly |
                                                                 QFileDialog.DontResolveSymlinks)
        if import_file_directory:
            self.line_import_directory_display.setText(import_file_directory)

    def choose_destination_dir(self):
        dir_name = QFileDialog.getExistingDirectory(self, "QFileDialog.GetExistingDirectory()", QDir.homePath(),
                                                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if dir_name:
            self.line_destination_path_display.setText(dir_name)


def import_launch_tool():
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    window = ToolWindow()
    window.show()
    app.exec_()


def main():
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    window = ToolWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
