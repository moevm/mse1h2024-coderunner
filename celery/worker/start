#!/bin/ash

set -o errexit
set -o nounset

celery -A src.celery_configurator worker -Q tasks-queue,replies-queue -l info --pool=solo