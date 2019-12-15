# React-app

This is an example react app with docker-compose.

Note: The application in the `app` directory is a vanilla create-react-app boilerplate

It supports running in several modes:
 * NPM development (supporting hot reloads)
 * Serve production (default mode for container image)

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

| Mode                                             | Variables                                                |
| ------------------------------------------------ | -------------------------------------------------------- |
| NPM development (default for docker-compose.yml) | build.args: `BUILD=false`<br>env: `NODE_ENV=development` |
| Serve production (default for container image)   | build.args: `BUILD=true`<br>env: `NODE_ENV=production`   |

Note: Hot reloads only mount the `src` and `public` directories to the host.