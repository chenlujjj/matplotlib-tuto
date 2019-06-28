## take away
"""使用 stack plot 展示几条有相互关系的折线的趋势
"""

from matplotlib import pyplot as plt

plt.style.use('ggplot')


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player1', 'player2', 'player3']

plt.stackplot(minutes, player1, player2, player3, labels=labels)

# legend 位置见： https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.legend.html
# plt.legend(loc='lower left')
plt.legend(loc=(0.08, 0.05))

plt.title('Awesome Stack Plot')
plt.tight_layout()
plt.show()








