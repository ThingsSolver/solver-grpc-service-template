#!/usr/bin/env bash

echo Starting Gunicorn.

exec gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8080 --workers 10
