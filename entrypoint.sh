#!/bin/sh

flask db upgrade
python app/modbus_reader.py &
flask run --host=0.0.0.0