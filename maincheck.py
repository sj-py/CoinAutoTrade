from tabnanny import check
import time
import pyupbit
import datetime
import winsound as sd

access = "rrMenVhjvMRyD87qWjbQcRzDm7LL8DDdYyoB45sO"
secret = "EkfxrlAYNBbxDUlwmhMCOmS4B0twHAzEVwk6nY5I"

def main_check_price(ticker):
    #"""변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=1)
    now = datetime.datetime.now()
    target_price = df.iloc[0]['open']*0.997
    low_price = df.iloc[0]['low']
    high_price = df.iloc[0]['high']
    current_price = pyupbit.get_current_price("KRW-BTC")
    open_price = df.iloc[0]['open']
    print("\
시간 : {0}\n\
매수 목표가 : {1}\n\
최저가 : {2}\n\
최고가 : {3}\n\
현재가 : {4}\n\
시작가 : {5}\n\
".format(now,target_price,low_price,high_price,current_price, open_price), end="")
    return 0

def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 300     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
ch = True
while True:
        main_check_price("KRW-BTC")
        time.sleep(0.1)