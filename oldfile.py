import time
import pyupbit
import datetime

access = "rrMenVhjvMRyD87qWjbQcRzDm7LL8DDdYyoB45sO"
secret = "EkfxrlAYNBbxDUlwmhMCOmS4B0twHAzEVwk6nY5I"

number_of_coins_to_trade = ["KRW-BTC", "KRW-ETH"]

def get_target_price(ticker, k):#per day
    #"""변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[1]['open'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_target_price2(ticker, k):#per hour
    #"""변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=2)
    target_price2 = df.iloc[1]['open'] + (df.iloc[1]['high'] - df.iloc[1]['low']) * k
    return target_price2

def get_target_price3(ticker):#per hour
    #"""변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=1)
    target_price3 = df.iloc[0]['open'] 
    return target_price3

def get_buy_price(ticker):
    if start_time < now < start_time + datetime.timedelta(hours=6):
        wish_price = get_target_price(ticker, 0.6)
        #print("dldl")
    else: #start_time - datetime.timedelta(hours=6) < now < end_time - datetime.timedelta(seconds=10):
        wish_price = get_target_price2(ticker, 0.2)
        #print("qwqw")
    a = ticker[4:]
    print(a + " 매수 목표 가격 : " + str(wish_price))
    return 0

def get_sell_price(ticker):
    target_price = get_target_price(ticker, 0.6)
    target_price2 = get_target_price2(ticker, 0.2)
    start_time = get_start_time(ticker)
    now = datetime.datetime.now()
    a = ticker[4:]

    if start_time < now < start_time + datetime.timedelta(hours=6):
        #print("qwqw")
        plus_sell_price = target_price + (target_price * 0.01)
        minus_sell_price = target_price - (target_price * 0.05)

    else:
        plus_sell_price = target_price2 + (target_price2 * 0.005)
        minus_sell_price = target_price2 - (target_price2 * 0.02)

    print(a + " 이익 목표치 : " + str(plus_sell_price))
    print(a + " 손해 방어치 : " + str(minus_sell_price))
    return 0


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

def get_reward():
    a = 100000
    b = int(upbit.get_balance("KRW"))

    for i in number_of_coins_to_trade:
        b += get_current_price(i) * upbit.get_balance(i)

    c = round(((b - a) / a) * 100,3)
    print("현재 수익률 : " + str(c) + "%")
    print("================================================")
    return 0

def any_trade():
    print(datetime.datetime.now())
    print("KRW시작금액 : 100,000")
    print("KRW보유량 : " + str(int(upbit.get_balance("KRW"))))
    # a = 100000
    # b = int(upbit.get_balance("KRW"))
    # print("현재 수익률 : " + str(((b-a)/a)*100))
    print("현재는 코인 거래가 발생하지 않았습니다.")
    get_reward()
    print("거래하시는 코인이 모두 매수목표가격보다 아래입니다.")
    print("================================================")
    for i in number_of_coins_to_trade:
        print(i + "의 현재 가격 : " + str(get_current_price(i)))
        get_buy_price(i)
        print("------------------------------------------------")
    print("================================================")
    return 0

def sell_order(ticker):
    avg = upbit.get_avg_buy_price(ticker)
    current_price = get_current_price(ticker)
    if start_time < now < start_time + datetime.timedelta(hours=6):
        sell_check = -0.05 >= (current_price - avg)/avg or (current_price - avg)/avg >= 0.01
        print("!")
    else:
        print("0")
        sell_check = -0.02 >= (current_price - avg)/avg or (current_price - avg)/avg >= 0.005
        if sell_check:
            print("hi")
    return sell_check

def sell_order2(ticker):
    avg = upbit.get_avg_buy_price(ticker)
    current_price = get_current_price(ticker)
    if start_time  + datetime.timedelta(hours=9) < now < start_time - datetime.timedelta(seconds=10):
        sell_check = -0.05 >= (current_price - avg)/avg or (current_price - avg)/avg >= 0.01
  
    return sell_check

# def printpart_for_coins(ticker, coin):
#     now = datetime.datetime.now()
#     now_price = get_current_price(ticker)
#     print("현재 거래코인은 " + coin + "입니다.")
#     print("현재시각 : " + str(now))
#     print(coin + "보유량 : " + str(upbit.get_balance(ticker)))   # KRW-BTC 조회
#     print("KRW보유량 : " + str(int(upbit.get_balance("KRW"))))  # 보유 현금 조회
#     print(coin + "에 할당된 KRW : " + str(int(get_balance("KRW"))))
#     print("현재가격 : " + str(now_price))
#     get_buy_price(ticker)
#     get_sell_price(ticker)
#     print("==========================================")
#     return 0

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("auto trade start")

