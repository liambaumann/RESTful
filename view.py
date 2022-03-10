from PyQt6.QtWidgets import *
from PyQt6 import uic


class View(QMainWindow):
    def __init__(self, controller):
        """
        init methode des Models
        Hier wird das theme , window title, erste message gesetzt und der ausfuehren button verbunden
        """

        super().__init__()
        #laedt die GUI
        uic.loadUi("restful-gui.ui", self)

        self.setWindowTitle("Language Checker")
        #Statusbar message
        self.statusbar.showMessage("Please enter text to check")


        #listener connecten
       # self.pb_.clicked.connect(controller.convert)     #ausfuehren button, Signal und Slot
        #self.pb_refresh.clicked.connect(controller.refresh)
        #self.cb_live.clicked.connect(controller.livedata)