from PyQt5.QtWidgets import QApplication, QMenuBar, QMainWindow, QMenu, QAction, QLabel, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import sys
import cfg_parser

app = QApplication(sys.argv)
msg = QMessageBox()
msg.setWindowTitle("Название окна")
msg.setText("Описание")
msg.setIcon(QMessageBox.Warning)
sys.exit(app.exec_())
