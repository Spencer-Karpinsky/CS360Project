#!/bin/bash

exec gunicorn ToiSite.wsgi:application --bind 0.0.0.0:8000 --workers 2 
