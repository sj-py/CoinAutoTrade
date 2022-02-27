import pyupbit

# access = "rrMenVhjvMRyD87qWjbQcRzDm7LL8DDdYyoB45sO"          # 본인 값으로 변경
# secret = "EkfxrlAYNBbxDUlwmhMCOmS4B0twHAzEVwk6nY5I"          # 본인 값으로 변경
# upbit = pyupbit.Upbit(access, secret)

# print(upbit.get_balance("KRW-DOGE"))     # KRW-XRP 조회
# print(upbit.get_balance("KRW"))         # 보유 현금 조회s

# print(pyupbit.get_ohlcv("KRW-BTC", count=7))
# print(pyupbit.get_ohlcv("KRW-BTC", interval = "minute60", count=7))
# print(pyupbit.get_ohlcv("KRW-BTC", interval = "minute60", count=2))


# 로그인
access = "rrMenVhjvMRyD87qWjbQcRzDm7LL8DDdYyoB45sO"
secret = "EkfxrlAYNBbxDUlwmhMCOmS4B0twHAzEVwk6nY5I"
upbit = pyupbit.Upbit(access, secret)
ticker0 = input("""코인명을 입력하시오(예시 "KRW-BTC") : """)
ticker1 = '"'+ticker0+'"'
ticker2 = '"'+ticker0[0:3]+'"'
ticker3 = '"'+ticker0[4:]+'"'
print(ticker1)
print(ticker2)
print(ticker3)
print("BTC보유량 : " + str(upbit.get_balance(ticker3)))     # KRW-XRP 조회
print("KRW보유량 : " + str(int(upbit.get_balance(ticker2)))) 