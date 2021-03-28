#!/bin/sh

if [ -n "$scrape" ]; then
    flask scrape-data
fi

exec "$@"
