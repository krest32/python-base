import numpy as np
import matplotlib.pyplot as plt


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
    plt.style.use('deeplearning.mplstyle')
    # 训练数据集合
    x_train = np.array([1.0, 2.0])
    y_train = np.array([300.0, 500.0])


    w = 100
    b = 100

    tmp_f_wb = compute_model_output(x_train, w, b, )

    # Plot our model prediction（计算出预测的值） 画出直线
    plt.plot(x_train, tmp_f_wb, c='b', label='Our Prediction')

    # Plot the data points
    plt.scatter(x_train, y_train, marker='x', c='r', label='Actual Values')

    # Set the title
    plt.title("Housing Prices")
    # Set the y-axis label
    plt.ylabel('Price (in 1000s of dollars)')
    # Set the x-axis label
    plt.xlabel('Size (1000 sqft)')
    plt.legend()
    plt.show()
