#!/bin/sh

if [ "$NODE_ENV" = "development" ]
then
  npm start
elif [ "$NODE_ENV" = "production" ]
then
  yarn global add serve
  serve -s build
else
  echo "Unknown run NODE_ENV"
fi
