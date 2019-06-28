"""时序数据
学习 matplotlib.dates 中日期格式化的用法
学习 pandas 对日期数据的处理
"""
from datetime import datetime, timedelta

from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd

plt.style.use('seaborn')

# datetimes = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]

# y = [0, 1, 3, 4, 6, 5, 7]

data = pd.read_csv('price.csv')

data['Date'] = pd.to_datetime(data['Date'])
# 将数据按日期排序，否则会出现“回折线”
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']


plt.plot_date(price_date, price_close, linestyle='solid')

# get current figure
# TODO: figure 和 plot 的关系是啥？？
# 让横坐标的时间标识 自动format，使得它们不会拥挤在一起
plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.tight_layout()
plt.show()
