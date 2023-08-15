import xlrd

if __name__ == '__main__':
    # 表格相应的路径，此处使用的是相对路径
    path = 'demo.xls'

    # 创建一个表格对象Excel
    Excel = xlrd.open_workbook(path)
    print(type(Excel))

    # 创建工作表Sheet1对象Sheet
    Sheet = Excel.sheet_by_name('sheet1')
    print(type(Sheet))

    # 获取总行数
    Num_H = Sheet.nrows
    print(Num_H, "行")

    # 获取总列数
    Num_L = Sheet.ncols
    print(Num_L, "列")

    n = 1
    m = 1

    # 获取第n行数据，返回列表
    # 需要传值(n-1)
    lst_H = Sheet.col_values(n - 1)
    print(lst_H)

    # 获取第m列数据，返回列表
    # 需要传值(m-1)
    lst_L = Sheet.row_values(m - 1)
    print(lst_L)

    # 获取第n行,第m列数据，返回列表
    # 需要传值(n-1,m-1)
    lst_Table = Sheet.cell(n - 1, m - 1).value
    print(lst_Table)
