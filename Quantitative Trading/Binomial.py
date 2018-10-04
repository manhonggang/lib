import numpy as np
import matplotlib.pyplot as plt

gamblers = 100

def casino(win_rate, win_once=1, loss_once=1, commission=0.01):
    """

    :param win_rate:
    :param win_once:
    :param loss_once:
    :param commission:手续费
    :return:
    """
    my_money = 1000000
    play_cnt = 10000000
    commission = commission

    for _ in np.arange(0, play_cnt):
        w = np.random.binomial(1, win_rate)
        if w:
            my_money += win_once
        else:
            my_money -= loss_once

        my_money -= commission
        if my_money <= 0:
            break

    return my_money



