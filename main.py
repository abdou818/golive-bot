import json
import requests
import base64
import time


with open('config.json') as f:
    config = json.load(f)

# ترميز التوكن إلى Base64
token_b64 = base64.b64encode(config['token'].encode('utf-8')).decode('ascii')

headers = {
    'Authorization': f"Basic {token_b64}",
    'Content-Type': 'application/json'
}


def go_live():
    payload = {
        'type': 1,
        'guild_id': config['guild_id'],
        'channel_id': config['channel_id'],
        'message': config['message']
    }

    while True:
        requests.post(
            'https://discord.com/api/v9/channels/' + config['channel_id'] + '/call',
            headers=headers,
            data=json.dumps(payload)
        )
        print("Go Live Sent")
        time.sleep(60 * 5)  # Repeat every 5 minutes

go_live()
