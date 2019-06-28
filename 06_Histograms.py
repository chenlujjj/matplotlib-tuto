"""take away:
histogram 是分布态势图，要和 bar plot 区分开
"""

from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('ggplot')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

plt.hist(ages, bins=list(range(0, 110, 10)), edgecolor='black', log=True)

# 绘制中位数线
median_age = 29
color = 'b'

plt.axvline(median_age, color=color, linewidth=2, label='Median Age')

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.legend()
plt.tight_layout()

plt.show()
