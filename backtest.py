import pyupbit
import pandas as pd
import numpy as np

# Per Hour
df = pyupbit.get_ohlcv("KRW-BTC", interval = "day", count=300, period=0.1)

df2 = pd.DataFrame()

df2['open'] = df['open']
df2['high'] = df['high']
df2['close'] = df['close']

df2_test = df2['high']/df['open'] > 1.002

df2['result'] = np.where(df2_test,df2['high']/df['open'],df2['close']/df['open'])



df2.to_excel("backtest.xlsx")


