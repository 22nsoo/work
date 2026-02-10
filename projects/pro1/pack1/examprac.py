i = 1

while i < 100 :
    if i % 3 != 0 and i % 2 != 0:
        print('3의 배수 또는 2의 배수가 아닌 수는 : ', i)
        
    i += 1

i = 2
while i <= 5 :
    j = 1
    while j <= 9 :
        print(f'{i} * {j} = {i*j}',  end = ' ')
        j += 1
    print('')
    i += 1

i = 1
sum = 0
while i <= 100:
    if i % 2 == 0 :
        sum += i
    
    else : 
        sum -= i
    i += 1

print('합계는 : ', sum)


i = 1
j = -1
sum = 0
while i < 100:
    print(i*j)
    sum = sum + j*j
    i = i + 2
    j *= -1
    
print('합계 : ', sum)



i = 1
sum = 0
while 1:
    sum += i
    if sum > 1000:
        break
    i +=1
print(f'1000을 넘는 순간 숫자는 {i}')


i = 1
while i < 100:
    if i%10 + i//10 >=10:
        print(f'각 자릿 수 합이 10 이상인 수는 {i}')

    i += 1




i = 2
while i < 10:
    j = 1
    while j < 10:
        if i*j > 30:
            break
        print(f'{i} * {j} = {i*j}', end =' ')
        j += 1
    print()
    i += 1




def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas

def processfunc(datas):
    for data in datas:
        emp_no, name, base_pay, hire_year = data
        

processfunc(inputfunc())





def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas


def answer(datas):
    # 1. 취급상품표 (단가)
    price = {
        '새우깡': 450,
        '감자깡': 300,
        '양파깡': 350
    }
    
    sogye_gun = []
    sogye_ack = []

    for data in datas :
        name, num = data.split(',')
        don = price[name]
        total_money = don * int(num)
        if name =='새우깡':
            sogye_ack[0] += don * int(num)
            sogye_gun[0] += int(num)
        elif name =='새우깡':
            sogye_ack[1] += don * int(num)
            sogye_gun[1] += int(num)
        if name =='새우깡':
            sogye_ack[2] += don * int(num)
            sogye_gun[2] += int(num)
        print(f'{name}   {num}   {don}   {total_money}')
    
    for i in range(1,4):
        print(f'{sogye_ack}.   {sogye_gun}')

    

answer(inputfunc())




def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas


def answer(datas):
    # 1. 취급상품표 (단가)
    price = {
        '새우깡': 450,
        '감자깡': 300,
        '양파깡': 350
    }

    # 2. 소계용 딕셔너리 초기화
    sub_cnt = {'새우깡': 0, '감자깡': 0, '양파깡': 0}
    sub_sum = {'새우깡': 0, '감자깡': 0, '양파깡': 0}

    total_cnt = 0
    total_sum = 0

    # 3. 헤더 출력
    print("상품명   수량   단가   금액")
    print("-" * 35)

    # 4. 데이터 처리
    for data in datas:
        name, cnt = data.split(',')
        cnt = int(cnt)
        unit = price[name]
        money = cnt * unit

        print(f"{name:<6} {cnt:>4} {unit:>6} {money:>7}")

        # 소계 누적
        sub_cnt[name] += cnt
        sub_sum[name] += money

        # 총계 누적
        total_cnt += cnt
        total_sum += money

    # 5. 소계 출력
    print("\n소계")
    for name in sub_cnt:
        print(f"{name} : {sub_cnt[name]}건   소계액 : {sub_sum[name]}원")

    # 6. 총계 출력
    print("\n총계")
    print(f"총 건수 : {total_cnt}")
    print(f"총 액  : {total_sum}원")


answer(inputfunc())
