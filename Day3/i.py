

print(-3.4)
print(abs(-3.4))

datas = [2,3,-4,5,6,-7,8,9]

newDatas = list(map(abs,datas))

print(newDatas)

langTitle = ["asdf","zxcv","qwer"]
scoreList = [20,30,40]

totalList = zip(langTitle,scoreList)
print(totalList)
for lang, score in totalList:
    print(lang, score)

totalList_1 = list(zip(langTitle, scoreList))
print(totalList_1)

