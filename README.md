# bot
write pip install keyboard in command terminal

to run kraken file goto project directory and write python krakenTest.py

all other instructions will avaliable during running of code 

# Telegram API

set your Telegram API key in .env file 


# Kraken API

set your kraken API inside Kraken folder's config.py

# Binance API

set your Binance API inside Binance folder's config.py


# Telegram Bot

# TelegramTradeBot  PRIVATE VERSION
# TelegramKrakenBot   🤖 💱
---
## Python3 Telegram Bot For Trading in Kraken exchange

![alt tag](https://github.com/reproteq/TelegramKrakenBot/blob/main/TelegramKrakenBot.gif) 

[![Alt text](https://img.youtube.com/vi/Rrmb_6cPzFE/0.jpg)](https://www.youtube.com/watch?v=Rrmb_6cPzFE)


---
> #### Requirements

rerun python -r requirements.txt

> #### Functions

  - Trading
  - Buy
  - Sell
  - Orders 
  - Balance
  - Alerts up price 
  - Alerts down price
  - Alerts percentage
  - Alerts On/Off
  - Currency prices 
  - Funding 
  - Chart 
  - Updates
  - Check status api
  - Config api

---
> #### Config

Edit files for configuration:

- You need to have or create Kraken ApiKey with alls privileges

- kraken.key

  Line1 write here your kraken Api key 56 chars

  Line2 write here your kraken secret key 88 chars




- config.json

  "user_id": "write here you telegram user_id"

  "bot_token": "write here you telegram bot_token"


---
> #### Start

Starting

To start the bot execute:

 - python3 bot.py &



Starting

To start the bot permanently so that it does not close when you close the window shell execute:

 - nohup python3 bot.py &

To start the bot permanently so that it does not close when you close the window shell and not want create nohup.out for save memory execute:

 -  nohup python3.6 bot.py >& /dev/null &




Closing

For see python3 process execute:

 - ps -ef | grep python3

now execute:

 - kill id-process bot.py


---