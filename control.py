import sys
import view
from PyQt6.QtWidgets import QApplication
import view
import model
import requests
import json

class control:
    def __init__(self):
        self.view = view.view(self)
        self.model = model.model(self)

    def check(self):
        mResult = self.model.getResult();
        self.view.setResult(mResult)

    def reset(self):
        self.view.setResult("")

if __name__ == '__main__':
    app = QApplication([])
    c = control()
    c.view.show()
    sys.exit(app.exec())