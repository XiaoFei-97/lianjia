import pandas as pda
from matplotlib import pylab as pyl


class Analyzer(object):
    def __init__(self, filename):
        # 读取数据
        self.data = pda.read_csv(filename)

    def convert(self):
        try:
            # 自动进行格式转化
            self.data = self.data.convert_objects(convert_numeric=True)
        except FutureWarning:
            pass
        # 查看data的类型
        print('----打印数据类型----')
        print(self.data.info())

    def tongji(self):
        """基本统计"""
        self.convert()
        print(self.data.describe())

    def sort_by_meters(self):
        """按meters排序"""
        self.data = self.data.sort_values(by=['meters'])

    def line_chart(self):
        """显示折线图"""
        self.sort_by_meters()

        # 将行与列进行转置
        self.data = self.data.T

        pyl.subplot(2, 1, 1)
        pyl.title('meters/price')
        pyl.xlabel('meters')
        pyl.ylabel('price')
        x1 = self.data.values[2]
        y1 = self.data.values[6]
        pyl.plot(x1, y1)

        pyl.subplot(2, 1, 2)
        pyl.title('meters/num')
        pyl.xlabel('meters')
        pyl.ylabel('num')
        x2 = self.data.values[2]
        y2 = self.data.values[7]
        pyl.plot(x2, y2)
        pyl.show()

    def histogram(self):
        """显示直方图"""
        # self.sort_by_meters()
        pyl.subplot(2, 1, 1)
        x1 = list(self.data.values[2])[:-1]
        pyl.hist(x1)

        pyl.subplot(2, 1, 2)
        x2 = list(self.data.values[6])[:-1]
        pyl.hist(x2)

        pyl.show()


if __name__ == "__main__":
    analyzer = Analyzer(filename='zufang.csv')
    analyzer.tongji()
    analyzer.line_chart()
    analyzer.histogram()



