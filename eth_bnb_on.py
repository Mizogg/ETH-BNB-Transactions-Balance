# ethon_bnb_on.py Random ETH&BNB addresses and Private Keys.Online scan Get FREE ETH API KEY from https://ethplorer.io/ and Get FREE BNB API KEY from https://bscscan.com/
# Good Luck and Happy Hunting. Made by mizogg.co.uk 11/08/2021
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
import sys
from ecdsa import SigningKey, SECP256k1
import sha3
import random
import requests
import json
import multiprocessing
from multiprocessing import Pool

r = 0
cores=2 #CPU Control Set Cores set ammount to API KEYS USED

def seek(r):
    while True:
        api1="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
        api2="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
        #api3="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
        #api4="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
        #api5="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
        #api6="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
        mylist = [str(api1), str(api2)] # 2 API KEYS
        #mylist = [str(api1), str(api2), str(api3), str(api4)] # 4 API KEYS
        #mylist = [str(api1), str(api2), str(api3), str(api4), str(api5), str(api6)] # 6 API KEYS
        apikeys=random.choice(mylist)
        apibnb1= "&apikey=freekey" ## Get FREE API KEY from https://bscscan.com/
        apibnb2= "&apikey=freekey" ## Get FREE API KEY from https://bscscan.com/
        #apibnb3= "&apikey=freekey" ## Get FREE API KEY from https://bscscan.com/
        #apibnb4= "&apikey=freekey" ## Get FREE API KEY from https://bscscan.com/
        #apibnb5= "&apikey=freekey" ## Get FREE API KEY from https://bscscan.com
        #apibnb6= "&apikey=freekey" ## Get FREE API KEY from https://bscscan.com/
        mylist1 = [str(apibnb1), str(apibnb2)] # 2 API KEYS
        #mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3)] # 3 API KEYS
        #mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3), str(apibnb4)] # 4 API KEYS
        #mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3), str(apibnb4), str(apibnb5), str(apibnb6)] # 6 API KEYS
        apikeysbnb=random.choice(mylist1)
        c1 = str (random.choice('0123456789abcdef'))
        c2 = str (random.choice('0123456789abcdef'))
        c3 = str (random.choice('0123456789abcdef'))
        c4 = str (random.choice('0123456789abcdef'))
        c5 = str (random.choice('0123456789abcdef'))
        c6 = str (random.choice('0123456789abcdef'))
        c7 = str (random.choice('0123456789abcdef'))
        c8 = str (random.choice('0123456789abcdef'))
        c9 = str (random.choice('0123456789abcdef'))
        c10 = str (random.choice('0123456789abcdef'))
        c11 = str (random.choice('0123456789abcdef'))
        c12 = str (random.choice('0123456789abcdef'))
        c13 = str (random.choice('0123456789abcdef'))
        c14 = str (random.choice('0123456789abcdef'))
        c15 = str (random.choice('0123456789abcdef'))
        c16 = str (random.choice('0123456789abcdef'))
        c17 = str (random.choice('0123456789abcdef'))
        c18 = str (random.choice('0123456789abcdef'))
        c19 = str (random.choice('0123456789abcdef'))
        c20 = str (random.choice('0123456789abcdef'))
        c21 = str (random.choice('0123456789abcdef'))
        c22 = str (random.choice('0123456789abcdef'))
        c23 = str (random.choice('0123456789abcdef'))
        c24 = str (random.choice('0123456789abcdef'))
        c25 = str (random.choice('0123456789abcdef'))
        c26 = str (random.choice('0123456789abcdef'))
        c27 = str (random.choice('0123456789abcdef'))
        c28 = str (random.choice('0123456789abcdef'))
        c29 = str (random.choice('0123456789abcdef'))
        c30 = str (random.choice('0123456789abcdef'))
        c31 = str (random.choice('0123456789abcdef'))
        c32 = str (random.choice('0123456789abcdef'))
        c33 = str (random.choice('0123456789abcdef'))
        c34 = str (random.choice('0123456789abcdef'))
        c35 = str (random.choice('0123456789abcdef'))
        c36 = str (random.choice('0123456789abcdef'))
        c37 = str (random.choice('0123456789abcdef'))
        c38 = str (random.choice('0123456789abcdef'))
        c39 = str (random.choice('0123456789abcdef'))
        c40 = str (random.choice('0123456789abcdef'))
        c41 = str (random.choice('0123456789abcdef'))
        c42 = str (random.choice('0123456789abcdef'))
        c43 = str (random.choice('0123456789abcdef'))
        c44 = str (random.choice('0123456789abcdef'))
        c45 = str (random.choice('0123456789abcdef'))
        c46 = str (random.choice('0123456789abcdef'))
        c47 = str (random.choice('0123456789abcdef'))
        c48 = str (random.choice('0123456789abcdef'))
        c49 = str (random.choice('0123456789abcdef'))
        c50 = str (random.choice('0123456789abcdef'))
        c51 = str (random.choice('0123456789abcdef'))
        c52 = str (random.choice('0123456789abcdef'))
        c53 = str (random.choice('0123456789abcdef'))
        c54 = str (random.choice('0123456789abcdef'))
        c55 = str (random.choice('0123456789abcdef'))
        c56 = str (random.choice('0123456789abcdef'))
        c57 = str (random.choice('0123456789abcdef'))
        c58 = str (random.choice('0123456789abcdef'))
        c59 = str (random.choice('0123456789abcdef'))
        c60 = str (random.choice('0123456789abcdef'))
        c61 = str (random.choice('0123456789abcdef'))
        c62 = str (random.choice('0123456789abcdef'))
        c63 = str (random.choice('0123456789abcdef'))
        c64 = str (random.choice('0123456789abcdef'))
        magic = (c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34+c35+c36+c37+c38+c39+c40+c41+c42+c43+c44+c45+c46+c47+c48+c49+c50+c51+c52+c53+c54+c55+c56+c57+c58+c59+c60+c61+c62+c63+c64)
        hex_priv_key = str(magic)
        keccak = sha3.keccak_256()
        priv = SigningKey.from_string(string=bytes.fromhex(hex_priv_key), 
                                  curve=SECP256k1)
        pub = priv.get_verifying_key().to_string()
        keccak.update(pub)
        kec = keccak.hexdigest()[24:]
        ethadd = '0x' + kec
        bnbadd = '0x' + kec
        privatekey = priv.to_string().hex()
        blocs=requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd +apikeys)
        ress = blocs.json()
        TXS = dict(ress)["countTxs"]
        blocs1 = requests.get("https://api.bscscan.com/api?module=account&action=balance&address=" + bnbadd + apikeysbnb)
        ress1 = blocs1.json()
        balancebnb = dict(ress1)["result"]
        print ( 'Ethereum ETH Address           :  ', ethadd,  '  : TX       = ',  str(TXS))
        print ( 'Binance Coin BNB Address       :  ', ethadd,  '  : Balance  = ',  str(balancebnb))
        #print('\nPrivate key: ', priv.to_string().hex(), '\nAddress: ', ethadd, '  : TX = '  +  str(TXS))
        if int(TXS) > 0:
            print ( 'Found Found Found Found Found Found Found Found Found Found Found Found ')
            print ( 'Ethereum ETH Address           :  ', ethadd,  '  : TX       = ',  str(TXS))
            print ( 'Binance Coin BNB Address       :  ', ethadd,  '  : Balance  = ',  str(balancebnb))
            print ( 'Found Found Found Found Found Found Found Found Found Found Found Found ')
            f=open("winner.txt","a")
            f.write('\nPrivate key:'+ priv.to_string().hex())
            f.write('\n Eth Address: ' + ethadd + '  : TX      = ' + str(TXS))
            f.write('\n BNB Address: ' + bnbadd + '  : Balance = ' + str(balancebnb))
            f.close()
#CPU Control Command
if __name__ == '__main__':
        jobs = []
        for r in range(cores):
                p = multiprocessing.Process(target=seek, args=(r,))
                jobs.append(p)
                p.start()