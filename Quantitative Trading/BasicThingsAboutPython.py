price_str = '30.14, 29.58, 26.36, 32.56, 32.82'
type(price_str)
#print(type(price_str))
# print('旧的price_str id={}'.format(id(price_str))) ## format 用来填充字符串
price_str = price_str.replace(' ', '')
# print('新的price_str id={}'.format(id(price_str)))
# print(price_str)

price_array = price_str.split(',')

print(price_array)

## 数组推导式

date_array = []
date_base = 20170118
for _ in range(0, len(price_array)):  ## 本来是xrange后来改成了range，python3里面都改成了range。
    date_array.append(str(date_base))
    date_base += 1

# print(date_array)

stock_tuple_list = [(date, price) for date, price in zip(date_array, price_array)]

# print(stock_tuple_list)
# print('20170119日价格:{}'.format(stock_tuple_list[1][1]))

## 字典推导式

stock_dict = {date: price for date, price in zip(date_array, price_array)}
# print(stock_dict)

minprice = min(zip(stock_dict.values(), stock_dict.keys())) ## 先使用zip把字典的keys和values翻转过来，再用min取出值最小的那组数据
# print(minprice)

## 有序字典

from collections import OrderedDict

stock_dict = OrderedDict((date, price)for date,price in zip(date_array, price_array))

# print(stock_dict)

## 找第二大价格

def find_second_max(dict_array):
    stock_prices_sorted = sorted(zip(dict_array.values(), dict_array.keys()))
    return stock_prices_sorted[-2]
if callable(find_second_max):
    print(find_second_max(stock_dict))

## Lambda函数，简洁，不用命名。

find_second_max_lambda = lambda dict_array:\
    sorted(zip(dict_array.values(), dict_array.keys()))[-2]  # 此处“\”起到换行作用
# print('Lambda方法' + str(find_second_max_lambda(stock_dict)))

## 高阶函数
## 切片/两两比较
price_float_array = [float(price_str) for price_str in stock_dict.values()]

pp_array = [(price1, price2) for price1, price2 in zip(price_float_array[:-1], price_float_array[1:])]

#print(pp_array)

from functools import reduce

change_array = list(map(lambda pp: reduce(lambda a, b: round((b-a)/a, 3), pp), pp_array))

change_array.insert(0, 0)
#print(change_array)

## 使用namedtuple 重新构建数据结构

from collections import namedtuple

stock_namedtuple = namedtuple('stock', ('date', 'price', 'change'))
stock_dict = OrderedDict((date, stock_namedtuple(date, price, change)) for date, price, change in zip(date_array, price_array, change_array))

print(stock_dict.values())
for x in stock_dict.values():
    print(x.change)

up_days = list(filter(lambda day: day.change > 0, stock_dict.values()))
#print(up_days)

# 筛选上涨和下跌

def filter_stock(stock_array_dict, want_up=True, want_calc_sum=False):
    if not isinstance(stock_array_dict, OrderedDict):
        raise TypeError('stock_array_dict must be OrderdDict')

    filter_func = (lambda day: day.change > 0) if want_up else (lambda day: day.change < 0) # want_up 为真时输出 day.change>0的值，否则输出day.change<0的值。

    want_days = list(filter(filter_func, stock_array_dict.values()))

    if not want_calc_sum:
        return want_days
    change_sum = 0.0
    for day in want_days:
        change_sum += day.change
    return change_sum

print('所有上涨的交易日：{}'.format(filter_stock(stock_dict)))