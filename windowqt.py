import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from RunLEDrpi import LED

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        l = LED()

        title = "LED Lights"

        #making the buttons
        redbtn = QPushButton("Turn on Red Light", self)
        yellowbtn = QPushButton("Turn on Yellow Light", self)
        greenbtn = QPushButton("Turn on Green Light", self)
        randbtn = QPushButton("Turn on Random Light", self)
        lsbtn = QPushButton("Light Show", self)
        quitbtn = QPushButton("Quit", self)
        redbtn.resize(redbtn.sizeHint())
        yellowbtn.resize(yellowbtn.sizeHint())
        greenbtn.resize(greenbtn.sizeHint())
        randbtn.resize(randbtn.sizeHint())
        redbtn.setFixedWidth(220)
        yellowbtn.setFixedWidth(220)
        greenbtn.setFixedWidth(220)
        randbtn.setFixedWidth(220)
        lsbtn.setFixedWidth(220)
        quitbtn.setFixedWidth(75)
        redbtn.clicked.connect(lambda: l.Red_LED())
        yellowbtn.clicked.connect(lambda: l.Yellow_LED())
        greenbtn.clicked.connect(lambda: l.Green_LED())
        randbtn.clicked.connect(lambda: l.Rand_LED())
        lsbtn.clicked.connect(lambda: l.LSButton())
        quitbtn.clicked.connect(QApplication.instance().quit)

        #making the Layout
        layout = QGridLayout()
        layout.addWidget(redbtn, 1,2)
        layout.addWidget(yellowbtn, 2,2)
        layout.addWidget(greenbtn, 3,2)
        layout.addWidget(randbtn, 4,2)
        layout.addWidget(lsbtn, 5,2)
        layout.addWidget(quitbtn, 8,2)

        #vbox = QVBoxLayout()
        ##vbox.addStretch(1)
        
        ##hbox = QHBoxLayout()
        ##hbox.stretch(1)
        #vbox.addWidget(redbtn)
        #vbox.addWidget(yellowbtn)
        #vbox.addWidget(greenbtn)

        ##hbox.addLayout(vbox)

        #making the window
        self.setLayout(layout)
        self.setGeometry(360, 360, 360, 360)
        self.setWindowTitle(title)
        self.show()


def main():
    application = QApplication(sys.argv)
    app = Window()
    sys.exit(application.exec_())