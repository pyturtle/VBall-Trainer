from PyQt5.QtWidgets import * 
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import * 
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import QPropertyAnimation
  
class Window(QMainWindow):
    width = 1920
    height = 1080 
    
    def __init__(self):
        super().__init__()

        purple = "#856FF8"
  
        self.setStyleSheet(f"background-color: {purple};")
  
        self.setWindowTitle("Color")
        self.setGeometry(0, 0, self.width, self.height)
        self.label = QLabel("VBall-Trainer", self)
        self.label.move(415, 140)
        self.label.setStyleSheet("""font-family: Time-New-Roman;
        font-size: 200px;
        color: white;
            """)
        self.label.resize(600 * 2, 200 * 2)
        self.button = QPushButton('Start Trainer', self)
        self.button.setStyleSheet("""font-family: Time-New-Roman;
        font-size: 70px;
        background-color: #23C9FF;
        border: 0;
        border-radius: 20px;
        color: white;
            """)
        self.button.resize(300 * 2, 100 * 2)
        self.button.move(650, 650)
    
        self.button.clicked.connect(self.on_click)

        self.grid_1 = QtWidgets.QLabel(self)
        self.grid_1.setGeometry(QtCore.QRect(180, 140, 400, 1000))
        self.grid_1.setText("")
        self.grid_1.setPixmap(QtGui.QPixmap("wood.png"))
        self.grid_1.setScaledContents(True)
        self.grid_1.setObjectName("grid_1")
        self.grid_1.setStyleSheet("""background-color: white;
        border-radius: 10px;
        border: 7px solid rgba(247, 108, 94, 1);
        """)
        self.grid_1.resize(400, 800)
        self.grid_1.hide()

        self.grid_2 = QtWidgets.QLabel(self)
        self.grid_2.setGeometry(QtCore.QRect(760, 140, 400, 1000))
        self.grid_2.setText("")
        self.grid_2.setPixmap(QtGui.QPixmap("wood.png"))
        self.grid_2.setScaledContents(True)
        self.grid_2.setObjectName("grid_2")
        self.grid_2.setStyleSheet("""background-color: white;
        border-radius: 10px;
        border: 7px solid rgba(245, 221, 144, 1);
        """)
        self.grid_2.resize(400, 800)
        self.grid_2.hide()

        self.grid_3 = QtWidgets.QLabel(self)
        self.grid_3.setGeometry(QtCore.QRect(1340, 140, 400, 1000))
        self.grid_3.setText("")
        self.grid_3.setPixmap(QtGui.QPixmap("wood.png"))
        self.grid_3.setScaledContents(True)
        self.grid_3.setObjectName("grid_3")
        self.grid_3.setStyleSheet("""background-color: white;
        border-radius: 10px;
        border: 7px solid rgba(108, 122, 137, 1);
        """)
        self.grid_3.resize(400, 800)
        self.grid_3.hide()

        # Black Backgrounds
        self.bg_1 = QLabel("", self)
        self.bg_1.move(180, 140)
        self.bg_1.setStyleSheet("""font-family: Time-New-Roman;
        font-size: 200px;
        border-radius: 10px;
        background-color: #f5f5dc;
            """)
        self.bg_1.resize(400, 800)
        self.bg_1.stackUnder(self.grid_1)
        self.bg_1.hide()

        self.bg_2 = QLabel("", self)
        self.bg_2.move(760, 140)
        self.bg_2.setStyleSheet("""font-family: Time-New-Roman;
        font-size: 200px;
        border-radius: 10px;
        background-color: #f5f5dc;
            """)
        self.bg_2.resize(400, 800)
        self.bg_2.stackUnder(self.grid_2)
        self.bg_2.hide()

        self.bg_3 = QLabel("", self)
        self.bg_3.move(1340, 140)
        self.bg_3.setStyleSheet("""font-family: Time-New-Roman;
        font-size: 200px;
        background-color: #f5f5dc;
        border-radius: 10px;
            """)
        self.bg_3.resize(400, 800)
        self.bg_3.stackUnder(self.grid_3)
        self.bg_3.hide()

        # Training
        QFontDatabase.addApplicationFont('myfont.ttf')

        self.training = QLabel("Training", self)
        self.training.move(260, 220)
        self.training.setStyleSheet("""
        font-family: 'Alfa Slab One', cursive;
        font-size: 50px;
        color: #F76C5E;
        background-color: transparent
            """)
        self.training.resize(400, 80)
        self.training.hide()

        # Practice
        self.practice = QLabel("Practice", self)
        self.practice.move(840, 220)
        self.practice.setStyleSheet("""font-family: 'Alfa Slab One', cursive;
        font-size: 50px;
        color: #F5DD90;
        background-color: transparent;
            """)
        self.practice.resize(400, 80)
        self.practice.hide()

        # Lock

        self.lock = QtWidgets.QLabel(self)
        self.lock.setGeometry(QtCore.QRect(230, 20, 331, 311))
        self.lock.setText("")
        self.lock.setPixmap(QtGui.QPixmap("lock.png"))
        self.lock.setScaledContents(True)
        self.lock.setObjectName("lock")
        self.lock.setStyleSheet("background: transparent; opacity: 0.5;")
        self.lock.move(1380, 360)
        self.lock.hide()

        self.opacity_effect1 = QGraphicsOpacityEffect()
  
        # setting opacity level
        self.opacity_effect1.setOpacity(0.5)

        self.opacity_effect2 = QGraphicsOpacityEffect()
  
        # setting opacity level
        self.opacity_effect2.setOpacity(0.5)

        self.opacity_effect3 = QGraphicsOpacityEffect()
  
        # setting opacity level
        self.opacity_effect3.setOpacity(0.5)

        self.opacity_effect4 = QGraphicsOpacityEffect()
  
        # setting opacity level
        self.opacity_effect4.setOpacity(0.5)

        self.lock.setGraphicsEffect(self.opacity_effect1)
        self.grid_1.setGraphicsEffect(self.opacity_effect2)
        self.grid_2.setGraphicsEffect(self.opacity_effect3)
        self.grid_3.setGraphicsEffect(self.opacity_effect4)

        # show all the widgets
        self.show()
  
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.grid_1.hide()
        self.grid_2.hide()
        self.grid_3.hide()
        self.bg_1.hide()
        self.bg_2.hide()
        self.bg_3.hide()
        self.training.hide()
        self.practice.hide()
        self.lock.hide()

    @pyqtSlot()
    def on_click(self):
        print("Clicked")

        purple = "#856FF8"
  
        self.setStyleSheet(f"background-color: {purple};")

        self.label.resize(0, 0)
        self.button.resize(0, 0)

        self.grid_1.show()
        self.grid_2.show()
        self.grid_3.show()
        self.training.show()
        self.practice.show()
        self.bg_1.show()
        self.bg_2.show()
        self.bg_3.show()
        self.lock.show()
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
window.showFullScreen()

# start the app
sys.exit(App.exec())
