from bottle import Bottle

frivet  = Bottle()

@frivet.route("/")
def index():
    return "<h1>Frivet: Prototype</h1>"

frivet.run(
    host="localhost",
    port=8080
)
