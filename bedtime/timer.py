import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.count = 10

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        self.label = QtWidgets.QLabel("Countdown")
        vbox.addWidget(self.label)

        self.time_passed_qll = QtWidgets.QLabel()
        vbox.addWidget(self.time_passed_qll)       

        self.setWindowOpacity(0.1)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFont(QFont("Times", 100, QFont.Bold))
        self.adjustSize()
        self.move(QApplication.instance().desktop().screen().rect().center() - self.rect().center())

        self.timer_start()
        self.update_gui()

    def timer_start(self):
        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000) # update the timer every second 
        self.count = self.count + 2 # Make start count appear for two seconds
        self.update_gui()

    def timer_timeout(self):
        print("timer timeout")
        if self.count > 0:
            self.update_gui()
        else:
            self.close_application()

    def update_gui(self):
        self.count = self.count - 1
        text = str(self.count) + " s"
        self.time_passed_qll.setText(text)

    def close_application(self):
        sys.exit(app.exec_())

app = QtWidgets.QApplication(sys.argv)

main_window = MyMainWindow()
main_window.showFullScreen()

sys.exit(app.exec_())
