import json

import requests

response = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')
apps = response.json()['applist']['apps']
apps = list(filter(lambda app: 'server' in str(app['name']).lower(), apps))
apps = sorted(apps, key=lambda x: x['appid'])

with open(f'apps.json', 'w', encoding='utf-8') as fp:
    json.dump(apps, fp, indent=4, ensure_ascii=False)
