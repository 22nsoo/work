# ##문제 1 : 2~9 구구단 출력(단은 행 단위 출력)


# for i in range(2,10) :
#     for j in range(1,10):
#         print(f'{i} * {j} = ', i*j,end = ', ')
#     print('\n')





# ##########################################################
# ##문제 2 : 주사위를 두번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
# num1 = int(input("input 1st number : "))
# num2 = int(input("input 2nd number : "))

# if (num1 + num2) % 4 == 0 :
#     print(f'첫번째는 {num1}, 두번째는 {num2}')
# else : 
#     print('4의 배수가 아님')





# for i in range(1,7):
#     for j in range(1,7):
#         if (i + j) % 4 == 0:
#             print(f'첫번째 숫자 {i}, 두번째 숫자 {j} 4의 배수')



#문제 3 : 1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
sum = 0
for i in range(1, 101) :
    if i % 3 == 0 and i % 2 != 0 :
        print(f'수는 {i}')
        sum += i

print(f'합계는 {sum}')


##문제 4 : 2 ~ 5 까지의 구구단 출력
for i in range(2,6) :
    for j in range(1,10):
        print(f'{i} * {j} = ', i*j)



##문제 5 : 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력
sum = 0
for i in range(1, 101) :
    if i % 2 == 0 :
        sum += i
    else :
        sum -= i
print(f'결과는 {sum}')

i = 1
hap = 0
while i <= 100 :
    if i % 2 == 0 :
        hap += i
    else :
        hap -= i
    i += 1

print(f'최종 결과는 {hap}')


##문제 6 : -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
i = 1
sum = 0
while (2*i - 1) <= 99 :
    if i % 2 == 1 :
        sum = sum - (2*i -1)
    else : 
        sum = sum + (2*i -1)
    i += 1
print(f'합계는 {sum}')

##문제 7 : 1 ~ 100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력
for i in range(1, 100) :
    num1 = i % 10
    num2 = i // 10
    if num1 + num2 >= 10 :
        print(f'각 자릿수의 합이 10 이상인 수는 {i}')



##문제 8 : 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력
i = 1
sum = 0
while 1 :
    sum += i
    if sum >= 1000 :
        break
    i += 1

print(f'합계는 {sum}, 그때의 수는 {i}')


##문제 9 : 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동
for i in range(2, 10):
    for j in range(1, 10):
        if i*j <= 30 :
            print(f'{i} * {j} = {i*j}')
        else :
            break


i = 2
while i < 10 :
    j = 1
    while j < 10 :
        if i * j > 30 :
            break
        else:
            print(f'{i} * {j} = ', i*j, end = ' ')
        j += 1
    print('')
    i += 1

# ##문제 10 : 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
# 힌트: 이 문제는 반복이 두 단계다. 2부터 1000까지 하나씩 검사한다. 각 숫자마다 소수인지 확인한다.
# 그래서 while 안에 while 구조가 필요하다.
i = 1
num = 0
while i < 1000 :
    count = 0
    j = 1
    while j <= i:
        if i % j == 0 :
            count += 1
        j += 1
    if count == 2:
        print(f'소수인 수는 {i}')
        num += 1
    i += 1
print(f'소수의 갯수는 {num}')


##문제 11 :1부터 50까지의 숫자 중 3의 배수는 건너뛰고 나머지 수만 출력하라
for i in range(1, 51):
    if i % 3 == 0 :
        continue
    else :
        print(f'3의 배수가 아닌 수는 {i}')



i = 0
while i < 50 :
    i += 1
    if i % 3 == 0 :
        continue
    else :
        print(f'3의 배수가 아닌 수는 {i}')




##문제 12 :1부터 100까지 출력하되 4의 배수, 6의 배수는 건너뛴다. 그 외의 수 중 5의 배수만 출력하고 그들의 합도 출력하라
sum = 0
for i in range(1, 101):
    if i % 4 ==0 or i % 6 == 0:
        continue
    elif i % 5 == 0:
        sum += i
        print(f'4와 6의 배수가 아닌 5의 배수는 {i}')

# print(f'합계는 {sum}')
# ##문제 13 :
# ##문제 14 :