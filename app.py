# app.py

from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

BOT_ID = '980444878:AAGNvR4UA71SvvbEUmOSMEGPhwFDFu6KspI'
CHAT_ID = '@MartianWavesNode'

@app.route('/warningMessage', methods=['POST'])
def msg():
    value = request.json.get('score')
    msg = f'Warnig: sensor alert {value}'
    url = f'https://api.telegram.org/bot{BOT_ID}/sendMessage?chat_id={CHAT_ID}&text={msg}'

    req = requests.get(url)
    
    return jsonify({"msg": msg}),200
