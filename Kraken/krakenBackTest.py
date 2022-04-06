import backtrader as bt
import datetime

class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=1)
        
        if self.rsi > 70 and self.position:
            self.close()


cerebro = bt.Cerebro()


fromdate = datetime.datetime.strptime('2017-06-01', '%Y-%m-%d') #set your start date here as of kraken_rig_runner.py's line
todate = datetime.datetime.strptime('2017-06-14', '%Y-%m-%d')

data = bt.feeds.GenericCSVData(dataname='save.csv', dtformat=2, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)

cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)

cerebro.run()

cerebro.plot()




