import json

from steam.client import SteamClient

client = SteamClient()
client.anonymous_login()

with open('apps.json', 'r', encoding='utf-8') as fp:
    app_ids = list(map(lambda app: app['appid'], json.loads(fp.read())))
    apps = client.get_product_info(app_ids)['apps']

for app_id in app_ids:
    with open(f'AppInfo/{app_id}.json', 'w', encoding='utf-8') as fp:
        json.dump(apps[app_id], fp, indent=4, ensure_ascii=False)
