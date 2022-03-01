# import time
# import pyupbit
# import datetime

# access = "rrMenVhjvMRyD87qWjbQcRzDm7LL8DDdYyoB45sO"
# secret = "EkfxrlAYNBbxDUlwmhMCOmS4B0twHAzEVwk6nY5I"

# def get_target_price(ticker, k):#per day
#     #"""변동성 돌파 전략으로 매수 목표가 조회"""
#     df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
#     target_price = df.iloc[1]['open'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
#     return target_price

# def get_target_price2(ticker, k):#per hour
#     #"""변동성 돌파 전략으로 매수 목표가 조회"""
#     df = pyupbit.get_ohlcv(ticker, interval="minute60", count=2)
#     target_price2 = df.iloc[1]['open'] + (df.iloc[1]['high'] - df.iloc[1]['low']) * k
#     return target_price2

# def get_sell_price(ticker):
#     target_price = get_target_price(ticker, 0.6)
#     target_price2 = get_target_price2(ticker, 0.2)
#     start_time = get_start_time(ticker)
#     now = datetime.datetime.now()

#     if start_time < now < start_time + datetime.timedelta(hours=6):
#         #print("qwqw")
#         plus_sell_price = target_price + (target_price * 0.01)
#         minus_sell_price = target_price - (target_price * 0.05)

#     else:
#         plus_sell_price = target_price2 + (target_price2 * 0.01)
#         minus_sell_price = target_price2 - (target_price2 * 0.008)

#     print("이익 목표치 : " + str(plus_sell_price))
#     print("손해 방어치 : " + str(minus_sell_price))
#     return 0


# def get_start_time(ticker):
#     #"""시작 시간 조회"""
#     df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
#     start_time = df.index[0]
#     return start_time

# def get_balance(ticker):
#     #"""잔고 조회"""
#     balances = upbit.get_balances()
#     for b in balances:
#         if b['currency'] == ticker:
#             if b['balance'] is not None:
#                 return float(b['balance'])
#             else:
#                 return 0
#     return 0

# def get_current_price(ticker):
#     #"""현재가 조회"""
#     return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# # 로그인
# upbit = pyupbit.Upbit(access, secret)
# print("autotrade start")
