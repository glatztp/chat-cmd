import paho.mqtt.client as mqtt
import json

user = 'glatz'
password = '1239'
broker = 'mqtt.eclipseprojects.io'
topico = 'senai/teste69'

def on_message(client, userdata, msg):
    try:
        message = json.loads(msg.payload.decode('utf-8'))  # Decode payload from bytes to string and then to JSON
        user = message.get("user")
        message_text = message.get("message")
        print(f"{user}: {message_text}")
    except json.JSONDecodeError:
        print("Received non-JSON message:", msg.payload.decode('utf-8'))

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic
    client.subscribe(topico)

# Create and configure MQTT client
sub = mqtt.Client()
sub.username_pw_set(user, password)

sub.on_message = on_message
sub.on_connect = on_connect

# Connect to broker and start loop
sub.connect(broker, 1883)
sub.loop_forever()
