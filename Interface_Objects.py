from PyQt5.QtWidgets import QApplication, QMenuBar, QMainWindow, QMenu, QAction, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import sys
import cfg_parser

open('temp_img/4custom/1.png', 'r')



class Screen(QThread):
    changePixmap = pyqtSignal(QImage)


class Main(QMainWindow):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.initUI()

    def initUI(self):
        self.MenuBar = QMenuBar(self)
        self.setMenuBar(self.MenuBar)

        self.camMenu = QMenu("Камера", self)
        self.MenuBar.addMenu(self.camMenu)
        self.connect_camAction = QAction('Подключиться', self)
        self.get_camlistAction = QAction('Список камер', self)
        self.add_camAction = QAction('Добавить камеру', self)
        self.camMenu.addAction(self.connect_camAction)
        self.camMenu.addAction(self.get_camlistAction)
        self.camMenu.addAction(self.add_camAction)

        self.modeMenu = QMenu("Режим", self)
        self.MenuBar.addMenu(self.modeMenu)
        self.frame_modeAction = QAction('Покадровый', self)
        self.line_modeAction = QAction('Потоковый', self)
        self.custom_modeAction = QAction('По массиву изображений', self)
        self.modeMenu.addAction(self.frame_modeAction)
        self.modeMenu.addAction(self.line_modeAction)
        self.modeMenu.addAction(self.custom_modeAction)

        self.recordMenu = QMenu("Запись", self)
        self.MenuBar.addMenu(self.recordMenu)
        self.start_recAction = QAction('Начать запись', self)
        self.stop_recAction = QAction('Прекратить запись', self)
        self.stop_recAction.setEnabled(False)
        self.save_cfgAction = QAction('Сохранять в...', self)
        self.recordMenu.addAction(self.start_recAction)
        self.recordMenu.addAction(self.stop_recAction)
        self.recordMenu.addAction(self.save_cfgAction)


        self.aiMenu = QMenu("Интеллект", self)
        self.MenuBar.addMenu(self.aiMenu)
        self.ai_statusAction = QAction('Статус: интеллект отключен', self)
        self.ai_cfgAction = QAction('Настройки', self)
        self.aiMenu.addAction(self.ai_statusAction)
        self.aiMenu.addAction(self.ai_cfgAction)

        self.controlMenu = QMenu("Управление", self)
        self.MenuBar.addMenu(self.controlMenu)
        self.exitAction = QAction('Выход', self)
        self.exitAction.triggered.connect(self.exit_app)
        self.helpAction = QAction('Справка', self)
        self.controlMenu.addAction(self.helpAction)
        self.controlMenu.addAction(self.exitAction)


        self.screen = QLabel(self, alignment=Qt.AlignCenter)
        self.pixmap = QPixmap('temp_img/4custom/1.png').scaled(self.cfg['resolution']['width'],
                                                               self.cfg['resolution']['height'])
        self.screen.setPixmap(self.pixmap)
        self.screen.resize(self.cfg['resolution']['width'], self.cfg['resolution']['height'])
        self.screen.move(0, 50)
        self.screen.setText(f'{self.cfg["resolution"]["width"]}, {self.cfg["resolution"]["height"]}')
        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.screen)
        self.setLayout(self.hbox)

        self.setGeometry(0, 0, 100, 100)
        self.setWindowTitle('Наблюдатель: пользовательский терминал')
        self.setWindowIcon(QIcon('icon.ico'))
        self.showFullScreen()


    def get_img_path(self):
        if self.cfg['mode'] == 'custom':
            return '/temp_img/4custom/'

    def setImage(self, image='/temp_img/4custom/1.png'):
        self.pixmap.load(image)
        self.screen.setPixmap(self.pixmap)

    def exit_app(self):
        self.close()


app = QApplication(sys.argv)
window = Main(cfg_parser.parse('config.cfg'))
sys.exit(app.exec_())
