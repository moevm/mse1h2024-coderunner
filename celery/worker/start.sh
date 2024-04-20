#!/bin/ash

set -o errexit
set -o nounset

celery -A src.celery_configurator worker -Q jobe-1-queue,jobe-2-queue,jobe-3-queue,jobe-4-queue -l info --pool=solo