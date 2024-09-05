#!/bin/bash

# Define app variables
Version="0.0.1"
proxy_host="0.0.0.0"
proxy_port="8888"

# Define the path to the SQLite database file
DB_FILE="instance/sqlite.db"

echo "Start Goftino_Ai Builder Version $Version";

#sudo apt update && upgrade
#sudo apt install python3 python3-pip

#python3 -m venv ../env
#source ../env/bin/activate

#echo "Installing requirements";
#pip3 install -r requirements.txt

# Check if the database file exists
if [ ! -f "$DB_FILE" ]; then
    echo "Database file not found. Initializing database..."

    flask db init
    flask db migrate
    flask db upgrade

else
    echo "Database file already exists."
fi

clear

# bind flask server
echo "bind gunicorn proxy on port $proxy_host:$proxy_port";
gunicorn --workers 4 --bind $proxy_host:$proxy_port run:app