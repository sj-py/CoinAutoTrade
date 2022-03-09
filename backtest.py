import pyupbit
import pandas as pd
import numpy as np

# Per Hour
df = pyupbit.get_ohlcv("KRW-BTC", interval = "day", count=200, period=0.1)

test = (df['open'])*1.02 < df['high']
df['buy']=df['open']
df['sell']=(df['open'])*1.02

win = df['open']*1.02/df['open']
lose = df['close']/df['open']
df['test'] = np.where(test, win, lose)
df['ratio']=df['test'].cumprod()

# df["money"] = df["ratio"].cumprod()
# df['result']=np.where(1, df['open']+df['open']*df['ratio'], df['open']+df['open']*df['ratio'])
df.to_excel("backtest.xlsx")


