#!/bin/sh

if [ ! -f database.db ]; then
    python init.py
fi

exec "$@"
