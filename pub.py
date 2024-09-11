import paho.mqtt.client as mqtt
import json
from datetime import datetime

user = 'glatz'
password = '1239'
broker = 'mqtt.eclipseprojects.io'
topico = 'senai/teste69'

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

pub = mqtt.Client()
pub.username_pw_set(user, password)
pub.on_connect = on_connect
pub.connect(broker, 1883)
pub.loop_start()

try:
    while True:
        message_text = input("")
        if message_text.lower() == 'sair':
            break

        timestamp = datetime.now().strftime('%H:%M')  # Format timestamp to hh:mm
        message = {
            "user": user,
            "message": message_text,
            "timestamp": timestamp  # Add formatted timestamp
        }
        pub.publish(topico, json.dumps(message))

finally:
    pub.loop_stop()
    pub.disconnect()