# 자동매매 시작
while True:
    try:
        #Part Of Time
        #Common
        now = datetime.datetime.now()
        #For BTC
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        now_price = get_current_price("KRW-BTC")
        #For ETH
        start_time = get_start_time("KRW-ETH")
        end_time = start_time + datetime.timedelta(days=1)
        now_price = get_current_price("KRW-ETH")
        #Numbers Of Coins
        coins = len(number_of_coins_to_trade) #number_of_coins_to_trade

        #Started Part Of printing Information About Trade

        if upbit.get_balance("BTC") > 0.00008:
        #Started Part Of Printing Information About BTC
            now = datetime.datetime.now()
            now_price = get_current_price("KRW-BTC")
            print("현재 거래코인은 BTC 입니다.")
            print("현재시각 : " + str(now))
            print("BTC보유량 : " + str(upbit.get_balance("KRW-BTC")))   # KRW-BTC 조회
            print("KRW보유량 : " + str(int(upbit.get_balance("KRW"))))  # 보유 현금 조회
            print("BTC에 할당된 KRW : " + str(int(get_balance("KRW")/coins)))
            print("현재가격 : " + str(now_price))
            get_buy_price("KRW-BTC")
            get_sell_price("KRW-BTC")
            print("==========================================")
        #Finished Part Of Printing Information About BTC

        if upbit.get_balance("ETH") > 0.0015:
        #Started Part Of Printing Information About ETH
            now = datetime.datetime.now()
            now_price = get_current_price("KRW-ETH")
            print("현재 거래코인은 ETH 입니다.")
            print("현재시각 : " + str(now))
            print("ETH보유량 : " + str(upbit.get_balance("KRW-ETH")))   # KRW-BTC 조회
            print("KRW보유량 : " + str(int(upbit.get_balance("KRW"))))  # 보유 현금 조회
            print("ETH에 할당된 KRW : " + str(int(get_balance("KRW")/coins)))
            print("현재가격 : " + str(now_price))
            get_buy_price("KRW-ETH")
            get_sell_price("KRW-ETH")
            print("==========================================")
        #Finished Part Of Printing Information About ETH

        if upbit.get_balance("ETH") < 0.0015 and upbit.get_balance("BTC") < 0.00008:
            any_trade()
        else:
            get_reward()

        #Finished Part Of printing Information About Trade



        #Started Part Of AutoTrading

        #Started Part Of AutoTrading For BTC
        #장 시작 직후
        if start_time < now < start_time + datetime.timedelta(hours=6):
            target_price = get_target_price("KRW-BTC", 0.6)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW") / coins
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
                    print("Buy : " + str(target_price))
            sell_check = sell_order("KRW-BTC")
            if sell_check:
                btc = get_balance("BTC")
                if btc > 0.00008:
                    print("Sell : " + str(current_price))
                    upbit.sell_market_order("KRW-BTC", btc*0.9995)
        #장 시작 6시간 후
        elif start_time + datetime.timedelta(hours=6) < now < end_time - datetime.timedelta(hours=15):
            #
            target_price2 = get_target_price2("KRW-BTC", 0.2)
            current_price = get_current_price("KRW-BTC")
            if target_price2 < current_price:
                krw = get_balance("KRW") / coins
                if krw > 5000:
                    if current_price <= target_price2 + (target_price2*0.0002):
                        upbit.buy_market_order("KRW-BTC", krw*0.9995)
                        print("Buy : " + str(target_price2))
            sell_check = sell_order("KRW-BTC")
            if sell_check:
                
                btc = get_balance("BTC")
                if btc > 0.00008:
                    print("Sell : " + str(current_price))
                    upbit.sell_market_order("KRW-BTC", btc*0.9995) 
        
        # #오후 6시 이후
        # elif start_time + datetime.timedelta(hours=9) < now < end_time - datetime.timedelta(seconds=10):
        #     if start_time + datetime.timedelta(hours=9) < now < end_time - datetime.timedelta(hours=10):
        #         target_price3 = get_target_price3("KRW-BTC")
        #     target_price3 = target_price3
        #     current_price = get_current_price("KRW-BTC")
        #     if target_price3 < current_price:
        #         krw = get_balance("KRW") / coins
        #         if krw > 5000:
        #             upbit.buy_market_order("KRW-BTC")
        #             print("Buy : " + str(target_price3))
        #     sell_check = sell_order2("KRW-BTC")
        #     if sell_check:
                
        #         btc = get_balance("BTC")
        #         if btc > 0.00008:
        #             print("Sell : " + str(current_price))
        #             upbit.sell_market_order("KRW-BTC", btc*0.9995) 

        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995)
        time.sleep(1)
        #Finished Part of AutoTrading For BTC

        #Started Part Of AutoTrading For ETH
        #장 시작 직후
        if start_time < now < start_time + datetime.timedelta(hours=6):
            target_price = get_target_price("KRW-ETH", 0.6)
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price:
                krw = get_balance("KRW") / coins
                if krw > 5000:
                    upbit.buy_market_order("KRW-ETH", krw*0.9995)
                    print("Buy : " + str(target_price))
            sell_check = sell_order("KRW-BTC")
            if sell_check:
                eth = get_balance("ETH")
                if eth > 0.0015:
                    print("Sell : " + str(current_price))
                    upbit.sell_market_order("KRW-ETH", eth*0.9995)
        #장 시작 6시간 후
        elif start_time + datetime.timedelta(hours=6) < now < end_time - datetime.timedelta(seconds=10):
            #
            target_price2 = get_target_price2("KRW-ETH", 0.2)
            current_price = get_current_price("KRW-ETH")
            if target_price2 < current_price:
                krw = get_balance("KRW") / coins
                if krw > 5000:
                    if current_price <= target_price2 + (target_price2*0.0002):
                        upbit.buy_market_order("KRW-ETH", krw*0.9995)
                        print("Buy : " + str(target_price2))
            sell_check = sell_order("KRW-ETH")
            if sell_check:
                
                eth = get_balance("ETH")
                if eth > 0.0015:
                    print("Sell : " + str(current_price))
                    upbit.sell_market_order("KRW-ETH", eth*0.9995) 

        else:
            eth = get_balance("ETH")
            if eth > 0.0015:
                upbit.sell_market_order("KRW-ETH", eth*0.9995)
        time.sleep(1)
        #Finished Part of AutoTrading For ETH

        #Started Part Of AutoTrading

    except Exception as e:
        print(e)
        time.sleep(1)