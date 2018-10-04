import statsmodels.api as sm
from statsmodels import regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# from sklearn import metrics
import itertools


data = pd.read_csv('price.csv')

df2 = data['closePrice']
y = df2.values

x = np.arange(0, data.shape[0])

def regress_y(y):

    y = y
    x = np.arange(0, len(y))
    x = sm.add_constant(x)
    model = regression.linear_model.OLS(y, x).fit() #线性拟合
    return model

model = regress_y(y)

b = model.params[0]
k = model.params[1]

y_fit = k * x + b
plt.plot(x, y)
plt.plot(x, y_fit, 'r')
# print(model.summary())
# plt.show()


# MAE = metrics.mean_absolute_error(y, y_fit)
# MSE = metrics.mean_squared_error(y, y_fit)
# RMSE = np.sqrt(metrics.mean_squared_error(y, y_fit))
#
# print(MAE, MSE, RMSE)


_, axs = plt.subplots(nrows=3, ncols=3, figsize=(15, 15)) # 生成九个图表
axs_list = list(itertools.chain.from_iterable(axs))
poly = np.arange(1, 10, 1)
for p_cnt, ax in zip(poly, axs_list):
    p = np.polynomial.Chebyshev.fit(x, y, p_cnt) #从1到9拟合
    y_fit = p(x)
    mse = sum(np.square(y - y_fit)) / len(y) #计算MSE
    ax.set_title('{} poly MSE={}'.format(p_cnt, mse)) # 给与每个表格名称，显示其MSE。
    ax.plot(x, y, '', x, y_fit, 'r.')
plt.show()