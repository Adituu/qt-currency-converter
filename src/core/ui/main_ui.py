import logging

from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets
)

from . import (
    fonts,
    about_ui,
    error_ui
)

from .. import currencies

from ... import utils

logger = logging.getLogger('main_ui')
logger.setLevel(logging.DEBUG)

logger_handler = logging.FileHandler('./log/app.main.log')
logger_handler.setLevel(logging.DEBUG)

logger_format = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')
logger_handler.setFormatter(logger_format)

logger.addHandler(logger_handler)


class UI(about_ui.AboutUI, fonts.Fonts):
    def __init__(self, main_window):
        # UIs
        about_ui.AboutUI.__init__(self)
        error_ui.ErrorUI.__init__(self)

        # Fonts
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
        self.convert_btn.clicked.connect(self.currency_convert)

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

        currencies = utils.read_currencies()

        currencies_list = [x['ID'] for x in currencies if isinstance(currencies, list)]
        currencies_list.sort()

        # Input currencies list
        self.input_currencies_list.setGeometry(QtCore.QRect(50, 130, 121, 30))
        self.input_currencies_list.addItems(currencies_list)

        # Output currencies list
        self.output_currencies_list.setGeometry(QtCore.QRect(460, 130, 121, 30))
        self.output_currencies_list.addItems(currencies_list)

        # Set central widget
        self.main_window.setCentralWidget(self.main_widget)

    def currency_convert(self):
        input_currency = self.input_currencies_list.currentText()
        output_currency = self.output_currencies_list.currentText()

        input_currency_data = self.input_currency.toPlainText()

        exchange_rate = currencies.get_exchange_rate(input_currency, output_currency)
        if len(exchange_rate) < 1:
            logger.error('Cannot get exchange rate.')
            return

        try:
            amount = float(input_currency_data) * float(exchange_rate)
        except ValueError:
            logger.error('Invalid input data.')
            return

        self.output_currency.setPlainText(f'{amount:,}')

        logger.info(f'Converted {amount} {input_currency} to {output_currency}')
