import paho.mqtt.client as mqtt
import json

user = 'glatz'
password = '1239'
broker = 'mqtt.eclipseprojects.io'
topico = 'senai/teste69'

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# Create and configure MQTT client
pub = mqtt.Client()
pub.username_pw_set(user, password)

pub.on_connect = on_connect

# Connect to broker and start loop
pub.connect(broker, 1883)
pub.loop_start()

try:
    while True:
        message_text = input("")
        if message_text.lower() == 'sair':
            break

        message = {
            "user": user,
            "message": message_text
        }
        pub.publish(topico, json.dumps(message))
        print(f"Message published to topic {topico}: {message_text}")

except KeyboardInterrupt:
    print("Disconnecting...")

finally:
    pub.loop_stop()
    pub.disconnect()
