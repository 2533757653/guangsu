from openpyxl import load_workbook

def readquizfile(path):
    # 加载工作簿
    workbook = load_workbook(path)

    # 获取所有工作表名
    sheet_names = workbook.sheetnames

    # 遍历每个工作表并读取数据
    for sheet_name in sheet_names:
        # 获取当前工作表
        sheet = workbook[sheet_name]

        # 打印工作表名
        print("表名:", sheet_name)

        # 遍历当前工作表的所有行
        for row in sheet.iter_rows(values_only=True):
            # 检查行是否为空
            if all(value is None for value in row):
                continue  # 如果行为空，则跳过
            # 打印非空行数据
            print(row)

# 用法示例
readquizfile('data.xlsx')
