# import asyncio
# from binance import AsyncClient, BinanceSocketManager
# from binance.enums import *
# import pprint
# import asyncio
# from binance import AsyncClient, BinanceSocketManager


# async def main():
#     client = await AsyncClient.create()
#     bm = BinanceSocketManager(client)
#     # start any sockets here, i.e a trade socket
#     ks = bm.kline_socket('BNBBTC', interval='15m')

#     # then start receiving messages
#     async with ks as tscm:
#         while True:
#             res = await tscm.recv()
#             pprint.pprint(res)

#     await client.close_connection()

# if __name__ == "__main__":

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

from decimal import Decimal
from binance.client import Client
from binance.enums import *
from binance import ThreadedWebsocketManager
import config as Config
from datetime import datetime
import numpy
import talib
import pprint


client=Client()
TRADESYMBOL='BNBETH'

info = client.get_symbol_info(TRADESYMBOL)
for x in info["filters"]:
    if x["filterType"] == "LOT_SIZE":
        minQty = float(x["minQty"])
        maxQty = float(x["maxQty"])
        stepSize= x["stepSize"]
        print(minQty)
        print(maxQty)
        print(stepSize)

# def get_round_step_quantity(qty):
#         info = client.get_symbol_info(TRADESYMBOL)
#         print(info)
        # for x in info["filters"]:
        #     if x["filterType"] == "LOT_SIZE":
        #         minQty = float(x["minQty"])
        #         maxQty = float(x["maxQty"])
        #         stepSize= x["stepSize"]
#         if qty < minQty:
#             qty = minQty
#         return floor_step_size(qty)
# def floor_step_size(quantity):
#         step_size_dec = Decimal(str(stepSize))
#         return float(int(Decimal(str(quantity)) / step_size_dec) * step_size_dec)

# def get_quantity(asset):
#         balance = get_balance(asset=asset)
#         quantity = get_round_step_quantity(float(balance))
#         return quantity

# def get_balance(asset) -> str:
#         balance = client.get_asset_balance(asset=asset)
#         return balance['free']







