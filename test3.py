import pyupbit
import pandas as pd
import numpy as np
import datetime
import winsound as sd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import sys
# access = "rrMenVhjvMRyD87qWjbQcRzDm7LL8DDdYyoB45sO"
# secret = "EkfxrlAYNBbxDUlwmhMCOmS4B0twHAzEVwk6nY5I"
# upbit = pyupbit.Upbit(access, secret)
# a = 100000
# b = int(upbit.get_balance("KRW"))
# b += int(pyupbit.get_current_price("KRW-BTC") * upbit.get_balance("KRW-BTC"))
# c = round(((b - a) / a) * 100,3)
# print(c)
# print(str((upbit.get_balance-100000/100000)*100))
f = open("수.txt", "a",encoding="UTF8")
f.write("거래 시간 : \n")
f.close()