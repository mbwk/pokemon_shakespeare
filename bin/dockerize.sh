#!/usr/bin/env bash

set -e

docker run --rm \
    -it $ARGS \
    -v $(pwd):/code \
    pokemon_shakespeare_api \
    $@

