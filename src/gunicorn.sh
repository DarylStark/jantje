#!/bin/sh
gunicorn --chdir ./ dashboard:flask_app -w 2 --threads 2 -b 0.0.0.0:80 -b [::]:80