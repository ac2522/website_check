import time
import requests
from bs4 import BeautifulSoup
from IPython.display import Audio, display
import webbrowser

def check_changed(address, interval):
    result = requests.get(address).content
    old_web = BeautifulSoup(result, 'html.parser')
    
    changed = False
    while !changed:
        time.sleep(interval)
        result = requests.get(address).content
        updated_web = BeautifulSoup(result, 'html.parser')
        if old_web != updated_web:
            changed = True
    webbrowser.open(address)

# Example for artshop 
# check_changed("https://tstout.bigcartel.com/", 60)
