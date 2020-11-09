import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.count = 10

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout()
        vbox.setAlignment(Qt.AlignCenter)
        central_widget.setLayout(vbox)

        self.label = QtWidgets.QLabel("Bedtime")
        vbox.addWidget(self.label)

        self.time_passed = QtWidgets.QLabel()
        self.time_passed.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.time_passed)       

        self.setWindowOpacity(0.1)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(420, 32),
                QtWidgets.qApp.desktop().availableGeometry()
        ))

        self.setFont(QFont("Times", 200, QFont.Bold))
        self.showMaximized()

        self.timer_start()
        self.update_gui()

    def timer_start(self):
        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000) # update the timer every second 
        self.update_gui()

    def timer_timeout(self):
        if self.count > 0:
            self.update_gui()
        else:
            self.close_application()

    def update_gui(self):
        self.count = self.count - 1
        text = str(self.count) + " s"
        self.time_passed.setText(text)

    def close_application(self):
        QtWidgets.qApp.quit()


app = QtWidgets.QApplication(sys.argv)

main_window = MyMainWindow()
main_window.showFullScreen()

sys.exit(app.exec_())
