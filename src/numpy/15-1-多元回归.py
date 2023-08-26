import pandas
from sklearn import linear_model

if __name__ == '__main__':
    # Pandas 模块允许我们读取 csv 文件并返回一个 DataFrame 对象。
    df = pandas.read_csv("cars.csv")

    # 然后列出独立值，并将这个变量命名为 X。
    # 将相关值放入名为 y 的变量中。
    X = df[['Weight', 'Volume']]
    y = df['CO2']

    # 在 sklearn 模块中，我们将使用 LinearRegression() 方法创建一个线性回归对象。
    # 该对象有一个名为 fit() 的方法，该方法将独立值和从属值作为参数，并用描述这种关系的数据填充回归对象：
    regr = linear_model.LinearRegression()
    regr.fit(X, y)

    # 现在，我们有了一个回归对象，可以根据汽车的重量和排量预测 CO2 值：
    # 预测重量为 2300kg、排量为 1300ccm 的汽车的二氧化碳排放量：
    predictedCO2 = regr.predict([[2300, 1300]])

    print(predictedCO2)
