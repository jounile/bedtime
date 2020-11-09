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

        self.count = 4815

        self.intervals = (
            ('w', 604800),  # 60 * 60 * 24 * 7
            ('d', 86400),    # 60 * 60 * 24
            ('h', 3600),    # 60 * 60
            ('min', 60),
            ('seconds', 1),
        )

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
        text = str(self.display_time(self.count, 4))
        self.time_passed.setText(text)

    def display_time(self, seconds, granularity=2):
        result = []

        for name, count in self.intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return '\n'.join(result[:granularity])

    def close_application(self):
        QtWidgets.qApp.quit()


app = QtWidgets.QApplication(sys.argv)

main_window = MyMainWindow()
main_window.showFullScreen()

sys.exit(app.exec_())
