# yuhuToDo

ToDo for Yuhu.mx

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

### Version 1.0.0

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Requirements

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Composer](https://docs.docker.com/compose/install/)


## Basic Commands

### Building then  images (only the first time or when you make changes to the Dockerfile)

      $ docker compose -f docker-compose.local.yml up --build

Visit `http://127.0.0.0:8000` in your browser. Enjoy!

### Create superuser

Run

    $ docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser


### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as docker container.

Container mailpit will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With Mailpit running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Flower

You can access the flower admin interface at `http://127.0.0.1:5555` for monitoring and managing your Celery cluster.

## API Documentation

The API documentation is available at `/api/docs/` (for DRF) and `/api/schema/swagger-ui/` (for GraphQL).


### TODO

- [ ] Test with `pytest`