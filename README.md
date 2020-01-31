# Pokemon Shakespeare

A simple FastAPI app that returns descriptions of Pokemon in Shakespearean
English.


## Tech Overview

This app is built from the following:

- FastAPI (with uvicorn)
- Redis (with redis-py)
- requests


The core web application itself is stateless, but due to the low ratelimit
quota of the upstream APIs, stateful caching is provided by Redis. This has
additional benefits such as: vastly improving the speed of duplicate API
requests, sharing response data between users, and allowing for multiple
workers.


## Pre-requisites

To build and run this application locally, install and configure the following
programs for your platform:

- Git (to clone the repository)
- Docker (to build, run the application, and run checks/tests)
- docker-compose (to run with a linked Redis container)

There is a set of convenient bash scripts under `bin/` for Linux users which
can quickly be adapted for other platforms.


## Building

1. Clone the repository

  ```
  $ git clone https://github.com/mbwk/pokemon_shakespeare.git
  ```


2. Build the Docker image from the top level directory of the project (i.e.
   the directory containing the `Dockerfile`)

  ```
  $ cd pokemon_shakespeare

  # For users of docker-compose
  $ docker-compose build

  # Optional: For users with access to bash
  $ bin/build.sh
  ```


3. Running the project (accessible at http://localhost:8080)

  a. Orchestration with docker-compose (recommended)
  
    ```
    $ docker-compose up
    ```

  b. Standalone (not recommended, runs without Redis)

    ```
    # Running this script by itself will spin up a container running the application
    $ bin/runserver.sh
    ```


## Usage

Assuming you have successfully spun up both the app and Redis with `docker-compose up`,
you should be able to access the application at http://localhost:8080/ with either your
browser or other HTTP client.

```
$ curl http://localhost:8080
"Hello, world!"
```

Example of retrieving a Shakespearean Pokemon description:
```
$ curl http://localhost:8080/pokemon/rayquaza
{
  "name": "rayquaza",
  "description": "'t flies still through the ozone layer,  consuming meteoroids for sustenance. The many meteoroids in its corse provide the energy 't needeth to mega evolve."
}
```

Handy automatically generated documentation can be accessed with your web browser
at: http://localhost:8080/docs


## Development

The `bin/` scripts can be used to perform development tasks.

- Formatting with black
  ```
  $ bin/format.sh
  ```

- Linting with flake8 & Type-checking with mypy
  ```
  $ bin/checks.sh
  ```

- Testing with pytest
  ```
  $ bin/tests.sh
  ```

- Running arbitrary commands within a container
  ```
  $ bin/dockerize.sh bash
  $ bin/dockerize.sh poetry show
  $ bin/dockerize.sh python
  ```
