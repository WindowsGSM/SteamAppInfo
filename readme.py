import json


def main():
    """Generate README.md"""
    with open('apps.json', 'r', encoding='utf-8') as fp:
        apps = json.loads(fp.read())

    header = '''# SteamAppInfo
Get the latest steam app info json here, automatic updated every 5 minutes.

## App List
This repository only updates the dedicated server apps for game server management purposes.

'''

    table = '''| AppId | Name | AppInfo Json |\n| - | - | - |\n'''

    for app in apps:
        table += f"| `{app['appid']}` | {app['name']} | [{app['appid']}.json](AppInfo/{app['appid']}.json) |\n"
        
    with open('README.md', 'w', encoding='utf-8') as fp:
        fp.write(header + table)

if __name__ == "__main__":
    main()      
