#!/usr/bin/env bash

set -e

DOCKER_RUN="$( dirname "${BASE_SOURCE[0]}" )/bin/dockerize.sh"

$DOCKER_RUN black .

