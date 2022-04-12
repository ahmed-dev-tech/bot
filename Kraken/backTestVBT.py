import numpy as np
import pandas as pd
from datetime import datetime
import vectorbt as vbt

# Kraken

pair=input("Enter Pair BTC/USDT : ")
start = input("Enter Start date: yyyy-mm-dd: ")+ " UTC"  # crypto is in UTC
end = input("Enter End date: yyyy-mm-dd: ")+ " UTC"
interval=input("Enter interval 1m , 1d , 1y :  ")
price = vbt.CCXTData.download(pair,start=start,end=end,timeframe=interval,missing_index='drop',exchange='kraken')
print(price.get())


options = input("\nPress 1 for Moving Average Backtesting Strategy\nPress 2 for RSI Backtesting Strategy:\n")

if options == "1":
    print("Moving Averages")
    # price = vbt.CCXTData.download(pair,start=start,end=end,timeframe=interval,missing_index='drop',exchange='kraken')
    print(price.get())
    up=int(input("Enter window range example 2: "))
    end=int(input("Enter window range example 101:"))
    windows = np.arange(up, end)
    fast_ma, slow_ma = vbt.MA.run_combs(price.get('Close'), window=windows, r=2, short_names=['fast', 'slow'])
    entries = fast_ma.ma_crossed_above(slow_ma)
    exits = fast_ma.ma_crossed_below(slow_ma)
    fee=float(input("fee value: 0.001 "))
    print(fee)
    freq=input("freq: 1D ")
    pf_kwargs = dict(size=np.inf, fees=fee, freq=freq)
    initialCash=int(input("initial cash : 1000 "))
    pf = vbt.Portfolio.from_signals(price.get('Close'), entries, exits,init_cash=initialCash, **pf_kwargs)
    pf[(10, 20, pair)].plot().show()
    print(pf[(10, 20, pair)].stats())
else:
    print("RSI")
    print(price.get())
    rsi=vbt.RSI.run(price.get('Close'))
    rsi_entries=int(input("Enter RSI Below:30 "))
    rsi_exit=int(input("Enter RSI Above:70 "))
    entries=rsi.rsi_below(rsi_entries)
    exits = rsi.rsi_above(rsi_exit)
    initialCash=int(input("initial cash : 1000 "))
    pf=vbt.Portfolio.from_signals(price.get('Close'),entries,exits,init_cash=initialCash)
    pf.plot().show()
    print(pf.stats())

