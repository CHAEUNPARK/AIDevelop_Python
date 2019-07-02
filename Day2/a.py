import random
# 로또 번호 발생기
def lotto():
    lott = list(range(1,46))
    random.shuffle(lott)
    return lott[:6]

lo = lotto()
print(lo)

# Call by Value와 Call by Reference
