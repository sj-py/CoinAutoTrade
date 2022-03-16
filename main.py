import time
import pyupbit
import datetime
import winsound as sd

access = "-"
secret = "-"

def get_target_price(ticker):
    #"""변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=1)
    target_price = df.iloc[0]['open']*0.997
    return target_price

def get_start_time(ticker):
    #"""시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=1)
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

#recording
f = open("수익 기록.txt", "w",encoding="UTF8")
# check_point = False
if get_balance("KRW") > 5000:
    check_point = False
    check_time = datetime.datetime.now()
elif get_balance("BTC") > 0.00008:
    check_point = True
    check_time = datetime.datetime.now()
# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(hours=1)
        avg = get_avg_buy_price("KRW-BTC")
        krw = get_balance("KRW")
        btc = get_balance("BTC")
        target_price = get_target_price("KRW-BTC")
        #시작 시간 30분뒤
        if start_time + datetime.timedelta(minutes=10) < now and check_point == False: #< end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC")
            current_price = get_current_price("KRW-BTC")
            check_time = datetime.datetime.now()
            print(now)
            print("구매 시도 중")
            print("구매 시도 가격 : " + str(target_price))
            if target_price > current_price:
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)#수수료 0.05%
                    btc = get_balance("BTC")
                if btc * current_price > 5000:
                    check_point = True
                    beepsound()
                    f = open("수익 기록.txt", "a",encoding="UTF8")
                    print(now)
                    f.write(str(now)+ "\n")
                    print("구매 완료")
                    f.write("구매 완료"+ "\n")
                    f.close()
        elif check_point and btc > 0.00008:
            btc = get_balance("BTC")
            current_price = get_current_price("KRW-BTC")
            avg = get_avg_buy_price("KRW-BTC")
            print(now)
            print("판매 시도 중")
            print("판매 시도 가격 : " + str(avg * 1.002))
            if btc > 0.00008 and avg * 1.0022 < current_price:
                upbit.sell_market_order("KRW-BTC", btc * 0.9995)
                f = open("수익 기록.txt", "a",encoding="UTF8")
                print(now)
                f.write(str(now)+"\n")
                beepsound()
                beepsound()
                print("판매 완료")
                f.write("판매 완료"+ "\n")
                krw = get_balance("KRW")
                reward = round(krw / 100000, 3)
                print("수익률 : " + str(reward) + "%")
                f.write("수익률 : " + str(reward) + "%" + "\n")
                print(now)
                f.write(str(now)+ "\n")
                print("거래 대기 시간")
                f.write("거래 대기 시간"+ "\n")
                print(now.hour,check_time.hour)
        if now.hour != check_time.hour and krw > 5000 and check_point:
            check_point = False
            print(now)
            f.write(str(now)+ "\n")
            beepsound()
            beepsound()
            beepsound()
            print("거래 재개")
            f.write("거래 재개"+ "\n")
        time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(1)