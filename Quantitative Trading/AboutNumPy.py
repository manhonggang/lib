import numpy as np
np_list = np.ones(5)*3
#print(np_list)

x = np.empty((2, 3, 3))
#print(x)

stock_cnt = 200
view_days = 504

stock_day_change = np.random.standard_normal((stock_cnt, view_days))

# print(stock_day_change.shape)
# print(np.around((stock_day_change[0:1, :5]), 2))
#
# mask = stock_day_change[0:2, 0:5] > 0.5 #先找出大于0.5的数组，生成一个筛选列表。
# print(mask)
#
# tmp_test = stock_day_change[0:2, 0:5].copy()
# print(tmp_test[mask])

#一些基础的统计函数使用

stock_day_change_four = stock_day_change[:4, :4]
# print(stock_day_change_four)
#
# print('最大涨幅{}'.format(np.max(stock_day_change_four, axis=1))) #每个元素是某只股票4天内的最大涨幅，横向每一个取最大。
#
# print('日最大涨幅：{}'.format(np.max(stock_day_change_four, axis=0))) #每个元素是某日内股票的最大涨幅，纵向每一个取最大，但还不知道具体是哪一个。
#
# print('最大涨幅股票{}'.format(np.argmax(stock_day_change_four, axis=0)))

import scipy.stats as scs
import matplotlib.pyplot as plt
stock_mean = stock_day_change[0].mean()
stock_std = stock_day_change[0].std()

plt.hist(stock_day_change[0], bins=50, density=True)

fit_linspace = np.linspace(stock_day_change[0].min(), stock_day_change[0].max())

pdf = scs.norm(stock_mean, stock_std).pdf(fit_linspace)
plt.plot(fit_linspace, pdf, lw=2, c='r')
plt.show()