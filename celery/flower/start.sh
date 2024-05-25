#!/bin/ash

set -o errexit
set -o nounset

worker_ready() {
    celery -A src.celery_configurator inspect ping
}

until worker_ready; do
  >&2 echo 'Celery workers not available'
  sleep 1
done
>&2 echo 'Celery workers is available'

export FLOWER_UNAUTHENTICATED_API=true

celery -A src.celery_configurator  \
    --broker="${CELERY_BROKER_URL}" \
    flower