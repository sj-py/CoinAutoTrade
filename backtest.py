import pyupbit#chater7-13 
import numpy as np

#open, high, low, close, volume // 원화-코인 몇일
df = pyupbit.get_ohlcv("KRW-BTC", count=7)

#변동폭 * k 계산, (고가-저가) * k 값
df['range'] = (df['high'] - df['low']) * 0.5

#target매수가, range 컬럼을 한칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

#print(df)

#ror 수익률, np.where(조건문, 참일때 값, 거짓일때 값) np는 numpy 라이브러리
fee = 0.0005
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

#누적 곱 계산(cumprod)=>누적수익률
df['hpr'] = df['ror'].cumprod()

#Draw Down 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

#MDD계산
print("MDD(%): ", df['dd'].max())

#Print by Excel
df.to_excel("dd.xlsx")