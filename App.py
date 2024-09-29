from flask import Flask, request
import json
import requests
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Your Telegram bot token
TOKEN = '6801259347:AAFPjxRHvs6kyfkIZw8EcKLoVUTMNlY4Du4'
ADMIN_ID = 6498551799
DATA_FILE = 'data.json'

# Load user data
def load_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

# Save user data
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.json
    if "message" in update:
        handle_message(update['message'])
    return 'ok', 200

def handle_message(message):
    chat_id = message['chat']['id']
    text = message.get('text', '')

    if text.startswith('/start'):
        start_command(chat_id, message['from']['first_name'])
    elif text.startswith('/cmds'):
        commands_command(chat_id)
    # Add more commands as needed

def start_command(chat_id, name):
    data = load_data
