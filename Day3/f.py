from fmodule import A, process

class subA(A):
    def func1(self):
        print("변경된 메소드")

def doInit():
    print("doInit")
    a = A()
    process(a)
    a1 = subA()
    process(a1)

if __name__ == "__main__":
    doInit()
