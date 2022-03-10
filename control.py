import sys
import view
from PyQt6.QtWidgets import QApplication
import view
import requests
import json

class Controller:
    def __init__(self):
        self.view = view.View(self)

    def reset(self) -> None:
        pass

    def refresh(self) -> None:
        pass

if __name__ == '__main__':
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())