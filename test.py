import pyupbit

access = "rrMenVhjvMRyD87qWjbQcRzDm7LL8DDdYyoB45sO"          # 본인 값으로 변경
secret = "EkfxrlAYNBbxDUlwmhMCOmS4B0twHAzEVwk6nY5I"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-DOGE"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회s

print(pyupbit.get_ohlcv("KRW-BTC", count=7))
print(pyupbit.get_ohlcv("KRW-BTC", interval = "minute60", count=7))
print(pyupbit.get_ohlcv("KRW-BTC", interval = "minute60", count=2))