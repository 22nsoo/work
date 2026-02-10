var1 = "안녕 파이썬"
print(var1)


var1 = 5.6
var2 = 6

print(var1,var2)
print(type(var1))

var2 = var1

print(var2, var1)

var3 = 7
print(var1, var2, var3)
print(id(var1), id(var2))     ##주소는 id 함수로 확인한다 같은 값을 가리키면 주소가 같다.

a = 5
b = a
c = 5

print(a, b, c)
print(id(a), id(b), id(c))
print(a is b)
print(a is b, b == c)       ##is : 주소 비교 연산자, == : 값 비교 연산자

aa = [5]
bb = [5]

print(aa, bb)
print(id(aa), id(bb))
print(aa == bb, aa is bb)       ##list의 값은 같더라도 주소는 다르다. 주로 ==를 써라

print("----")

import keyword          ##키워드 목록 확인용 모듈 읽기 자동으로 import 됨
a = input("입력 : ")
print("예약어 목록: ", keyword.kwlist)
print(a)

print(type(a))
kbs = 9.1
print(isinstance(a, str))
print(isinstance(kbs, float))
kk = 4j
print(kk, type(kk))
print((1, ), type((1, )))       #tuple
print([1], type([1]))           #list 가장 많이 사용
print({1},type({1}))            #set
print({'k':1},type({'k':1}))    #dict 중요함. 웹 상에 넘어다니는게 json인데 dict로 받는게 편하다.