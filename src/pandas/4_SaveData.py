import numpy as np
import pandas as pd

if __name__ == '__main__':
    df1 = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
                        "gender": ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
                        "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y', ],
                        "m-point": [10, 12, 20, 40, 40, 40, 30, 20]})

    df1.to_excel('excel_to_python.xlsx', sheet_name='bluewhale_cc')
    df1.to_csv('excel_to_python.csv')
