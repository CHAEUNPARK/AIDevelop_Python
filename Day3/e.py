## is 관계 (상속)
from emodule import A, SubA, Employee, Driver
def doInit():
    a= A()
    a1 = SubA()
    print("a", isinstance(a1,A))
    print("a1", isinstance(a1, SubA))
    print("object", isinstance(a1,object))
    pass
if __name__ == "__main__":
    doInit()
    e = Employee()
    d = Driver()