$env:FLASK_APP = ".\src\main.py"
$env:FLASK_ENV = "development"
$env:FLASK_RUN_HOST = "127.0.0.1"
$env:FLASK_RUN_PORT = "5000"
py -m flask run
py -m flask init-db
