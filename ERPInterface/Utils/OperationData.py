"""
学习目标
    掌握

概念
    pandas:基于numpy的一个工具,主要用于数据分析处理
           我们使用 pandas来读取 数据文件(excel,csv) 把读取的数据当做参数传给用例

           如果报错importError,xlrd,那么请安装 xlrd 库  安装的方式是 pip install xlrd

           但是默认安装的xlrd是2.0.1以上的版本,不支持 xlsx 的格式
           可以通过 pip install xlsx==1.2.0 来解决此问题
语法


案例
"""
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
        """返回列表嵌套列表的格式"""
        if self.table is not None:
            return [list(map(str, data)) for data in self.table.values.tolist()]
        else:
            print("数据文件读取失败")

    def get_data_dict(self):
        """返回列表嵌套字典的格式"""
        if self.table is not None:
            return [self.table.loc[i].to_dict() for i in self.table.index.values]
        else:
            print("数据文件读取失败")


if __name__ == '__main__':
    od = OperationData('member_info.xls')
    print(od.get_data_list())
