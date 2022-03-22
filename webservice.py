from flask import Flask, request, jsonify
from langdetect import detect_langs
from iso639 import languages

app = Flask(__name__)


@app.route('/hello')
def hello():
    name = request.args.get("name")     # liest Parameter ein
    return "Hello, " + name + "alter: " + str(20)        # Gibt response zurueck

@app.route('/langdetect')
def langdetect():
    sentence = request.args.get("input")
    result = detect_langs(sentence)
    bestlang = result[0]
    prob = bestlang.prob * 100
    short = bestlang.lang
    reliable = bestlang.prob > 0.5
    long = languages.get(part1=short).name
    return jsonify(reliable=reliable,language=long,short=short,prob=prob)

if __name__ == '__main__':
    app.run(debug=False)