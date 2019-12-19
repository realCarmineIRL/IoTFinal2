# app.py

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_ID = os.environ['BOT_ID']
CHAT_ID = os.environ['CHAT_ID']

@app.route('/warningMessage', methods=['POST'])
def msg():
    value = request.json.get('score')
    msg = f'Warnig: sensor alert {value}'
    url = f'https://api.telegram.org/bot{BOT_ID}/sendMessage?chat_id={CHAT_ID}&text={msg}'

    req = requests.get(url)
    
    return jsonify({"msg": msg}),200
