#!/usr/bin/env bash
# exit on error
set -o errexit


docker-compose -f dc-local.yml build

docker-compose -f dc-local.yml up