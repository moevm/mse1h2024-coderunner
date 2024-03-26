#!/bin/ash

set -o errexit
set -o pipefail
set -o nounset

flask --app src/main run --host=0.0.0.0