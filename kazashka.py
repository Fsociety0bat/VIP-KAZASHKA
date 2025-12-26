import requests
import re
from urllib.parse import urljoin
import time
import os 
from colorama import init, Fore, Back, Style
def dom2():
    logo = '''
|\     /|\__   __/(  ____ )  | \    /\(  ___  )/ ___   )(  ___  )|\     /|(  ____ \| \    /\(  ___  )  
| )   ( |   ) (   | (    )|  |  \  / /| (   ) |\/   )  || (   ) || )   ( || (    \/|  \  / /| (   ) |  
| |   | |   | |   | (____)|  |  (_/ / | (___) |    /   )| (___) || (___) || (_____ |  (_/ / | (___) |  
( (   ) )   | |   |  _____)  |   _ (  |  ___  |   /   / |  ___  ||  ___  |(_____  )|   _ (  |  ___  |  
 \ \_/ /    | |   | (        |  ( \ \ | (   ) |  /   /  | (   ) || (   ) |      ) ||  ( \ \ | (   ) |  
  \   /  ___) (___| )        |  /  \ \| )   ( | /   (_/\| )   ( || )   ( |/\____) ||  /  \ \| )   ( |  
   \_/   \_______/|/         |_/    \/|/     \|(_______/|/     \||/     \|\_______)|_/    \/|/     \|  
                                                                                                        
    '''
    print(logo)
    url =input("url>>")
    txt = input("txt file from domens:")
    with open(f"{txt}" , "r" , encoding="utf-8") as f:
        doms = f.redirect_splitliens()
    for dom in doms:
        full_url = f"{url}{dom}"
        r =requests.get(full_url)
        if r.status_code ==200:
            print("OK - " , full_url)
        else:
            print("ERROR - " ,r.status_code ,"--" , full_url)
    input("Enter to exit")
    os.system("cls")

def dom():
    logo = '''
|\     /|\__   __/(  ____ )  | \    /\(  ___  )/ ___   )(  ___  )|\     /|(  ____ \| \    /\(  ___  )  
| )   ( |   ) (   | (    )|  |  \  / /| (   ) |\/   )  || (   ) || )   ( || (    \/|  \  / /| (   ) |  
| |   | |   | |   | (____)|  |  (_/ / | (___) |    /   )| (___) || (___) || (_____ |  (_/ / | (___) |  
( (   ) )   | |   |  _____)  |   _ (  |  ___  |   /   / |  ___  ||  ___  |(_____  )|   _ (  |  ___  |  
 \ \_/ /    | |   | (        |  ( \ \ | (   ) |  /   /  | (   ) || (   ) |      ) ||  ( \ \ | (   ) |  
  \   /  ___) (___| )        |  /  \ \| )   ( | /   (_/\| )   ( || )   ( |/\____) ||  /  \ \| )   ( |  
   \_/   \_______/|/         |_/    \/|/     \|(_______/|/     \||/     \|\_______)|_/    \/|/     \|  
                                                                                                        
    '''
    print(logo)

    url = input("url>>>")
    target_domain = url.split("//")[-1].split("/")[0]
    local_time = time.strftime("%H:%M:%s" , time.localtime())

    try:
        response = requests.get(url , timeout=10)
        html = response.text
                # ------------------ 1. Subdomains ------------------
        subdomains = set(
            (item[0] or item[1]).lower()
            for item in re.findall(
                r'https?://([a-zA-Z0-9.-]+)\.[a-zA-Z]{2,}|["\']((?:[a-zA-Z0-9-]+\.)+' + re.escape(target_domain) + r')["\']',
                html,
                re.IGNORECASE
            )
            if item[0] or item[1]
        )

        # ------------------ 2. JS files ------------------
        js_files = set(
            item.lower()
            for item in re.findall(
                r'(?:src|data-[a-zA-Z0-9_-]+)=["\']([^"\'>]+\.js)["\']',
                html,
                re.IGNORECASE
            )
            if item
        )

        # ------------------ 3. Other links ------------------
        other_links = set(
            item.lower()
            for item in re.findall(
                r'(?:href|action)=["\']([^"\'>]+)["\']',
                html,
                re.IGNORECASE
            )
            if item
        )

    print("subdomains:")
    dums =[]
    for link in subdomains:
        full_link = urljoin(url ,link)
        dums.append(full_link)
        print(local_time, "-" , full_link)
    for dum in dums:
        r = requests.get(dum)
        print(local_time , f"{r.status_code} - " , full_link)

    print(".js file :")
    ll = []
    for link  in js_files:
        full_link = urljoin(url ,link)
        ll.append(full_link)
        print(local_time , "-" , full_link)
    for l in ll:
        r = requests.get(l)
        print(local_time , f"{r.status_code} - " , l)
    except requests.exceptions.RequestException as e:
        print(e)
    input("Enter to exit")
    os.system("cls")

while True:
    logo = '''
|\     /|\__   __/(  ____ )  | \    /\(  ___  )/ ___   )(  ___  )|\     /|(  ____ \| \    /\(  ___  )  
| )   ( |   ) (   | (    )|  |  \  / /| (   ) |\/   )  || (   ) || )   ( || (    \/|  \  / /| (   ) |  
| |   | |   | |   | (____)|  |  (_/ / | (___) |    /   )| (___) || (___) || (_____ |  (_/ / | (___) |  
( (   ) )   | |   |  _____)  |   _ (  |  ___  |   /   / |  ___  ||  ___  |(_____  )|   _ (  |  ___  |  
 \ \_/ /    | |   | (        |  ( \ \ | (   ) |  /   /  | (   ) || (   ) |      ) ||  ( \ \ | (   ) |  
  \   /  ___) (___| )        |  /  \ \| )   ( | /   (_/\| )   ( || )   ( |/\____) ||  /  \ \| )   ( |  
   \_/   \_______/|/         |_/    \/|/     \|(_______/|/     \||/     \|\_______)|_/    \/|/     \|  
                                                                                                        
    '''
    print(logo)
    print("1 - search for subdomains in HTML code")
    print("2 - Brute force subdomains")
    x = input(">>>")
    if x =="1":
        dom()
    if x =="2":
        dom2()