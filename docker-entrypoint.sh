#!/bin/bash

set -e

if [ -z "$SKIP_INIT_DB" ]
then
    python3 -m flask init-db
fi

python3 -m flask run
