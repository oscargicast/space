# SpaceAG 48h Challenge

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Copy the file .env.sample to .env and set you own env vars.

```bash
cp .env.sample .env
```

Start the dev server for [local development](http://localhost:8000/):

```bash
docker-compose up
```

Run a command inside the docker container of the app service:

```bash
docker-compose run --rm app [command]
```

For example:

```bash
docker-compose run --rm app python src/manage.py migrate
docker-compose run --rm --service-ports app python src/manage.py runserver 0.0.0.0:8000
```

# Run tests

To execute the test run this command:

```bash
docker-compose run --rm app_test pytest
```
