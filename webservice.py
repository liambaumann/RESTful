from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello')
def hello():
    name = request.args.get("name")     # liest Parameter ein
    return "Hello, " + name + "alter: " + str(20)        # Gibt response zurueck


if __name__ == '__main__':
    app.run(debug=False)