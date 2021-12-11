#!/bin/bash
export FLASK_APP=./src/main.py
export FLASK_ENV=development
export FLASK_RUN_HOST=127.0.0.1
export FLASK_RUN_PORT=8888
python3 -m flask run
python3 -m flask init-db