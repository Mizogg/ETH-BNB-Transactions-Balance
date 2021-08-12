#Mizogg.co.uk 09/06/21 BNB.py (BNB Binance Smart Chain Random Scanner With Transaction Checking)
#Install all Modules
#pip3 install bit chainside-btcpy eth_keys eth-hash[pycryptodome]
import random
from random import SystemRandom
import secrets
import eth_keys
from eth_keys import keys
import requests
import json
import atexit
from time import time
from datetime import timedelta, datetime

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))

def log(txt, elapsed=None):
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + " [TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)

def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))

start = time()
atexit.register(end_log)
log("Start Program")

count=1

while True:
    ran = secrets.SystemRandom().randrange(1,115792089237316195423570985008687907852837564279074904382605163141518161494336)
    myhex = "%064x" % ran
    private_key = myhex[:64]
    private_key_bytes = bytes.fromhex(private_key)
    public_key_hex = keys.PrivateKey(private_key_bytes).public_key
    public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
    bnbadd = keys.PublicKey(public_key_bytes).to_address()			#BNB address
    count+=1
    blocs = requests.get("https://api.bscscan.com/api?module=account&action=balance&address=" + bnbadd + "&apikey=freekey") #BNB Binance Smart Chain API Must create account to be better API
    ress = blocs.json()
    balance = dict(ress)["result"]
    print ("\n " + colour_cyan + "BNB Binance Smart Chain Random Scan : " + str (count) + colour_red + " : ---Good--Luck--Happy--Hunting--Mizogg.co.uk---" + colour_cyan + "With Balance Checker" + colour_reset) # Running Display Output
    print (colour_cyan + 'BNB Binance Smart Chain Address                    ' + '  : '  + colour_red + bnbadd + '     : ' + colour_reset + 'Transactions = ' +  str(balance)) #BNB Binance Smart Chain address display
    print(colour_cyan +'PrivateKey' + ' : ' + colour_red + myhex + colour_reset + " : Date&Time" + seconds_to_str(), '\n') # Running Display Output
    if int(balance) > 0:
        print("Matching Key ==== BNB Binance Smart Chain Address Found!!!\n PrivateKey: " + myhex) #BNB Binance Smart Chain winner
        f=open(u"winner.txt","a")
        f.write('\nPrivateKey (hex): ' + myhex)
        f.write('\n BNB Address: ' + bnbadd)
        f.write('\n==================================')
        f.close()