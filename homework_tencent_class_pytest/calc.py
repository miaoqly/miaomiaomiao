# 计算器功能
class Calculator:
    # 加法
    def addition(self,a,b):
        """
        为两个参数做加法运算
        :param a: 第一个参数
        :param b: 第二个参数
        :return: 两个参数的和
        """
        return a+b

    # 减法
    def subtraction(self,a,b):
        """
        为两个参数做减法运算
        :param a:第一个参数
        :param b:第二个参数
        :return:第一个参数减去第二个参数的差
        """
        return a-b

    # 乘法
    def multiplication(self,a,b):
        """
        为两个参数做乘法运算
        :param a:第一个参数
        :param b:第二个参数
        :return:两个参数的积
        """
        return a*b

    # 除法
    def division(self,a,b):
        """
        为两个参数做除法运算
        :param a:第一个参数
        :param b:第二个参数
        :return:第一个参数除以第二个参数的商
        """
        return a/b