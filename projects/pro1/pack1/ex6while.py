a = 1
while a <= 5 :
    print(a, end = '')
    a += 1

else : 
    print("수행성공")


print()

i = 1
while i <= 3 :
    j = 1
    while j <= 4 :
        print('i = ' + str(i) + '/j = ' + str (j))
        j += 1
    i += 1


print()



i = 1
sum = 0
while i <= 33 :
    sum = sum + (i * 3)
    i += 1

print(sum)



su = 1
hap = 0

while su <= 100 :
    if su % 3 == 0 :
        hap += su
    su += 1

print("합은 : " + str(hap))


print()

colors = ["빨강", "파랑", "노랑", "검정"]
num = 0

while num < len(colors) :
    print(colors[num])
    num += 1


print('\n 별 찍기 -------------------')
i = 1
while i <= 10 : 
    j = 1
    msg = ''
    while j < i : 
        msg += "*"
        j += 1
    print(msg)
    
    i += 1

print("\nif 블럭 내 while loop\n")

import time
sw = input("폭탄 스위치를 누를까요? : [y/n]")
if sw == 'y' or sw == 'Y' :
    count = 5
    while 1 <= count :
        print("%d초 남았습니다." %count)
        time.sleep(1)                           ##1초 지연
        count -= 1
    print('폭발')

elif sw =='n' or sw == 'N' :
    print('작업 취소')

else :
    print("y 또는 n을 누르세요.")


print('\ncontinue와 break\n -----------')

a = 0
while a<10 :
    a += 1 
    if a == 3 or a == 5:
        continue                 ###아래 문장을 무시하고 while로 이동
    # if a == 7 :
    #     break                    #### while 문 무조건 탈출, 비정상 종료 else를 만나지 않는다. else는 있어도 그만 없어도 그만
    print(a)

else : 
    print('정상종료.')


print('while 수행후 %d' %a)

print('\n 홀수 짝수 확인하기\n')

while True :                        ##True , 1, 100, -12, 'ok' 다 참이다
    pass
    mysu = int(input("입력할 숫자 : "))
    if mysu == 0 :
        break
    elif a % 2 == 0 : 
        print("%d는 짝수" %mysu)
    else :
        print('%d는 홀수' %d)

print("end")