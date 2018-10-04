import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt
import matplotlib

stock_cnt = 200
view_days = 504
keep_days = 50

stock_day_change = np.random.standard_normal((stock_cnt, view_days))

np.save('./stock_day_change', stock_day_change)

stock_day_change_test = stock_day_change[:stock_cnt, 0:view_days-keep_days]

print(np.sort(np.sum(stock_day_change_test, axis=1))[:3]) #由负数到正数，前面三个是最小的，因此是跌幅最大的。

stock_lower_array = np.argsort(np.sum(stock_day_change_test, axis=1))[0:3]

print(stock_lower_array)

def show_buy_lower(stock_ind):
    """

    :param stock_ind: 股票序号
    :return:
    """
    _, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 5)) # 返回两个值，只要第一个
    axs[0].plot(np.arange(0, view_days-keep_days), stock_day_change_test[stock_ind].cumsum()) #第一张图，第一天到第454天的涨跌，和盈利累加
    cs_buy = stock_day_change[stock_ind][view_days - keep_days:view_days].cumsum() #某一只股票，从454天到最后一天的累计盈利。
    axs[1].plot(np.arange(view_days - keep_days, view_days), cs_buy) #第二张图，回测区域的盈利情况图表
    return cs_buy[-1] #返回最后的测试结果，盈利结果

profit = 0

for stock_ind in stock_lower_array:
    sgl_profit = show_buy_lower(stock_ind)
    profit += show_buy_lower(stock_ind)
    #print(sgl_profit)

print('买入第{}只股票，从第454个交易日开始持有盈亏{:.2f}%'.format(stock_lower_array, profit))
#plt.show()