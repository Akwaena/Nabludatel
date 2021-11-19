import debugger
import cfg_parser

import sys
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.add_controls()

    def add_controls(self):
        wid = QWidget(self)
        self.setCentralWidget(wid)

        pixmap = QPixmap("1.png").scaled(250, 250)
        self.label = QLabel(self, alignment=Qt.AlignCenter)
        self.label.setPixmap(pixmap)

        control_area = QVBoxLayout()
        control_area.addWidget(self.label)

        wid.setLayout(control_area)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
