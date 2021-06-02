#!/bin/sh

set -e

until timeout -t 10 celery -A nepse_data inspect ping; do
    >&2 echo "Celery workers not available"
    sleep 1
done

echo 'Starting flower'
celery -A nepse_data flower
