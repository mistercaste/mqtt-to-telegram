import os
import telebot
import paho.mqtt.client as mqtt

# Configure via environment variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
MQTT_BROKER = os.getenv('MQTT_BROKER', 'localhost')
MQTT_TOPIC = os.getenv('MQTT_TOPIC', 'security/vulnerabilities')

bot = telebot.TeleBot(TOKEN)

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result: {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    message_text = f"WARNING - Vulnerability found!*\n\n\tTopic:* {msg.topic}\n💬 *Message:* {payload}"
    print(f"Sending notification: {payload}")
    bot.send_message(CHAT_ID, message_text, parse_mode='Markdown')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)
client.loop_forever()
