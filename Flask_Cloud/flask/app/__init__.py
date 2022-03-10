import datetime
import json

from flask import Flask, render_template, Response
from app.dynamodb_access import get_all_readings, get_item_by_attribute


app = Flask(__name__)


def convert_to_datetime(items):
    for item in items:
        item['datetime'] = datetime.datetime.strptime(item['datetime'], "%Y-%m-%d %H:%M:%S")


@app.get('/')
def index():
    readings = get_all_readings()
    return render_template('index.html', readings=readings)


@app.get('/data')
def get_data():
    sensor1_readings = get_item_by_attribute('sensor', 'Temp Sensor 1')
    sensor2_readings = get_item_by_attribute('sensor', 'Temp Sensor 2')
    sensor3_readings = get_item_by_attribute('sensor', 'Temp Sensor 3')
    sensor4_readings = get_item_by_attribute('sensor', 'Temp Sensor 4')
    convert_to_datetime(sensor1_readings)
    convert_to_datetime(sensor2_readings)
    convert_to_datetime(sensor3_readings)
    convert_to_datetime(sensor4_readings)
    # Get the latest reading for sensor 1
    sensor1 = sorted(sensor1_readings, key=lambda item: item['datetime'])[-1]
    sensor1['temp'] = int(sensor1['temp'])
    sensor1['datetime'] = sensor1['datetime'].strftime("%Y-%m-%d %H:%M:%S")
    # Get the latest reading for sensor 2
    sensor2 = sorted(sensor2_readings, key=lambda item: item['datetime'])[-1]
    sensor2['temp'] = int(sensor2['temp'])
    sensor2['datetime'] = sensor2['datetime'].strftime("%Y-%m-%d %H:%M:%S")
    # Get the latest reading for sensor 3
    sensor3 = sorted(sensor3_readings, key=lambda item: item['datetime'])[-1]
    sensor3['temp'] = int(sensor3['temp'])
    sensor3['datetime'] = sensor3['datetime'].strftime("%Y-%m-%d %H:%M:%S")
    # Get the latest reading for sensor 4
    sensor4 = sorted(sensor4_readings, key=lambda item: item['datetime'])[-1]
    sensor4['temp'] = int(sensor4['temp'])
    sensor4['datetime'] = sensor4['datetime'].strftime("%Y-%m-%d %H:%M:%S")

    sensors = [sensor1, sensor2, sensor3, sensor4]

    return Response(json.dumps(sensors), 200, content_type='application/json')