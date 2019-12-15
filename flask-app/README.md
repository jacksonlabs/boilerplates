# Flask-app

This is an example flask app with docker-compose.

It supports running in several modes:
 * Flask development (supporting hot reloads)
 * Flask production
 * Gunicorn with debug enabled
 * Gunicorn (default mode for container image)

Requirements to run the app locally:
 * docker
 * docker-compose

## Start

```
docker-compose up --build -d
```

## Stop

```
docker-compose down
```

## Run modes

To run in the specified modes set the environment variables as follows:

| Mode                                               | Variables                               |
| -------------------------------------------------- | --------------------------------------- |
| Flask development (default for docker-compose.yml) | `MODE=flask`<br>`FLASK_ENV=development` |
| Flask production                                   | `MODE=flask`<br>`FLASK_ENV=production`  |
| Gunicorn debug                                     | `MODE=gunicorn`<br>`DEBUG_MODE=1`       |
| Gunicorn (default for container image)             | `MODE=gunicorn`<br>`DEBUG_MODE=0`       |
