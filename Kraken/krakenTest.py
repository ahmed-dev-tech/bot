import requests
import time
import json, pprint
import keyboard
import sys
import os
# Attaches auth headers and returns results of a POST request
def kraken_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['API-Key'] = api_key
    # get_kraken_signature() as defined in the 'Authentication' section
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)             
    req = requests.post((api_url + uri_path), headers=headers, data=data)
    return req
def krakenBot():
    options=input("Select options:\nPress 1 to view all assets detail\nPress 2 to Get Tradable Asset Pairs\nPress 3 to Get Ticker Information\nPress 4 to Get OHLC Data\nPress 5 to Get Order Book\npress 6 to Get Recent Trades\nPress 7 to Get open orders\nPress 8 to Get close orders\nPress 9 to Get Open Positions\n")
    if options=="1":
        resp = requests.get('https://api.kraken.com/0/public/Assets')
        pprint.pprint(resp.json())
        boolAssetPair=input("\nDo you want specific Asset pairs?(y/n): ")
        if(boolAssetPair=="y"):
            assetPairs=input("Enter your asset pairs e.g. XBT,ETH : ")
            resp = requests.get('https://api.kraken.com/0/public/Assets?asset={assetPairs}'.format(assetPairs=assetPairs))
            pprint.pprint(resp.json())
        else:
            re=input("Do you want to rerun Program (y/n): ")
            if re=="y":
                krakenBot()
            else:
                sys.exit()
    elif options=="2":
        assetPairs=input("Enter your asset pairs e.g. XXBTZUSD,XETHXXBT: ")
        resp = requests.get('https://api.kraken.com/0/public/AssetPairs?pair={assetPairs}'.format(assetPairs=assetPairs))
        pprint.pprint(resp.json())
        boolAssetInfo=input("\nDo you want specific Asset info like 'leverage' 'fees' 'margin'?(y/n): ")
        if boolAssetInfo=="y":
            AssetInfo=input("\nWhich info do you want: 'leverage' or 'fees' or 'margin' : ")
            resp = requests.get('https://api.kraken.com/0/public/AssetPairs?pair={assetPairs}&info={AssetInfo}'.format(assetPairs=assetPairs,AssetInfo=AssetInfo))
            pprint.pprint(resp.json())
        else:
            re=input("Do you want to rerun Program (y/n): ")
            if re=="y":
                krakenBot()
            else:
                sys.exit()
    elif options=="3":
        pair=input("To get live Ticker Info Enter pair e.g. XBTUSD: ")
        flag=True
        while(flag):
            time.sleep(3)
            resp = requests.get('https://api.kraken.com/0/public/Ticker?pair={pair}'.format(pair=pair))
            pprint.pprint(resp.json())
            print("Press Esc to exit")
            if keyboard.is_pressed('Esc'):
                print("\nyou pressed Esc, so exiting...")
                flag=False
        re=input("Do you want to rerun Program (y/n): ")
        if re=="y":
            krakenBot()
        else:
            sys.exit()
    elif options=="4":
        pair=input("To get live Ticker Info Enter pair e.g. XBTUSD: ")
        resp = requests.get('https://api.kraken.com/0/public/OHLC?pair={pair}'.format(pair=pair))
        boolOHLC=input("Do you want to get data by specific time interval?(y/n): ")
        if boolOHLC=="y":
            interval=input("Set you interval(in minutes) 1 5 15 30 60 240 1440 10080 21600: ")
            resp = requests.get('https://api.kraken.com/0/public/OHLC?pair={pair}&interval={interval}'.format(pair=pair,interval=interval))
            pprint.pprint(resp.json())  
        else:
            re=input("Do you want to rerun Program (y/n): ")
            if re=="y":
                krakenBot()
            else:
                sys.exit()
    elif options=="5":
        pair=input("Enter pair e.g. XBTUSD: ")
        resp = requests.get('https://api.kraken.com/0/public/Depth?pair={pair}'.format(pair=pair))
        pprint.pprint(resp.json())
        boolOrderBookCount=input("Do you want to get Order book by specific count ? (y/n): ")
        if boolOrderBookCount=='y':
            orderBookCountValue=input("count value: 2 , 100 , 250: ")
            resp = requests.get('https://api.kraken.com/0/public/Depth?pair={pair}&count={orderBookCountValue}'.format(pair=pair,orderBookCountValue=orderBookCountValue))
            pprint.pprint(resp.json())
        else:
            re=input("Do you want to rerun Program (y/n): ")
            if re=="y":
                krakenBot()
            else:
                sys.exit()
    elif options=="6":
        pair=input("Enter pair e.g. XBTUSD: ")
        resp = requests.get('https://api.kraken.com/0/public/Trades?pair={pair}'.format(pair=pair))
        pprint.pprint(resp.json())
        boolSpecificTimestamp=input("Do you want to get data by specific timestamp ? (y/n): ")
        if boolSpecificTimestamp=='y':
            SpecificTimestamp=input("timestamp value: e.g. 1616663618 : ")
            resp = requests.get('https://api.kraken.com/0/public/Trades?pair={pair}&since={SpecificTimestamp}'.format(pair=pair,SpecificTimestamp=SpecificTimestamp))
            pprint.pprint(resp.json())
        else:
            re=input("Do you want to rerun Program (y/n): ")
            if re=="y":
                krakenBot()
            else:
                sys.exit()
    elif options=="7":
# Read Kraken API key and secret stored in environment variables
        api_url = "https://api.kraken.com"
        in_api_key = input("Enter Your API Key: ")
        in_api_secret = input("Enter Your API secret: ")
        api_key = in_api_key
        api_sec = in_api_secret
        # Construct the request and print the result
        resp = kraken_request('/0/private/OpenOrders', {
            "nonce": str(int(1000*time.time())),
            "trades": True
        }, api_key, api_sec)
        print(resp.json())
        re=input("Do you want to rerun Program (y/n): ")
        if re=="y":
            krakenBot()
        else:
            sys.exit()
    elif options=="8":
    # Read Kraken API key and secret stored in environment variables
        api_url = "https://api.kraken.com"
        in_api_key = input("Enter Your API Key: ")
        in_api_secret = input("Enter Your API secret: ")
        api_key = in_api_key
        api_sec = in_api_secret
        # Construct the request and print the result
        # Construct the request and print the result
        resp = kraken_request('/0/private/ClosedOrders', {
            "nonce": str(int(1000*time.time())),
            "userref": 36493663
        }, api_key, api_sec)
        print(resp.json())
        re=input("Do you want to rerun Program (y/n): ")
        if re=="y":
            krakenBot()
        else:
            sys.exit()
    elif options=="9":
        # Read Kraken API key and secret stored in environment variables
        api_url = "https://api.kraken.com"
        in_api_key = input("Enter Your API Key: ")
        in_api_secret = input("Enter Your API secret: ")
        api_key = in_api_key
        api_sec = in_api_secret
        # Construct the request and print the result
        resp = kraken_request('/0/private/OpenPositions', {
            "nonce": str(int(1000*time.time())),
            "docalcs": True
        }, api_key, api_sec)

        print(resp.json())
        re=input("Do you want to rerun Program (y/n): ")
        if re=="y":
            krakenBot()
        else:
            sys.exit()
    else:
        re=input("Do you want to rerun Program (y/n): ")
        if re=="y":
            krakenBot()
        else:
            sys.exit()
if __name__ == "__main__":
    krakenBot()