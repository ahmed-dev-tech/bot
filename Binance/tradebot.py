import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from binance.enums import *
# import telebot
import os
# TELE_API_KEY = os.getenv('API_KEY')
pair=input("Which token pair do you want eg.ethusdt , btcusdt: ")
tradeDuration=input("Enter Trade Duration eg.... 1m , 1d: ")

SOCKET = "wss://stream.binance.com:9443/ws/{pair}@kline_{tradeDuration}".format(pair=pair,tradeDuration=tradeDuration)

RSI_PERIOD = int(input("Set your RSI period example 14: "))
RSI_OVERBOUGHT = int(input("Set your RSI OverBought limit eg 70: "))
RSI_OVERSOLD = int(input("Set your RSI OverSold limit eg 30: "))
TRADE_SYMBOL = input("Trade Symbol (in caps)..... eg 'ETHUSD': ")
TRADE_QUANTITY = float(input("Trade Price Quantity e.g. 0.5 , 0.05: "))

opens = []
closes = []
in_position = False

client = Client(config.API_KEY, config.API_SECRET)

def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False
    return True

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global opens,closes, in_position
    
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']
    open1 = candle['o']

    if not is_candle_closed:
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
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    # order_succeeded=''
                    if order_succeeded:
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
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    # order_succeeded=''
                    if order_succeeded:
                        in_position = True
    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)
        if len(closes) > int(RSI_PERIOD):
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("all rsis calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))
            if last_rsi > int(RSI_OVERBOUGHT):
                if in_position:
                    print("Overbought! Sell! Sell! Sell!")
                    # put binance sell logic here
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    # order_succeeded=''
                    if order_succeeded:
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
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    # order_succeeded=''
                    if order_succeeded:
                        in_position = True
    #                 @bot.message_handler(func=order_succeeded)                   
    #                 def sendBuySignal(message):
    #                     bot.send_message(message.chat.id, "BUY")
    # bot.polling()
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()