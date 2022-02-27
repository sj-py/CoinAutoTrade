import time
import pyupbit
import datetime

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time
while True:
    nowTime = datetime.datetime.now()
    start_time = get_start_time("KRW-BTC")
    end_time = start_time + datetime.timedelta(days=1)
    after_six_hours = start_time - datetime.timedelta(hours=6)

    
    print("start time : " + str(start_time))
    print("end time : " + str(end_time))
    print("after_six_hours : " + str(after_six_hours))
    print("current time : " + str(nowTime))
    print("==========================================")

    time.sleep(10)
