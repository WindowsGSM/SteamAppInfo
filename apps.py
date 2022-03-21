import json

import requests
from steam.client import SteamClient


def main():
    """Generate apps.json"""
    response = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')
    apps = response.json()['applist']['apps']
    
    # filter the app doesn't contains "server" or "Server"
    apps = list(filter(lambda app: 'server' in str(app['name']).lower(), apps))

    # add the apps doesn't in the list
    apps.append({'appid': 232290, 'name': 'Day of Defeat: Source Dedicated Server'})
    
    # set up SteamClient and get product info
    client = SteamClient()
    client.anonymous_login()
    app_ids = list(map(lambda app: app['appid'], apps))
    infos = client.get_product_info(app_ids)['apps']
    
    # filter the apps whose don't contains "branches"
    apps = list(filter(lambda app: 'depots' in infos[app['appid']] and 'branches' in infos[app['appid']]['depots'], apps))
    
    # sort the list by app id
    apps = sorted(apps, key=lambda x: x['appid'])

    with open('apps.json', 'w', encoding='utf-8') as fp:
        json.dump(apps, fp, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
