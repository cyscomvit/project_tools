#!/bin/bash

cd /root/project_tools/Dashboard
export FLASK_APP=run
pipenv run flask run --host 0.0.0.0
