import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.send_file("./index.html")

@app.route("/css/base.css")
def css_base():
    return flask.send_file("./base.css")

@app.errorhandler(404)
def _404(err):
    return flask.send_file("./404.html")
