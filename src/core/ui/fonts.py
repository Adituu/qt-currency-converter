from PyQt5 import (
    QtGui
)


class Fonts():
    def __init__(self):
        # About button font
        self.about_btnFont = QtGui.QFont()
        self.about_btnFont.setBold(False)
        self.about_btnFont.setUnderline(False)
        self.about_btnFont.setItalic(False)
        self.about_btnFont.setWeight(50)
