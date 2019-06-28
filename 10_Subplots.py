"""subplots 相比于之前使用plt绘图的方式更加 OO（面向对象）

figure: a container of plots
axis: just think it as a plot

这里的例子绘制了两张figure，其中一张包含两个axis
"""

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')

data = pd.read_csv('salary.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# subplots(), 参数为空表示一行一列的subplot
fig1, ax1 = plt.subplots()
fig2, (ax2, ax3) = plt.subplots(ncols=1, nrows=2, sharex=True)

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python', color='y')
ax3.plot(ages, js_salaries, label='JavaScript', color='c')

ax1.legend()
ax2.legend()
ax3.legend()

# 注意方法名的变化： plt.title  -> ax.set_title
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.set_title('Median Salary (USD) by Age')
ax2.set_ylabel('Median Salary (USD)')
ax3.set_xlabel('Ages')
ax3.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

fig1.savefig('fig1.png')
fig2.savefig('fig2.png')
