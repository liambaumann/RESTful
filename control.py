import sys
from PyQt6.QtWidgets import QApplication
import view
import model

class control:
    def __init__(self):
        self.view = view.view(self)
        self.model = model.model(self)

    def check(self):
        self.curInput = self.view.text_input.toPlainText()
        if(self.curInput != ""):
            mResult = self.model.getResult(self.curInput)
            self.view.setResult(mResult)

    def reset(self):
        self.view.setResult("")

if __name__ == '__main__':
    app = QApplication([])
    c = control()
    c.view.show()
    sys.exit(app.exec())