# -*- coding:utf-8 -*-
import pandas
import os


class OperationData(object):
    def __init__(self, file_name: str):
        """
        初始化方法,调用pandas读取数据文件
        :param file_name: 文件名
        """
        # os.path.dirname 获取当前文件路径的 目录 相当于 cd ..
        data_path = os.path.dirname(os.path.dirname(__file__)) + '/Data/'
        # 拼接文件路径
        self.path = data_path + file_name

        # 通过用户输入的文件后缀判断应该使用什么方法来读取数据
        if file_name.endswith('.csv'):
            self.table = pandas.read_csv(self.path, keep_default_na=False)
        elif file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            self.table = pandas.read_excel(self.path, keep_default_na=False)
        else:
            print("输入的文件名错误,应该包含 .csv或者.xls或者.xlsx")
            self.table = None

    def get_data_list(self):
        if self.table is not None:
            return [list(map(str, data)) for data in self.table.values.tolist()]
        else:
            print("数据文件读取失败")

    def get_data_dict(self):
        if self.table is not None:
            return [self.table.loc[i].to_dict() for i in self.table.index.values]
        else:
            print("数据文件读取失败")


if __name__ == '__main__':
    od = OperationData('user_data.xls')
    print(od.get_data_dict())
