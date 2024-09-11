import paho.mqtt.client as mqtt
import json
from colorama import init, Style, Fore

# Initialize colorama
init()

user = 'glatz'
password = '1239'
broker = 'mqtt.eclipseprojects.io'
topico = 'senai/teste69'

def on_message(client, userdata, msg):
    try:
        message = json.loads(msg.payload.decode('utf-8'))  # Decode payload from bytes to string and then to JSON
        user = message.get("user")
        message_text = message.get("message")
        timestamp = message.get("timestamp")
        # Print user name in bold and color using colorama
        print(f"{Style.BRIGHT}{Fore.YELLOW}{user}{Style.RESET_ALL}: {message_text} - {timestamp}")  # Print timestamp along with user and message
    except json.JSONDecodeError:
        print("Received non-JSON message:", msg.payload.decode('utf-8'))

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topico)

sub = mqtt.Client()
sub.username_pw_set(user, password)
sub.on_message = on_message
sub.on_connect = on_connect
sub.connect(broker, 1883)
sub.loop_forever()
