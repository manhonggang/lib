import scipy.optimize as sco
from scipy.interpolate import interp1d
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('price.csv')
data_close = data['closePrice']

x = np.arange(0, data_close.shape[0])
y = data_close.values

linear_interp = interp1d(x, y) #做x, y的线性插值,接受一个[j, k]作为输入坐标，

plt.plot(linear_interp(x)) #画出线性插值的图
global_min_pos = sco.fminbound(linear_interp, 1, 329) #找出全局最低点
plt.plot(global_min_pos, linear_interp(global_min_pos), 'r^') #画出该点，并用上箭头表示
last_position = None
for find_min_pos in np.arange(50, len(x), 50): #注意 arrange 返回的也是ndarray
    local_min_pos = sco.fmin_bfgs(linear_interp, find_min_pos, disp=0) #find_min_pos 是个数列范围ndarray,找出最低点, 返回要一个数列[a, b]
    draw_position = (local_min_pos, linear_interp(local_min_pos))
    print(local_min_pos)
    print(linear_interp(local_min_pos))
    if last_position is not None:
        plt.plot([last_position[0][0], draw_position[0][0]], [last_position[1][0], draw_position[1][0]], 'o-')
    last_position = draw_position

plt.show()

