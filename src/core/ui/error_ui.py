from PyQt5 import (
    QtCore,
    QtWidgets
)


class ErrorUI():
    def __init__(self):
        # Window
        self.error_window = QtWidgets.QDialog()
        self.error_window.setObjectName("Error")
        self.error_window.resize(560, 130)

        # Error label
        self.error_label = QtWidgets.QLabel(self.error_window)
        self.error_label.setGeometry(QtCore.QRect(10, 40, 541, 41))
