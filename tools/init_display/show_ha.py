import os

def open_kiosk_mode_in_edge(url):
    edge_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" 
    print(f"Ouverture de Home Assistant dans Chrome en mode kiosque à l'adresse {url}...")
    os.system(f'"{edge_path}" --kiosk {url}')


if __name__ == "__main__":
    
        home_assistant_url = ""    

        open_kiosk_mode_in_edge(home_assistant_url)