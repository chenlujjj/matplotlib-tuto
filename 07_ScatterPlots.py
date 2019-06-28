"""
散点图：用于查看两个变量是否有相关性
"""

from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn')

# part1: simple example
"""
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]


colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

# 可以设置点的大小，颜色，形状等属性
plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', marker=r'$\clubsuit$', 
            edgecolors='k', linewidths=1, alpha=0.5, label='Luck')

# 每个点的大小单独设置
# 每个点的颜色可以单独设置，并且在旁边展示颜色渐变条
# colormap 选项： https://matplotlib.org/3.1.0/gallery/color/colormap_reference.html
cbar = plt.colorbar()
cbar.set_label('Satisfaction')
"""


# part2: real world data
# 探寻视频观看数量和点赞数的关系
data = pd.read_csv('youtube.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

# 对数坐标和坐标轴范围
plt.xscale('log')
plt.yscale('log')
plt.xlim(10e4, 10e7)
plt.ylim(10e2, 10e6)

plt.scatter(view_count, likes, c=ratio, cmap='rainbow',
            edgecolors='k', linewidths=1, alpha=0.5)

cbar = plt.colorbar()
cbar.set_label('Like Ratio')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
