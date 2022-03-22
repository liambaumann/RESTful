from PyQt6.QtWidgets import *
from PyQt6 import uic


class view(QMainWindow):
    def __init__(self, control):
        """
        init methode des Views
        Hier wird das theme , window title, erste message gesetzt und der ausfuehren button verbunden
        """

        super().__init__()
        #laedt die GUI
        uic.loadUi("restful-gui.ui", self)

        self.setWindowTitle("Language Checker")
        #Statusbar message
        self.statusbar.showMessage("Please enter text to check")

        #listener connecten
        self.pb_check.clicked.connect(control.check)
        self.pb_reset.clicked.connect(control.reset)

    def setResult(self, result):
        self.text_result.setPlainText(result)
