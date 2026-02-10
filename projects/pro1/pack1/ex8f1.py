####function 여러개의 수행문을 하나의 이름으로 묶은 실행 단위
####함수 고유의 실행 공간을 갖음
####자원의 재활용

#내장함수 일부 체험
print(sum([1,2,3]))         ###list, set, tuple 올 수 있음
print(bin(8))               ###2진수
print(eval('4+5'))
print(round(1.2), round(1.6))

import math
print(math.ceil(1.2), math.floor(1.2))      ##ceil은 큰수, floor 작은 수

b_list = [True, 1, False]
print(all(b_list))                             ###하나만 Fasle여도 False 
print(any(b_list))                             ###하나만 True여도 True

data1 = [10, 20, 30]
data2 = ['a', 'b']
for i in zip(data1, data2) :
    print(i)                                    ###반환 타입은 tuple

###....