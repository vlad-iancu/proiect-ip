from flask import Flask
from config.Config import ConfigObject
from config.AppEnvironmentEnum import AppEnvironment

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(host=ConfigObject.host, port=ConfigObject.port,
            debug=ConfigObject.env == AppEnvironment.DEV)
