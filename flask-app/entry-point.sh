#!/bin/sh

if [ "$MODE" = "flask" ]
then
  export FLASK_RUN_HOST=$ADDRESS
  export FLASK_RUN_PORT=$PORT
  flask run
elif [ "$MODE" = "gunicorn" ]
then
  gunicorn app:app --config=config.py
else
  echo "Unknown run MODE"
fi
