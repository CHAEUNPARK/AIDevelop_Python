#class A: 는 class A(object): <-- object가 생략되어있는것이다. 모든 클래스는 object클래스를 상속받은 것이다.
class A:
    pass

class SubA(A):
    pass
### 부모꺼 super
#직원 관리 name, 급여, age

class Employee : #(object) <<생략되어있음.
    def __init__(self, name="박채언", salary=2000000, age=26):
        #super.__init__()생략되어있음.
        self._name = name
        self._salary = salary
        self._age = age
        pass
    def showInfo(self):
        print(self._name, self._age, self._age)
# 운전사 관리, name, 급여, age

class Driver(Employee) :
    def __init__(self, name = "김창효", salary = 2000000, age = 26, carNumber ="00-1234"):
        super().__init__(name, salary, age)
        self._carNumber = carNumber
        pass
    def showInfo(self):
        print(self._name, self._age, self._age, self._carNumber)
