# # 수강생 정보가 있는데 그 정보를 정렬해서 출력하라.
# students = [{"name":"홍길동1", "age":30, "score": 50},
#             {"name":"홍길동3", "age":20, "score": 30},
#             {"name":"홍길동2", "age":40, "score": 60},
#             {"name":"홍길동5", "age":15, "score": 10},
#             {"name":"홍길동4", "age":23, "score": 20},
#             {"name":"홍길동6", "age":65, "score": 70},
#             {"name":"홍길동7", "age":54, "score": 80},
#             {"name":"홍길동8", "age":43, "score": 80},
#             {"name":"홍길동9", "age":59, "score": 20}]
# print(students)
#
# students.sort(key=lambda data: data.get("age"), reverse=True)

try:
    a = 3/1
except (ZeroDivisionError, IndexError):
    print("오류")
else:
    print("오류안생김")
finally:
    print("ggggggggggggggggggggggggg")
# map(), filter()
