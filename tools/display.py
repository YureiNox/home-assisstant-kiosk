import socket
import requests
import os
import json

home_assistant_port = 8123
timeout = 1  
ip_base = '192.168.1.'  
json_file = 'tools/json/main.json'  

def scan_network():
    print("Scanning réseau pour trouver Home Assistant...")
    home_assistant_devices = []

    for i in range(1, 255):
        ip = f"{ip_base}{i}"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            try:
                s.connect((ip, home_assistant_port))
                print(f"Appareil trouvé : {ip}")
                home_assistant_devices.append(ip)
            except (socket.timeout, ConnectionRefusedError):
                pass

    return home_assistant_devices

def check_ip(ip):
    url = f"http://{ip}:{home_assistant_port}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Home Assistant trouvé à l'adresse : {url}")
            return True
    except requests.ConnectionError:
        print("Appareil non trouvé ou inaccessible.")
    return False

def load_url_from_json():
    if os.path.exists(json_file):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                return data.get("url")  
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Erreur lors du chargement du fichier JSON : {e}")
            return None 
    return None  


def save_url_to_json(url):
    try:
        with open(json_file, 'w') as f:
            json.dump({"url": url}, f, indent=4) 
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de l'URL dans le fichier JSON : {e}")


def main():
    print("=== Interface de Scan Home Assistant ===")

    saved_url = load_url_from_json()
    if saved_url:
        print(f"URL trouvée dans le fichier JSON : {saved_url}")
        ip = saved_url
    else:
        print("1. Scanner le réseau pour trouver Home Assistant")
        print("2. Entrer une adresse IP manuellement")
        choice = input("Votre choix (1 ou 2) : ")

        if choice == '1':
            devices = scan_network()
            if devices:
                print("Appareils Home Assistant trouvés :")
                for idx, ip in enumerate(devices, start=1):
                    print(f"{idx}. {ip}")
                selected = int(input("Choisissez un appareil par son numéro : "))
                ip = devices[selected - 1]
                save_url_to_json(f"http://{ip}:{home_assistant_port}")  
            else:
                print("Aucun appareil Home Assistant trouvé.")
                exit()

        elif choice == '2':
            ip = input("Entrez l'adresse IP de l'appareil Home Assistant : ")
            if not check_ip(ip):
                print("Impossible d'accéder à cet appareil.")
                exit()
            save_url_to_json(f"http://{ip}:{home_assistant_port}")  
        else:
            print("Choix invalide.")
            exit()

    home_assistant_url = json.load(open(json_file))["url"]

    from tools.init_display.show_ha import open_kiosk_mode_in_edge

    open_kiosk_mode_in_edge(home_assistant_url)

if __name__ == "__main__":
    main()
