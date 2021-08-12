# ethbnbapi.py Random Scan for ETH&BNB Addresses and Transactions Made by mizogg.co.uk Get FREE ETH API KEY from https://ethplorer.io/ and Get FREE BNB API KEY from https://bscscan.com/
# Mizogg 12/08/2021 mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
# Good Luck and Happy Hunting.
import random
import eth_keys
from eth_keys import keys
import requests
import multiprocessing
from multiprocessing import Pool

x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336

r = 0
cores=2 #CPU Control Set Cores

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
        apibnb3= "&apikey=freekey" ## Get FREE API KEY from https://bscscan.com/
        #apibnb4= "&apikey=freekey" ## Get FREE API KEY from https://bscscan.com/
        #apibnb5= "&apikey=freekey" ## Get FREE API KEY from https://bscscan.com
        #apibnb6= "&apikey=freekey" ## Get FREE API KEY from https://bscscan.com/
        #mylist1 = [str(apibnb1), str(apibnb2)] # 2 API KEYS
        mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3)] # 3 API KEYS
        #mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3), str(apibnb4)] # 4 API KEYS
        #mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3), str(apibnb4), str(apibnb5), str(apibnb6)] # 6 API KEYS
        apikeysbnb=random.choice(mylist1)
        ran= random.randint(x,y)
        seed=str(ran)
        myhex = "%064x" % ran
        private_key = myhex[:64]
        private_key_bytes = bytes.fromhex(private_key)
        public_key_hex = keys.PrivateKey(private_key_bytes).public_key
        public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
        ethadd = keys.PublicKey(public_key_bytes).to_address()			#Eth address
        bnbadd = keys.PublicKey(public_key_bytes).to_address()			#BNB address
        blocs=requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd +apikeys)
        ress = blocs.json()
        TXS = dict(ress)["countTxs"]
        blocs1 = requests.get("https://api.bscscan.com/api?module=account&action=balance&address=" + bnbadd + apikeysbnb)
        ress1 = blocs1.json()
        balancebnb = dict(ress1)["result"]
        print ( 'Ethereum Address           :  ', ethadd,  '  : TX      = ',  str(TXS))
        print ( 'Binance Coin BNB Address   :  ', bnbadd,  '  : Balance = ',  str(balancebnb))
        if int(TXS) > 0 or int(balancebnb) > 0:
            print("ETH&BNBAPI.py---Random Scan for ETH&BNB Addresses Transactions/Balance---ETH&BNBAPI.py")
            print ( ' <================================= WINNER Ethereum Address With Transactions/Balance WINNER =================================>' '\n' )
            print ('Ethereum Address           :  ', ethadd,  '  : TX      = ',  str(TXS)) #Ethereum winner
            print ('Binance Coin BNB Address   :  ', bnbadd,  '  : Balance = ',  str(balancebnb)) #Binance Coin BNB winner
            print("Matching Key ==== Ethereum Address Found!!!\n PrivateKey HEX : " + myhex)
            print("Matching Key ==== Ethereum Address Found!!!\n PrivateKey DEC: " + seed)
            print ( ' <================================= WINNER ETH&BNB Address With Transactions/Balance WINNER =================================>' '\n' )
            f=open(u"winner.txt","a")
            f.write('\n=============ETH&BNB Address With Transactions/Balance=====================')
            f.write('\nPrivateKey (hex): ' + myhex)
            f.write('\nPrivateKey (dec): ' + seed)
            f.write('\n Eth Address: ' + ethadd + '  : TX      = ' + str(TXS))
            f.write('\n BNB Address: ' + bnbadd + '  : Balance = ' + str(balancebnb))
            f.write('\n=============ETH&BNB Address With Transactions/Balance=====================')
            f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' + '\n')
            f.close()
#CPU Control Command
if __name__ == '__main__':
        jobs = []
        for r in range(cores):
                p = multiprocessing.Process(target=seek, args=(r,))
                jobs.append(p)
                p.start()