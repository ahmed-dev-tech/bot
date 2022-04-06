import csv
import request
import backtrader as bt
import datetime
import requests

csvfile = open('2020_15minutes.csv', 'w', newline='')
file=csv.writer(csvfile, delimiter=',')
    

pair=input("Enter pair e.g. XBTUSD: ")
resp = requests.get('https://api.kraken.com/0/public/Trades?pair={pair}'.format(pair=pair))
print(resp.json())
boolSpecificTimestamp=input("Do you want to get data by specific timestamp ? (y/n): ")
if boolSpecificTimestamp=='y':
    SpecificTimestamp=input("timestamp value: e.g. 1616663618 : ")
    resp = requests.get('https://api.kraken.com/0/public/Trades?pair={pair}&since={SpecificTimestamp}'.format(pair=pair,SpecificTimestamp=SpecificTimestamp))
    print(resp.json())
    for data in resp:
        file.writerow(data)
    csvfile.close()
    # convert data in CSV
    # pprint.pprint(resp.json())
class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=1)
        
        if self.rsi > 70 and self.position:
            self.close()


cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname='2020_15minutes.csv', timeframe=1616663618)

cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)

cerebro.run()

cerebro.plot()




