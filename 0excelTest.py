import datetime
import pyupbit
import numpy as np

start_time = df = pyupbit.get_ohlcv("KRW-BTC", interval="day", count=1)
start_time = df.index[0]

now = datetime.datetime.now()
now_price = pyupbit.get_orderbook(ticker="KRW-BTC")["orderbook_units"][0]["ask_price"]

if start_time == now:
            now2 = "결산 시간 : " + str(now)
            now_price2 = "마지막 가격" + str(now_price)
            btc = "현재 BTC 보유량 : " + str(pyupbit.get_balance("KRW-BTC"))
            won = "현재 원화 보유량 : " + str(int(pyupbit.get_balance("KRW")))
            earn = "누적 수익률 : " + str((pyupbit.get_balance("KRW")/100000)*100)

            now2.to_excel("invest.xlsx")
            now_price2.to_excel("invest.xlsx")
            btc.to_excel("invest.xlsx")
            won.to_excel("invest.xlsx")
            earn.to_excel("invest.xlsx")