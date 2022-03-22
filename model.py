import json
import requests


class model:
    def __init__(self, control):
        self.resJSON = ""
        self.resStr = ""
        self.req = None
        # print(type(self.resJSON))
        # self.webservice = webservice

    def getResult(self, input):
        params = {'input': input}
        self.req = requests.get('http://127.0.0.1:5000/langdetect', params=params)
        print("my req type: " + str(type(self.req)))
        self.resJSON = self.req.json()
        self.res = "reliable: " + str(self.resJSON["reliable"])
        self.res += "\nlanguage: " + self.resJSON["language"]
        self.res += "\nprobability: " + str(self.resJSON["prob"])
        return self.res
