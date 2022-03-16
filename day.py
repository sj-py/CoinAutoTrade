import time
import pyupbit
import datetime
import winsound as sd

access = "-"
secret = "-"

def get_target_price(ticker):
    #"""변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    target_price = df.iloc[0]['open']
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

def get_current_price(ticker):
    #"""현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

def get_avg_buy_price(ticker):
    #"""평균 구매가 조회"""
    return upbit.get_avg_buy_price(ticker)

def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 300     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        avg = get_avg_buy_price("KRW-BTC")
        krw = get_balance("KRW")
        btc = get_balance("BTC")
        target_price = get_target_price("KRW-BTC")
        current_price = get_current_price("KRW-BTC")

        if start_time < now < start_time + datetime.timedelta(seconds = 60): #< end_time - datetime.timedelta(seconds=10):
            print(now)
            print("구매 시도 중")
            print("구매 시도 가격 : " + str(target_price))
            if krw > 5000 and target_price > current_price:
                upbit.buy_market_order("KRW-BTC", krw*0.9995)#수수료 0.05%
            if btc * current_price > 5000:
                print(now)
                print("구매 완료")
                beepsound()
                beepsound()

        elif start_time + datetime.timedelta(seconds = 60) < now < end_time - datetime.timedelta(seconds=20) and btc > 0.00008:
            print(now)
            print("판매 시도 중")
            print("판매 시도 가격 : " + str(avg * 1.01))
            if avg * 1.01 < current_price:
                upbit.sell_market_order("KRW-BTC", btc * 0.9995)
                print(now)
                beepsound()
                beepsound()
                print("판매 완료")
                krw = get_balance("KRW")
                reward = round(krw / 100000, 3)
                print("수익률 : " + str(reward) + "%")
                print(now)
                print("거래 대기 시간")

        elif end_time - datetime.timedelta(seconds=20) < now < end_time and btc > 0.00008:
            upbit.sell_market_order("KRW-BTC", btc * 0.9995)
            print(now)
            beepsound()
            beepsound()
            print("판매 완료")
            krw = get_balance("KRW")
            reward = round(krw / 100000, 3)
            print("수익률 : " + str(reward) + "%")
            print(now)
            print("거래 대기 시간")

        else:
            print("현재 거래 없음")

    except Exception as e:
        print(e)
        time.sleep(1)