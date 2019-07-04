## BeautifulSoup4
#웹 크롤링 할 때 많이 씀
#https://twpower.github.io/84-how-to-use-beautiful-soup

# css selector 검색 #asdf  .asdf
# select와 find의 차이

import requests, bs4
resp = requests.get('https://www.naver.com')
print(resp.raise_for_status())

if (resp.status_code == requests.codes.ok):
    html = resp.text
    # print(html)

bs = bs4.BeautifulSoup(html,'html.parser')
tags = bs.select('a.ah_a')
for t in tags:
    print(t.getText())
    # print(t.text)



#darksky api

## flask가 django보다 light함


## 김재웅 010-3792-6917
## gsarang10@gmail.com