$env:FLASK_APP = ".\src\main.py"
$env:FLASK_ENV = "development"
$env:FLASK_RUN_HOST = "127.0.0.1"
$env:FLASK_RUN_PORT = "5001"
py -m flask init-db

if ($COVERAGE)
{
    coverage run -m unittest discover -v
}
else
{
    python3 -m unittest discover -v
}
