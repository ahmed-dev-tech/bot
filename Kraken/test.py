print("Bot Configurations\n")
RSI_PERIOD = int(input("length of open trades limit e.g. 10: "))
RSI_OVERBOUGHT = int(input("Set your RSI OverBought limit eg 70: "))
RSI_OVERSOLD = int(input("Set your RSI OverSold limit eg 30: "))
pair=input("Enter pair e.g. XBTUSD: ")
TRADE_QUANTITY = float(input("Trade Price Quantity e.g. 0.5 , 0.05: "))
buy_limit=int(input("Enter your Buy limit: "))
sell_limit=int(input("Enter your Sell limit: "))
api_url = "https://api.kraken.com"
in_api_key = input("Enter Your Kraken API Key: ")
in_api_secret = input("Enter Your Kraken API secret: ")
api_key = in_api_key
api_sec = in_api_secret
opens = []
flag=True
in_position = False
resp = requests.get('https://api.kraken.com/0/public/Ticker?pair={pair}'.format(pair=pair))
pprint.pprint(resp.json()['result'])
setValuePair=input("Value Pair (Symbol on terminal's left corner): ")
while(flag):
    time.sleep(3)
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair={pair}'.format(pair=pair))
    val=resp.json()['result']['{setValuePair}'.format(setValuePair=setValuePair)]
    if val['o'] < sell_limit :
        print("candle opens at {}".format(open1))
        opens.append(float(open1))
        print("opens")
        print(opens)
        if len(opens) > int(RSI_PERIOD):
            np_opens = numpy.array(opens)
            rsi = talib.RSI(np_opens, RSI_PERIOD)
            print("all rsis calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))

            if last_rsi > int(RSI_OVERBOUGHT):
                if in_position:
                    print("Overbought! Sell! Sell! Sell!")
                    # put binance sell logic here
                    resp = kraken_request('/0/private/AddOrder', {
                    "nonce": str(int(1000*time.time())),
                    "ordertype": "market",
                    "type": "sell",
                    "volume": TRADE_QUANTITY,
                    "pair": TRADE_SYMBOL,
                    }, api_key, api_sec)
                    # order_succeeded=''
                    if resp:
                        in_position = False
                    # @bot.message_handler(func=order_succeeded)                   
                    # def sendSellSignal(message):
                    #     bot.send_message(message.chat.id, "Sell")
                else:
                    print("It is overbought, but we don't own any. Nothing to do.")
            
            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("It is oversold, but you already own it, nothing to do.")
                else:
                    print("Oversold! Buy! Buy! Buy!")
                    # put binance buy order logic here
                    resp = kraken_request('/0/private/AddOrder', {
                    "nonce": str(int(1000*time.time())),
                    "ordertype": "market",
                    "type": "sell",
                    "volume": TRADE_QUANTITY,
                    "pair": TRADE_SYMBOL,
                    }, api_key, api_sec)
                    # order_succeeded=''
                    if resp:
                        in_position = True
    # if float(val['o'][0]) > sell_limit:
    #     opens.append(val['o'][0])
    #     print(opens)
    #     if len(opens) > RSI_PERIOD:
    #         np_opens = numpy.array(opens)
    #         rsi = talib.RSI(np_opens, RSI_PERIOD)
    #         print("all rsis calculated so far")
    #         print(rsi)
    #         last_rsi = rsi[-1]
    #         print("the current rsi is {}".format(last_rsi))
    #         if last_rsi > int(RSI_OVERBOUGHT):
    #             if in_position:
    #                 print("Overbought! Sell! Sell! Sell!")
                    # resp = kraken_request('/0/private/AddOrder', {
                    # "nonce": str(int(1000*time.time())),
                    # "ordertype": "market",
                    # "type": "sell",
                    # "volume": TRADE_QUANTITY,
                    # "pair": TRADE_SYMBOL,
                    # }, api_key, api_sec)
    #                 print("Buying of {TRADE_SYMBOL} at {price}!!!".format(price=val['c'][0],TRADE_SYMBOL=TRADE_SYMBOL))
    #         else:
    #             print("It is overbought, but we don't own any. Nothing to do.")
        
    #         if not resp.json()['error']:
    #             print("Sucessfully Buy {TRADE_SYMBOL} at {price}".format(price=val['c'][0],TRADE_SYMBOL=TRADE_SYMBOL))
    #         else:
    #             print("Error : {error}".format(error=resp.json()['error']))
    #         elif float(val['o'][0]) < sell_limit:
    #             print("Selling of {TRADE_SYMBOL} at {price}!!!".format(price=val['c'][0],TRADE_SYMBOL=TRADE_SYMBOL))
    #             resp = kraken_request('/0/private/AddOrder', {
    #             "nonce": str(int(1000*time.time())),
    #             "ordertype": "market",
    #             "type": "sell",
    #             "volume": TRADE_QUANTITY,
    #             "pair": TRADE_SYMBOL,
    #             }, api_key, api_sec)
    #     if not resp.json()['error']:
    #         print("Sucessfully Sell {TRADE_SYMBOL} at {price}".format(price=val['c'][0],TRADE_SYMBOL=TRADE_SYMBOL))            
    #     else:
    #         print("Current Price: {price}, not buying and selling ".format(price=val['c'][0]))