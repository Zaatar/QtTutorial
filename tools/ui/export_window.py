from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow
from Qt import QtCompat
import six

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
        # self.handler = handler.choose_handler()

    def handle_inputs(self):
        self.export_button.clicked.connect(self.export_to_alembic)

    def export_to_alembic(self):
        print(self.frame_range_start.value())
        print(self.frame_range_end.value())
        print(self.file_name_input.text())
        print(self.root_input.text())
        '''self.export_button.clicked.connect(self.handler.alembic_export
                                           (self, self.frame_range_start, self.frame_range_end,
                                            self.root_input, self.file_name_input))
        '''


# def launch_tool():


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = ToolWindow()
    window.show()
    app.exec_()
