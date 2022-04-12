import numpy as np
import pandas as pd
from datetime import datetime
import vectorbt as vbt

# Kraken

# symbols = ["BTC/USDT","ETH/USDT", "LTC/USDT"]
# price = vbt.CCXTData.download(symbols,exchange='kraken')
# print(price.get())

# Prepare data

# start = '2019-01-01 UTC'  # crypto is in UTC
# end = '2020-01-01 UTC'

pair=input("Enter Pair BTCUSDT : ")
start = input("Enter Start date: yyyy-mm-dd: ")+ " UTC"  # crypto is in UTC
end = input("Enter End date: yyyy-mm-dd: ")+ " UTC"
interval=input("Enter interval 1m , 1d , 1y :  ")
binance_data = vbt.BinanceData.download(pair,start=start,end=end,interval=interval,missing_index='drop')
print(binance_data.get())

options = input("\nPress 1 for Moving Average Backtesting Strategy\n\nPress 2 for RSI Backtesting Strategy:  ")

if options == "1":
    print("Moving Averages")
    binance_data = vbt.BinanceData.download(pair,start=start,end=end,interval=interval)
    print(binance_data.get())
    up=int(input("Enter window range example 2: "))
    end=int(input("Enter window range example 101:"))
    windows = np.arange(up, end)
    fast_ma, slow_ma = vbt.MA.run_combs(binance_data.get('Close'), window=windows, r=2, short_names=['fast', 'slow'])
    entries = fast_ma.ma_crossed_above(slow_ma)
    exits = fast_ma.ma_crossed_below(slow_ma)
    fee=float(input("fee value: 0.001 "))
    print(fee)
    freq=input("freq: 1D ")
    pf_kwargs = dict(size=np.inf, fees=fee, freq=freq)
    pf = vbt.Portfolio.from_signals(binance_data.get('Close'), entries, exits, **pf_kwargs)
    print(pf[(10, 20, pair)].stats())
    pf[(10, 20, pair)].plot().show()
else:
    print("RSI")
    rsi=vbt.RSI.run(binance_data.get('Close'))
    rsi_entries=int(input("Enter RSI Below:30 "))
    rsi_exit=int(input("Enter RSI Above:70 "))
    entries=rsi.rsi_below(rsi_entries)
    exits = rsi.rsi_above(rsi_exit)
    initialCash=int(input("initial cash : 1000 "))
    pf=vbt.Portfolio.from_signals(binance_data.get('Close'),entries,exits,init_cash=initialCash)
    print(pf.stats())
    pf.plot().show()    
# # fig = pf.total_return().vbt.heatmap(
# #     x_level='fast_window', y_level='slow_window', slider_level='symbol', symmetric=True,
# #     trace_kwargs=dict(colorbar=dict(title='Total return', tickformat='%')))
# # fig.show()
