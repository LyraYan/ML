import matplotlib.pyplot as plt
import numpy as np


def Figure_base() -> None:
    """
    brief: plot a base figure

    annotation:
        x_points = np.array([1,3,5,7,9])
                        x:   | | | | |
                             | | | | |
                        y:   V V V V V
        y_points = np.array([2,5,6,8,10])
        coordinate:(1,2)、(3,5)、(5,6)、···

    :return: None
    """
    x_points = np.array([1, 3, 5, 7, 9])
    y_points = np.array([2, 6, 6, 8, 10])
    plt.title('Figure_base')
    plt.plot(x_points, y_points, 'r--o')  # 一条杠是实线，两条是虚线
    plt.show()


def Figure_subplots() -> None:
    """
    brief: plot several subplots in a figure

    :return: None
    """
    x_points_1 = x_points_2 = np.random.randint(0, 10, [1, 10])
    y_points_1 = y_points_2 = np.random.randint(0, 10, [1, 10])
    # x_points_2 = np.random.randint(0, 10, [1, 10])
    # y_points_2 = np.random.randint(0, 10, [1, 10])

    plt.subplot(1, 2, 1)
    """
            plt.subplot(rows, cols, index):
            rows:行数            例: plt.subplot(2,2,3) --> 0   1 
            cols:列数                分成2×2区域，绘制3号位    2   3*
            index:子图位置
    """
    plt.plot(x_points_1, y_points_1, 'r+')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('subplot_1')

    plt.subplot(1, 2, 2)
    plt.plot(x_points_2, y_points_2, 'lime', marker='.')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('subplot_2')

    plt.show()


Figure_base()
Figure_subplots()

filePath = 'W:\pyCharmProject\KMeans\KMeans\Mission2\dif.xlsx'.strip('.xlsx')

print(filePath)

