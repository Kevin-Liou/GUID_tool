# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
from GUID_UI import Ui_MainWindow
import uuid, sys, os

def InputStr(Str):
    if sys.version > '3':
        OutStr = input(Str)
    else:
        OutStr = raw_input(Str)
    return OutStr

def GenerateGUID():
    NewGUID = str(uuid.uuid4()).upper()
    return NewGUID

def GUIDConversion(GUID):
    if "-" in GUID:
        NewGUID = "0x"+GUID[6:8]+", 0x"+GUID[4:6]+", 0x"+GUID[2:4]+", 0x"+GUID[0:2]+ \
                ", 0x"+GUID[11:13]+", 0x"+GUID[9:11]+ \
                ", 0x"+GUID[16:18]+", 0x"+GUID[14:16]+ \
                ", 0x"+GUID[19:21]+", 0x"+GUID[21:23]+ \
                ", 0x"+GUID[24:26]+", 0x"+GUID[26:28]+", 0x"+GUID[28:30]+", 0x"+GUID[30:32]+", 0x"+GUID[32:34]+", 0x"+GUID[34:36]
    elif "," in GUID:
        NewGUID = GUID[20:22]+GUID[14:16]+GUID[8:10]+GUID[2:4]+"-"+GUID[32:34]+GUID[26:28]+"-"+GUID[44:46]+GUID[38:40]+"-"+ \
                  GUID[50:52]+GUID[56:58]+"-"+GUID[62:64]+GUID[68:70]+GUID[74:76]+GUID[80:82]+GUID[86:88]+GUID[92:94]
    return NewGUID

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.GenGUIDButton.setText('GenGUIDButton')
        self.clicked_counter = 0
        self.ui.GenGUIDButton.clicked.connect(self.GenButtonClicked)

    def GenButtonClicked(self):
        self.clicked_counter += 1
        v = self.ui.Number.value()
        print(f"You clicked "+ str(v) + " times.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())