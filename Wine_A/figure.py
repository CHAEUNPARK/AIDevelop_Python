import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# 산포도
def figure_dot(x, y):
    fg = plt.figure(figsize=(6, 6))
    plt.scatter(x, y, s=5)
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    plt.grid()
    plt.show()
    fg.savefig('plot.png')


# # Box plot
# def figure_box(x1, x2, x3, x4, x5, x6):
#     fig, ax = plt.subplots()
#     ax.boxplot([x1, x2, x3, x4, x5, x6], sym="b*")
#     plt.title('Boxplot')
#     plt.xticks([1, 2, 3, 4, 5, 6], [x1.name, x2.name, x3.name, x4.name, x5.name, x6.name])
#     plt.show()


def figure_box(x1, x2, x3, x4, x5, x6):
    fig, ax = plt.subplots()
    ax.boxplot([x1, x2, x3, x4, x5, x6], sym="b*", vert=False)
    plt.title('Boxplot')
    plt.yticks([1, 2, 3, 4, 5, 6], [x1.name, x2.name, x3.name, x4.name, x5.name, x6.name])
    plt.show()


def figure_linear(x, y):
    plt.figure()
    fp1 = np.polyfit(x, y, 1)
    fy = np.poly1d(fp1)
    plt.plot(x, fy(x), ls='dashed', lw=3, color='g')
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    plt.show()


def figure_dot_linear(x, y):
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, s=5)
    fp1 = np.polyfit(x, y, 1)
    fy = np.poly1d(fp1)
    plt.plot(x, fy(x), ls='dashed', lw=3, color='r')
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    plt.grid()
    plt.show()


def figure_heat(x):
    plt.figure()
    sns.heatmap(data=x.corr(), annot=True, fmt='.2f', linewidths=.2, cmap='Reds')
    plt.title('heatmap')
    plt.show()
