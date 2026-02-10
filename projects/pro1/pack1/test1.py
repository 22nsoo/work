# 1번
li = [1, 2, 2, 2, 3, 4, 5, 5, 5, 2, 2]
im = set(li)
li = list(im)
print(li)

# 2번
for i in {1, 2, 3, 4, 5, 5, 5, 5}:
    print(i, end = ' ')

# 수행 결과 : 1 2 3 4 5
# 이유 : set 타입이기 때문에 중복 항 제거 되어 1,2,3,4,5 하나씩만 남은 후 for문을 이용하여  end = ' '로 일렬로 출력한다.

# 3번
count = 0
sum = 0
for i in range(1, 101):
    if (i % 3 == 0 or i %4 == 0) and i % 7 != 0:
        count += 1
        sum += i

print('건수 : ', count)
print('배수의 총합 : ', sum)

# #4번
# 1. while문
# 2. for문
# 3. 재귀함수
i = 3
while i < 10 :
    j = 1
    while j < 10 :
        print(f'{i}*{j}={i*j}', end = ' ')
        j += 1
    print()
    i += 2

lambda x,y: x + y * 5


class Bicycle :
    name = '이름'
    wheel = '바퀴수'
    price = '가격'
    
    def __init__(self, name, wheel, price):
        self.name = name
        self.wheel = wheel
        self.price = price
        self.chong = self.wheel*self.price

    def display(self):
        print(f'{self.name}님 자전거 바퀴 가격 총액은 {self.chong}원 입니다.')

gildong = Bicycle('길동', 2, 50000)
gildong.display()



# i = 0
# while True:
#     if i % 10 != 3:
#         i += 1
#         continue       
#     if i > 100: break
#     print(i, end=' ')
#     i += 1


*v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(v1, type(v1))
print(v2)
print(v3)
print({1, 2, 3, 4, 5, 1, 2, 3, 4, 5})


m = 1
n = 2
lambda m,n : m+n*5


for i in {1, 2, 3, 4, 5, 5, 5, 5}:
    print(i, end = ' ')


print()
try :
    aa = int(input())
    bb = 10 / aa

except ZeroDivisionError as err:
    print('0으로 나눌 수 없습니다.', err)


i = 10
j = 0
while i >= 1:
    print(' '*j + '*'*i)
    i -= 1
    j += 1

year = int(input('연도 입력:'))
if year % 400 == 0:
    print(f'{year}년은 윤년')
elif year % 4 == 0 and year % 100 != 0:
    print(f'{year}년은 윤년')
else : print(f'{year}년은 평년')

i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue       
    if i > 100: break
    print(i, end=' ')
    i += 1

print()


i = 3
while i < 10 :
    j = 1
    while j < 10 :
        print(f'{i}*{j}={i*j}', end = ' ')
        j += 1
    print()
    i += 2

*v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(v1)
print(v2)
print(v3)
print(list(range(1, 6, 2)))

i = 10
j = 0
while i >= 1:
    print(' '*j + '*'*i)
    i -= 1
    j += 1

i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue       
    if i > 100: break
    print(i, end=' ')
    i += 1



class Bicycle :
    name = '이름'
    wheel = '바퀴수'
    price = '가격'
    
    def __init__(self, name, wheel, price):
        self.name = name
        self.wheel = wheel
        self.price = price
        self.chong = self.wheel*self.price

    def display(self):
        print(f'{self.name}님 자전거 바퀴 가격 총액은 {self.chong}원 입니다.')

gildong = Bicycle('길동', 2, 50000)
gildong.display()