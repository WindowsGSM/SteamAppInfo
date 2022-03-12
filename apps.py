import json

import requests


def main():
    """Generate apps.json"""
    response = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')
    apps = response.json()['applist']['apps']
    apps = list(filter(lambda app: 'server' in str(app['name']).lower(), apps))
    apps = sorted(apps, key=lambda x: x['appid'])

    with open('apps.json', 'w', encoding='utf-8') as fp:
        json.dump(apps, fp, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
