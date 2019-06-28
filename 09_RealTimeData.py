"""绘制实时数据图：例如从api实时更新的数据、传感器的时序数据等
"""
from matplotlib import pyplot as plt

from matplotlib.animation import FuncAnimation
import pandas as pd
import random

plt.style.use('ggplot')


def animate(i):
    # TODO: 这个参数 i 是干啥的？去掉还不work了
    data = pd.read_csv('gen-data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.legend(loc='upper left')
    plt.tight_layout()


# TODO: 这个  ani = 赋值也是不可缺少的..不然也没有图形
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
