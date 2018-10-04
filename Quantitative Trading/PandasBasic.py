import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

stock_day_change = np.load('./stock_day_change.npy')


stock_symbols = ['股票' + str(x) for x in range(stock_day_change.shape[0])]
days = pd.date_range('2017-1-1', periods=stock_day_change.shape[1], freq='1d') #间隔为1天

df = pd.DataFrame(stock_day_change, index=stock_symbols, columns=days)
df = df.T #转置

df_20 = df.resample('20D').mean() #21天平均值

print(df_20.head())

# Seriers构建及方法

df_stock0 = df['股票0']
print(type(df_stock0))

df_stock0.cumsum().plot() #比较简单的实现了前面的图表需求

#重新采样数据

df_stock0_5 = df_stock0.cumsum().resample('5D').ohlc()
df_stock0_20 = df_stock0.cumsum().resample('21D').ohlc()

print(df_stock0_5.head())

