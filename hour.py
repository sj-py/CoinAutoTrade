import time
import pyupbit
import datetime
import pandas as pd
import numpy as np
import winsound as sd
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

df_hour = pd.DataFrame()
df_minute = pd.DataFrame()




def get_target_price(ticker):#per day
    #"""변동성 돌파 전략으로 매수 목표가 조회"""
    df_hour = pyupbit.get_ohlcv(ticker, interval="minute60",count=1)
    target_price = df_hour.iloc[0]['open']*0.9965
    return target_price

def get_buy_price(ticker):
    df_minute = pyupbit.get_ohlcv(ticker, interval="minute60",count=1)
    if get_current_price(ticker) > get_target_price(ticker)*1.01 or get_target_price(ticker)*0.997 < get_current_price(ticker):
        target_price = df_minute.iloc[0]['open']*0.9997
    else:
        target_price = df_hour.iloc[0]['open']*0.998
    return target_price

def get_start_time(ticker):
    #"""시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    #"""잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_locked(ticker):
    #"""잔고 조회"""
    balances = upbit.get_order(ticker)
    for b in balances:
        if b['market'] == ticker:
            if b['locked'] is not None:
                return b['locked']
            else:
                return 0
    return 0

def get_ordered_price(ticker):
    balances = upbit.get_order(ticker)
    for b in balances:
        if b['market'] == ticker:
            if b['price'] is not None:
                return b['price']
            else:
                return 0
    return 0

def get_current_price(ticker):
    #"""현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

def get_reward():
    a = 100000
    b = int(upbit.get_balance("KRW"))

    for i in number_of_coins_to_trade:
        b += get_current_price(i) * upbit.get_balance(i)

    c = round(((b - a) / a) * 100,3)
    print("\r전체 수익률 : " + str(c) + "%"+"\r",)
    return 0

def get_coin_reward(ticker):
    current_price = get_current_price(ticker)
    avg = upbit.get_avg_buy_price(ticker)
    btc = get_balance("BTC")
    if btc > 0.00008:
        coin_reward = round(((current_price - avg)/avg)*100,3)
        print("\r현재 거래 수익률 : " + str(coin_reward)+"\r",)
    else:
        coin_reward = "현재 거래 없음"
        print("\r현재 거래 수익률 : " + coin_reward +"\r",)
    
    return 0

def sell_order(ticker):
    avg = upbit.get_avg_buy_price(ticker)
    current_price = get_current_price(ticker)
    if avg*btc >= 5000:
        sell_check = current_price >= avg + (avg * 0.002) or current_price / avg < 0.98
    else:
        sell_check = False
  
    return sell_check

def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 300     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

# 로그인
access = "-"
secret = "-"
upbit = pyupbit.Upbit(access, secret)
print("auto trade start",)
number_of_coins_to_trade = ["KRW-BTC"]#, "KRW-ETH"]
avg = upbit.get_avg_buy_price("KRW-BTC")

# Auto Trade
check_point1 = False
check_point2 = False
# check point
btc_check = get_balance("BTC")
if btc_check > 0.00008:
    check_point1 = True
if btc_check < 0.00008:
    check_point2 = True

#recording
f = open("수익률.txt", "w",encoding="UTF8")

while True:
    trade = 1
    try:

        krw = get_balance("KRW")
        current_price = get_current_price("KRW-BTC")
        btc = upbit.get_balance("BTC")
        avg = upbit.get_avg_buy_price("KRW-BTC")
        #print(avg)
        #Coin reward
        if btc > 0.00009:
            coin_reward = round(((current_price - avg)/avg)*100,3)
        else:
            coin_reward = "현재 거래 없음"

        #Total reward
        a = 100000
        b = int(upbit.get_balance("KRW"))
        b += int(get_current_price("KRW-BTC") * upbit.get_balance("KRW-BTC"))
        c = round(((b - a) / a) * 100,3)

        #str part
        current_price_str = str(int(current_price))
        target_price_str = str(int(get_target_price("KRW-BTC")))
        buy_price_str = str(int(avg))
        time_str = str(datetime.datetime.now())
        sell_str = str(int(avg + (avg * 0.002)))
        coin_reward_str = str(coin_reward)
        total_reward_str = str(c)
        krw_str = str(int(krw))
        btc_str = str(btc)
        btc_krw_str = str(int(get_current_price("KRW-BTC") * upbit.get_balance("KRW-BTC")))
        goal_btc_krw_str = str(int((avg + (avg * 0.002))*btc))
        trading = str(get_locked("KRW-BTC"))
        sold = sell_order("KRW-BTC")
        ordered = str(get_ordered_price("KRW-BTC"))
    
        # information

        #구매시도
        print("\
================================\n\
{0}\n\
현재 가격 : {1}\n\
구매 목표 가격 : {2}\n\
================================\n\
구매 가격 : {3} \n\
================================\n\
판매 목표 가격 : {4} \n\
================================\n\
현재 원화 보유량 : {5}\n\
현재 비트코인 평가액 : {6}\n\
비트코인 목표액 : {7}\n\
현재 거래 수익률 : {8}% \n\
전체 수익률 : {9}% \n\
주문중 : {10}\n\
주문 중인 금액 : {11}\n\
Sell_check : {12}\n\
================================\
\r\n".format(time_str,current_price_str,target_price_str,buy_price_str,sell_str,krw_str,btc_krw_str,\
goal_btc_krw_str,coin_reward_str,total_reward_str,trading, ordered, sold), end="")

        # Auto Trading

        dt = datetime.datetime.now()
        now_coin_value = upbit.get_avg_buy_price("KRW-BTC")
        now_price = get_current_price("KRW-BTC")
        avg = upbit.get_avg_buy_price("KRW-BTC")
        buy_price = get_target_price("KRW-BTC")
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        #기준 시간
        dt2 = datetime.datetime.now()


        #Buy
        if krw > 5000 and now_price < buy_price:
            upbit.buy_market_order("KRW-BTC", krw*0.9995)
            beepsound()

        #Sell
        if sell_order("KRW-BTC") and avg*1.0018 < now_price:
            upbit.sell_market_order("KRW-BTC", btc*0.9995)
            trade += 1
            print(str(trade)+"번째 거래")
            f = open("수익률.txt", "a",encoding="UTF8")
            f.write("거래 시간 : " + str(dt) + "\n" + str(trade) + "번째 거래\n" + "현재 수익률 : " + str(c) + "\n")
            f.close()
            beepsound()
            time.sleep(0.5)
            beepsound()
            time.sleep(240)
            
        # #trade초기화
        # if dt.hour != dt2.hour:
        #     trade = 1

        # #거래 중지
        # if trade == 21 and dt.hour == dt2.hour:
        #     trade = 1
        #     while dt.hour == dt2.hour:
        #         print("이번시간 거래완료")
        #         print("누적 수익률 : " + total_reward_str)

    except Exception as e:

        print(e)
        time.sleep(1)
