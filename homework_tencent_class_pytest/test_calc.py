import pytest
import yaml

from homework_tencent_class_pytest.calc import Calculator

# 创建模块级别的setup方法
def setup_module():
    print("计算器启动")

# 创建模块界别的teardown方法
def teardown_module():
    print("计算器关闭")

# yaml文件读取
with open(r'E:\miaomiaomiao\homework_tencent_class_pytest\datas\test_addition.yaml') as f:
    # 读取后拿到所有加法add数据datas_add
    datas_addition = yaml.safe_load(f)['addition']
    # 取出加法的datas的值
    addition_datas_addition = datas_addition['datas']
    # 取出加法的myid的值
    myid_datas_addition = datas_addition['myid']

with open(r'E:\miaomiaomiao\homework_tencent_class_pytest\datas\test_division.yaml') as j:
    # 读取后拿到所有除法div数据datas_div
    datas_division = yaml.safe_load(j)['division']
    # 取出除法的datas的值
    division_datas_division = datas_division['datas']
    # 取出除法的myid的值
    myid_datas_division = datas_division['myid']

# 创建计算器加法类
class TestCalcAddition:
    # 定义一个类级别的setup方法
    def setup_class(self):
        print("加法计算开始")
        # 实例化计算器
        self.calc = Calculator()

    # 定义一个类级别的teardown方法
    def teardown_class(self):
        print("加法计算结束")

    # 定义一个方法级别的setup方法
    def setup(self):
        print("计算开始")

    # 定义一个方法级别的teardown方法
    def teardown(self):
        print("计算结束")
    @pytest.mark.parametrize('a,b,expect',addition_datas_addition,ids=myid_datas_addition)
    # 加法方法
    def test_add(self,a,b,expect):
        # 调用加法方法，结果放在result中
        result = self.calc.addition(a,b)
        # 添加判断，如果是浮点数，用round方法保留2位小数
        if isinstance(result,float):
            result = round(result,2)
        print(f"计算结果是{result},expect是{expect}")
        # 得到的结果要进行断言
        assert result == expect


# 创建计算器除法类
class TestCalcDivision:
    # 定义一个类级别的setup方法
    def setup_class(self):
        print("除法计算开始")
        # 实例化计算器
        self.calc = Calculator()

    # 定义一个类级别的teardown方法
    def teardown_class(self):
        print("除法计算结束")

    # 定义一个方法级别的setup方法
    def setup(self):
        print("计算开始")

    # 定义一个方法级别的teardown方法
    def teardown(self):
        print("计算结束")
    @pytest.mark.parametrize('a,b,expect',division_datas_division,ids=myid_datas_division)
    # 除法方法
    def test_div(self,a,b,expect):
        # 调用除法方法，结果放在result中
        result = self.calc.division(a,b)
        # 添加判断，如果是浮点数，用round方法保留2位小数
        if isinstance(result,float):
            result = round(result,2)
        print(f"计算结果是{result},expect是{expect}")
        # 得到的结果要进行断言
        assert result == expect
