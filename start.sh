#!/bin/bash

# Command to export PYTHONPATH
export PYTHONPATH=.

# migrating all changes to the database
alembic upgrade head

# Command to start uvicorn server
nohup python3 app/main.py -p >> ./backend.out &

# Keep the script running to prevent the container from exiting
tail -f ./backend.out