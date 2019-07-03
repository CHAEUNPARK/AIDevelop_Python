from gmodule import Student

def doInit():
    s = Student()
    # print(s.getInfo())
    # print(str(s))
    # print(s)
    print(s())
    s1 = Student()
    print(s+s1)
##print는 기본적으로 클래스의 __str__을 반환하도록 되어있다.

#__call__?
if __name__ == "__main__":
    doInit()