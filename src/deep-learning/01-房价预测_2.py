import numpy as np
from lab_utils_uni import plt_stationary
from lab_utils_uni import plt_update_onclick
from lab_utils_uni import soup_bowl
import matplotlib.pyplot as plt


def compute_cost(x, y, w, b):
    """
    Computes the cost function for linear regression.

    Args:
      x (ndarray (m,)): Data, m examples
      y (ndarray (m,)): target values
      w,b (scalar)    : model parameters

    Returns
        total_cost (float): The cost of using w,b as the parameters for linear regression
               to fit the data points in x and y
    """
    # number of training examples
    m = x.shape[0]

    cost_sum = 0
    for i in range(m):
        f_wb = w * x[i] + b
        cost = (f_wb - y[i]) ** 2
        cost_sum = cost_sum + cost
    total_cost = (1 / (2 * m)) * cost_sum

    return total_cost


def compute_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    Args:
      x (ndarray (m,)): Data, m examples
      w,b (scalar)    : model parameters
    Returns
      y (ndarray (m,)): target values
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b

    print(f_wb)
    return f_wb


if __name__ == '__main__':
    # 训练数据集合
    x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2])
    y_train = np.array([250, 300, 480, 430, 630, 730, ])

    plt.close('all')
    fig, ax, dyn_items = plt_stationary(x_train, y_train)
    updater = plt_update_onclick(fig, ax, x_train, y_train, dyn_items)

    soup_bowl()