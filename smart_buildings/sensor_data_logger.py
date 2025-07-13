# smart_buildings/sensor_data_logger.py

import random
import time
import json

def simulate_sensor_readings(num_readings=10):
    readings = []
    for _ in range(num_readings):
        reading = {
            'temperature': round(random.uniform(18, 25), 2),
            'humidity': round(random.uniform(30, 60), 2),
            'co2': round(random.uniform(400, 1000), 2),
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        readings.append(reading)
        print(json.dumps(reading, indent=2))
        time.sleep(0.5)  # simulate delay
    return readings

if __name__ == '__main__':
    simulate_sensor_readings()
