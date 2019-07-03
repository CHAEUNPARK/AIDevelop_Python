from c import A

if __name__ == "__main__":
    print("main")
    s1 = A()
    s2 = A(200)
    s1.func1()
    s2.func1()


#### 변수는 인스턴스를 생성한 만큼 만들어지지만 메소드는 클래스에 있는 것을 계속해서 재사용함.