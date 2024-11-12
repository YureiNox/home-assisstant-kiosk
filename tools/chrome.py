import requests
import os
import subprocess
from time import sleep

def download(url, filename):
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        return True
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
        return False

def install(filename):
    try:
        subprocess.run([filename], check=True, shell=True)
        print("Installation complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")

def clean(filename):
    try:
        os.remove(filename)
        print(f"Removed installer: {filename}")
    except OSError as e:
        print(f"Error cleaning up file: {e}")

if __name__ == "__main__":
    url = r"https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BC59D9243-6DA9-F721-2FD3-59C04A668082%7D%26lang%3Dfr%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe"
    filename = "ChromeSetup.exe"
    
    if download(url, filename):
        install(filename)
        sleep(10)
        clean(filename)
