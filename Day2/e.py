class Data:
    def __init__(self):
        pass
    def f1(self):
        print("f1")
    def _f2(self):
        print("f2")
    def __f3(self):
        print("f3")

d1 = Data()
d1.f1()
d1._f2()
# d1.__f3()

# if __name__ == "__main__" :
#     print("anldskfj")

class D :
    def __init__(self):
        self._price = 1000

    def __setPrice(self, price):
        if price > 0 :
            self._price = price
        else :
            print("허용되지 않은 금액입니다.")

    def __getPrice(self):
        return self._price

    price = property(__getPrice, __setPrice)

d.price = 7000
d.price