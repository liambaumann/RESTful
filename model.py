import json


class model:
    def __init__(self, control):
        self.result = "Testergebnis"
        self.resultJSON = json.loads('{"reliable": true,"language": "German","short": "de","prob": 45.33}')
        print(type(self.resultJSON))
        # self.webservice = webservice

    def getResult(self):
        res = "reliable: " + str(self.resultJSON["reliable"])
        res += "\nlanguage: " + self.resultJSON["language"]
        res += "\nprobability: " + str(self.resultJSON["prob"])
        return res
