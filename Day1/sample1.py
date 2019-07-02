
datas = [{"name":"asdf","age":30},{"name":"asdf","age":30},{"name":"asdf","age":30},{"name":"asdf"},{"name":"asdf","age":40},{"name":"asdf","age":20}]
data30 = [d for d in datas if d.get("age",0) >= 30]

# while문 다음에 else 지정 가능
# python은 semi bool을 지원
# python은 무조건 return값이 있따
# 'return'이없어도 return이 있음