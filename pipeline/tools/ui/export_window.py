from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog
from Qt import QtCompat
import six

from pipeline.engine import handler

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path

ui_path = Path(__file__).parent / 'qt' / 'export.ui'


class ToolWindow(QMainWindow):

    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.loadUi(str(ui_path), self)
        self.handle_inputs()
        self.handler = handler.choose_handler()

    def handle_inputs(self):
        self.file_choice_button.clicked.connect(self.choose_file)
        self.export_button.clicked.connect(self.export_to_alembic)
        self.frame_range_start.valueChanged.connect(self.update_max_fr_value)

    def export_to_alembic(self):
        path = Path(self.root_input.text())
        self.export_button.clicked.connect(
            self.handler.alembic_export(self.frame_range_start.value(), self.frame_range_end.value(),
                                        path, self.file_name_input.text()))

    def choose_file(self):
        file_name = QFileDialog.getExistingDirectory(self, "QFileDialog.GetExistingDirectory()", "C://",
                                                     QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if file_name:
            self.root_input.setText(file_name)

    def update_max_fr_value(self):
        self.frame_range_end.setValue(self.frame_range_start.value())


def launch_tool():
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    window = ToolWindow()
    window.show()
    app.exec_()
