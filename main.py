import os
import platform
import subprocess
import sys
from time import sleep

from tools.chrome import download, install, clean

url = r"https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BC59D9243-6DA9-F721-2FD3-59C04A668082%7D%26lang%3Dfr%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe"
filename = "ChromeSetup.exe"

def main():
    try:
        import requests
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "requests"], check=True)

    if os.path.exists("C:/Program Files/Google/Chrome/Application/chrome.exe"):
        print("Chrome is already installed.")
        sleep(2)
    else:
        print("Downloading Chrome...")
        if download(url, filename):
            print("Installing Chrome...")
            install(filename)
            sleep(10)
            print("Cleaning up installation files...")
            clean(filename)
        else:
            print("Download failed. Aborting installation.")
    if os.path.exists("C:/Program Files/Google/Chrome/Application/chrome.exe"):
        pass
    else:
        print("Chrome is still not installed.Please install it manually.")
        sys.exit(1)
    sleep(2)
    print("Killing chrome tasks...")
    os.system("taskkill /IM chrome.exe /F")
    print("Please wait for display...")
    sleep(5)
    os.system("cls" if platform.system() == "Windows" else "clear")

    print("Opening Chrome in kiosk mode...")

    from tools.display import main as display_main

    display_main()
    


    
if __name__ == "__main__":
    main()
