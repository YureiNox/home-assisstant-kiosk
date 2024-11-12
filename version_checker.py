import json
import requests
import platform
import os

def get_current_version():
    with open('version.json') as json_file:
        data = json.load(json_file)
        return data['version']
    
def get_current_os():
    return platform.system()

def get_latest_version():
    try:
        response = requests.get('https://api.github.com/repos/YureiNox/home-assisstant-kiosk/releases/latest')
        response.raise_for_status()
        return response.json()['tag_name']
    except Exception as e:
        print('Failed to check for updates:', e)
        return None

if get_current_os() == json.load(open('version.json'))['platform']:
    print("You are using the good version!")
    if get_current_version() == get_latest_version():
        print("You are using the latest version!")
        os.system("python main.py")
    elif get_current_version() > get_latest_version():
        print("You are using a newer version than the latest one!")
        os.system("python main.py")
    elif get_current_version() < get_latest_version():
        print("You are using an older version than the latest one!")
        exit(1)
else:
    print("Your pc is not a windows computer the programme will not run on your shit!")
    exit(0)
