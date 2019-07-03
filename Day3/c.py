class A:
    aa=1 ###########클래스 변수
    name = "Sam"
    def __init__(self, num = 100):
        self.bb = 2 ###########인스턴스 변수
        self._num = num
    def func1(self):
        print("func1",self.name, self._num)
    @classmethod  ##########cls인자 필수
    def func2(cls):
        print("func2", cls.name)

    @staticmethod  ########### 인자 필수 x
    def func3():
        print("func3")


#
# a1 = A()
# a2 = A()
# A.aa = 3
# print(a1.bb)
# print(A.aa)
# print(a1.aa)
# # print(A.bb) <--에러
