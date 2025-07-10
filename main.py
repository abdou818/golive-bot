import requests
import json
import time

with open('config.json') as f:
    config = json.load(f)
    
headers = {
    'Authorization': f"Bearer {config['token']}",
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
