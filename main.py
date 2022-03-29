import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)

from src.core.ui.main_ui import UI


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()

    ui = UI(window)
    ui.setup_ui()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
