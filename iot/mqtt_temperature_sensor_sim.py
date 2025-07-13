import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

try:
    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)
        client.publish("smart_building/temperature", temperature)
        print(f"Published: {temperature}°C")
        time.sleep(5)
except KeyboardInterrupt:
    client.disconnect()
