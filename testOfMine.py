import time
import pyupbit
import datetime

access = "rrMenVhjvMRyD87qWjbQcRzDm7LL8DDdYyoB45sO"
secret = "EkfxrlAYNBbxDUlwmhMCOmS4B0twHAzEVwk6nY5I"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, count=2)
    target_price = df.iloc[1]['open'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        print("현재시각" + str(now))

        print("BTC보유량 : " + str(upbit.get_balance("KRW-BTC")))     # KRW-XRP 조회
        print("KRW보유량 : " + str(int(upbit.get_balance("KRW"))))         # 보유 현금 조회
        
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        # df = pyupbit.get_ohlcv("BTC-KRW", interval="day", count=2)
        # print("최저가 : " + df[0]['low'])
        # print("최고가 : " + df[0]['high'])
        # print("기준가 : " + df[1]['low'])

        now_price = get_current_price("KRW-BTC")
        print("현재가격 : " + str(now_price))

        wish_price = get_target_price("KRW-BTC", 0.6)
        print("목표가격 : " + str(wish_price))

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.6)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
                    print("Buy : " + target_price)
                    if ((current_price-target_price)/target_price) >= 0.01 or ((current_price-target_price)/target_price) <= -0.05:
                        btc = get_balance("BTC")
                        if btc > 0.00008:
                            print("Sell : " + current_price)
                            upbit.sell_market_order("KRW-BTC", btc*0.9995)
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)