# 학생관리하는 클래스 , name, age

class Student(object):
    def __init__(self, name = "박채언", age = 26):
        super().__init__()
        self._name = name
        self._age = age
    def getInfo(self):
        return "이름 : {}\n나이 : {}".format(self._name, self._age)
    # def __str__(self):
    #     return "이름 : {}\n나이 : {}".format(self._name, self._age)

    def __call__(self, *args, **kwargs):
        return self.getInfo()
    def __add__(self, other):
        if isinstance(other , Student):
            tot = self._age+ other._age
        else:
            tot = 0
            print("인자오류")
        return tot