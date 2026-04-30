#!/bin/bash
pip install -r requirements.txt
python evaluaciones_JuanJosePerez/manage.py collectstatic --noinput
python evaluaciones_JuanJosePerez/manage.py migrate
