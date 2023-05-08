#!/usr/bin/env bash
pip install -r requirements.txt
python dblog/manage.py collectstatic --no-input
python dblog/manage.py migrate
