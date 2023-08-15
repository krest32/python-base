import xlwt

if __name__ == '__main__':
    workbook = xlwt.Workbook(encoding='utf-8')

    # 添加表单
    sheet1 = workbook.add_sheet("sheet1")
    # 前面两个代表在表格中的位置
    sheet1.write(0, 0, "你好")
    sheet1.write(0, 1, "我好")
    sheet1.write(0, 2, "大家好")
    sheet1.write(1, 1, "嘿嘿嘿")
    # 输出到文件当中
    workbook.save(str("demo.xls"))
