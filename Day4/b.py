# 정확하게 따지면 쓰레드 함수를 사용하는 것이 아닌 쓰레드 객체를 생성하는 것.
# 쓰레드는 뭔가 a라는 작업과 b라는 작업을 동시에 할때 또는 한가지 작업이 너무 오래 걸릴 때 사용
# 병행작업을 하거나 오랜시간 작업을 동작해야 하는 경우
# java, python 멀티쓰레드 지원

import threading, time

def sum(low, high):
    total = 0
    for i in range(low, high):
        time.sleep(1)
        print("sum : " + str(i))
        total += i
    print("sumthread", total)


def count(low, high):
    total = 0
    for i in range(low, high):
        time.sleep(0.7)
        print("count : ", i)
        total += i
    print("countthread", total)

t = threading.Thread(target=sum, args=(1, 10))
t.start()
t1 = threading.Thread(target=count, args=(1,10))
t1.start()
print("-----------------------------------------------")

class CountThread(threading.Thread):
    def __init__(self):
        pass
    def __str__(self):
        return "count"

    def run(self):
        print("count")

##start를 오버라이딩 하면 안되고 run을 오버라이딩 해야함
8