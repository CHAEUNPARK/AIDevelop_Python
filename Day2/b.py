# Call by Value와 Call by Reference
#
# def foo(a,b):
#     a+=3
#     b[1] = 99
#     print(a, b)
#     print(id(a),id(b))
#     print("---------------------------------------")
# num = 10
# li = [1,2,3]
#
# foo(num,li)
# print(num,li)
# print(id(num),id(li))


# # 키워드 인자를 주게되면 그 다음 인자는 무조건 키워드 인자로 줘야된다.
#
# def doSum(*a):               #*a는 결과적으로 tuple이 된다.
#     # tot = 0
#     # for n in a :
#     #     tot += n
#     # return tot
#     return sum(a)
#
# print(doSum(2,3))
# print(doSum(3,2,1,5,6,7))
# print(doSum(2,3,4,5,6,7,8,9,0))


# 사용자 정의 함수 (인자) 부분 다시 한번 봐보기
def success():
    print("성ㅇㅇㅇㅇ공")
def fail():
    print("fail")
def makeImage(name, s, f):
    if name == 'a.png':
        s;
    else:
        f;

def success1():
    print("성공")

makeImage('a.png',s=success1() ,f = fail)

# side effect
