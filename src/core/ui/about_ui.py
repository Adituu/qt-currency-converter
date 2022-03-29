from PyQt5 import (
    QtWidgets,
    QtCore
)


class AboutUI():
    def __init__(self):
        # Window
        self.about_window = QtWidgets.QDialog()
        self.about_window.setFixedSize(490, 150)
        self.about_window.setWindowTitle("About")

        # Github label
        self.github_label = QtWidgets.QLabel(self.about_window)
        self.github_label.setGeometry(QtCore.QRect(10, 30, 411, 31))
        self.github_label.setStyleSheet("font: 63 11pt 'Fira Code';")
        self.github_label.setText("https://github.com/Adituu/qt-currency-converter")

        # Version label
        self.version_label = QtWidgets.QLabel(self.about_window)
        self.version_label.setGeometry(QtCore.QRect(10, 110, 231, 41))
        self.version_label.setStyleSheet("font: 11pt 'Fira Code';")
        self.version_label.setText("Version: 0.0.1-alpha")
