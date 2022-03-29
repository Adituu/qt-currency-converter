from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets
)

# UI components
from . import about_ui
from . import fonts


class UI(about_ui.AboutUI, fonts.Fonts):
    def __init__(self, main_window):
        about_ui.AboutUI.__init__(self)
        fonts.Fonts.__init__(self)

        # Main window
        self.main_window = main_window

        # Main widget
        self.main_widget = QtWidgets.QWidget(self.main_window)

        # Buttons
        self.convert_btn = QtWidgets.QPushButton(self.main_widget)
        self.reset_btn = QtWidgets.QPushButton(self.main_widget)
        self.about_btn = QtWidgets.QPushButton(self.main_widget)

        # Inputs
        self.input_currency = QtWidgets.QPlainTextEdit(self.main_widget)
        self.output_currency = QtWidgets.QPlainTextEdit(self.main_widget)

        # Box list
        self.input_currencies_list = QtWidgets.QComboBox(self.main_widget)
        self.output_currencies_list = QtWidgets.QComboBox(self.main_widget)

    def setup_ui(self):
        # Main window
        self.main_window.setFixedSize(642, 360)
        self.main_window.setWindowTitle("Currency converter")

        # Convert button
        self.convert_btn.setGeometry(QtCore.QRect(100, 320, 131, 31))
        self.convert_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convert_btn.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.convert_btn.setText("Convert")

        # Reset button
        self.reset_btn.setGeometry(QtCore.QRect(250, 320, 131, 31))
        self.reset_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_btn.setStyleSheet("background-color: rgb(164, 0, 0);")
        self.reset_btn.setText("Reset")

        # About button
        self.about_btn.setGeometry(QtCore.QRect(400, 320, 151, 31))
        self.about_btn.setFont(self.about_btnFont)
        self.about_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_btn.setStyleSheet("background-color: rgb(17, 218, 156);")
        self.about_btn.setText("About")
        self.about_btn.clicked.connect(self.about_window.show)

        # Input currency
        self.input_currency.setGeometry(QtCore.QRect(10, 60, 221, 51))
        self.input_currency.setStyleSheet("font: 60 15pt 'Fira Code';")

        # Output currency
        self.output_currency.setGeometry(QtCore.QRect(410, 60, 221, 51))
        self.output_currency.setStyleSheet("font: 60 15pt 'Fira Code';")

        # Input currencies list
        self.input_currencies_list.setGeometry(QtCore.QRect(50, 130, 121, 30))
        self.input_currencies_list.addItems(['RON', 'EUR', 'USD'])

        # Output currencies list
        self.output_currencies_list.setGeometry(QtCore.QRect(460, 130, 121, 30))
        self.output_currencies_list.addItems(['RON', 'EUR', 'USD'])

        # Set central widget
        self.main_window.setCentralWidget(self.main_widget)
