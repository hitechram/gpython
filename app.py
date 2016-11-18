from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Ram!!"

@app.route("/new")
def hello():
    return "Hello World from new Ram!!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
