def foo(a, b):
    if isinstance(a, int) and isinstance(b, int):
        result = a + b
    else:
        print("int형 변수만 입력해주세요.")
        result = 0
    return  result
####### isinstance( 변수, 클래스 )