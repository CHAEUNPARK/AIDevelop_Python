# class Car:
#     _speed = 0
#     name = "BMW"
#     def get_name(self):
#         return self.name
#     def get_info(self):
#         self.get_name()
#     def start(self):
#         pass
#     def set_speed(self, speed):
#         self._speed = speed
#         pass
# c1 = Car()
# c2 = c1
# c1._speed = 10
# print(c1._speed)
# print(c2._speed)
# print(c1 is c2)
# c3 = Car()
# #TODO : Car().start()    <--- 가능
#
# print(c3.get_info())

class Student:
    def __init__(self, name = "홍길동",age = 20, score_1 = 50, score_2 = 30, score_3 = 70):  ####생성자
        self._name = name
        self._age = age
        self._score_1 = score_1
        self._score_2 = score_2
        self._score_3 = score_3
        self._sum = 0
        print(name,"student객체가 생성됨")
    def doSum(self):
        self._sum = self._score_1 + self._score_2 + self._score_3
        print(self._sum)
    def showInfo(self):
        print(self._name,self._age)

s1 = Student()
s2 = Student("박채언")
s3 = Student("김창효",26)
s4 = Student(age=30)