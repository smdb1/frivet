from bottle import Bottle

frivet = Bottle()

@frivet.route("/")
def index():
    return "<h1>Frivet: Prototype</h1>"
