from flask import Flask

import db
import auth
import coffeerecipe

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
)

app.register_blueprint(auth.bp)
app.register_blueprint(coffeerecipe.bp)

db.init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
