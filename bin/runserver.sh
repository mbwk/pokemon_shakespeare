#!/usr/bin/env bash

set -e

DOCKER_RUN="$( dirname "${BASE_SOURCE[0]}" )/bin/dockerize.sh"

ARGS="-p 8080:8080" $DOCKER_RUN

