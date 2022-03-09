from tabnanny import check
import time
import pyupbit
import datetime
import winsound as sd

access = "rrMenVhjvMRyD87qWjbQcRzDm7LL8DDdYyoB45sO"
secret = "EkfxrlAYNBbxDUlwmhMCOmS4B0twHAzEVwk6nY5I"
# 로그인
upbit = pyupbit.Upbit(access, secret)

def main_check_price(ticker):
    #"""변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=1)
    now = datetime.datetime.now()
    target_price = df.iloc[0]['open']*0.997
    low_price = df.iloc[0]['low']
    high_price = df.iloc[0]['high']
    current_price = pyupbit.get_current_price("KRW-BTC")
    open_price = df.iloc[0]['open']
    #pre_rate_of_change = (round(df.iloc[0]['high']/df.iloc[0]['low'],3)-1)*100
    rate_of_change = round((df.iloc[0]['high']/df.iloc[0]['low']-1)*100,3)
    avg = upbit.get_avg_buy_price("KRW-BTC")
    sell = avg*1.0022
    percent = round(((current_price / sell)-1)*100,3)
    rate_of_now = round(((current_price / avg)-1)*100,3)
    rate_of_high = round(((df.iloc[0]['high'] / df.iloc[0]['open'])-1)*100,3)
    rate_of_low = round(((df.iloc[0]['low'] / df.iloc[0]['open'])-1)*100,3)
    rate_of_goal = round(((sell / df.iloc[0]['open'])-1)*100,3)
    krw = int(upbit.get_balance("KRW"))
    btc = upbit.get_balance("BTC")
    reward = round(((krw / 100000)-1)*100,3)
    print("\
시간 : {0}\n\
매수 목표가 : {1}\n\
최저가 : {2}\n\
최고가 : {3}\n\
시작가 : {4}\n\
현재가 : {5}\n\
변동률 : {6}%\n\
=====================\n\
현재 시간 상황\n\
현재 수익률 : {7}%\n\
목표 - 현재 : {8}%\n\
시작 - 최고 : {9}%\n\
시작 - 최저 : {10}%\n\
시작 - 목표 : {11}%\n\
원화 보유량 : {12}\n\
BTC 보유량 : {13}\n\
누적 수익률 : {14}%\n\
".format(now,target_price,low_price,high_price,open_price,current_price,rate_of_change\
    ,rate_of_now,percent,rate_of_high,rate_of_low,rate_of_goal,krw,btc,reward), end="")
    return 0

def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 300     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

# 로그인
upbit = pyupbit.Upbit(access, secret)
while True:
        main_check_price("KRW-BTC")
        time.sleep(0.1)