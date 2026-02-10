# def inputfunc():
#     datas = [
#         [1, "강나루", 1500000, 2010],
#         [2, "이바다", 2200000, 2018],
#         [3, "박하늘", 3200000, 2005],
#     ]
#     return datas


# ####don[2] = 기본급
# ####yy = 근속연수
# ####geun = 근속수당
# ####gy = 급여액
# ####gong = 공제액
# ####su = 수령액

# def processfunc(datas):
#     for don in datas: 
#         yy = 2026 - int(don[3])
#         del don[3]
#         don.append(yy)
#         if yy >= 9 :
#             geun = 1000000
#         elif yy >= 4 :
#             geun = 450000
#         else :
#             geun = 150000
        
#         gy = don[2] + geun

#         if gy >= 3000000 :
#             gong = 0.5 * gy
#         elif gy >= 2000000 :
#             gong = 0.3 * gy
#         else :
#             gong = 0.15 * gy
        
#         su = gy - gong
#         don.append(int(geun))
#         don.append(int(gong))
#         don.append(int(su))
#         for j in don :
#             print(j, end = ' ')
#         print('')
#     return don[0]


# print('사번 이름 기본급 근무년수 공제액 수령액')
# print('---'*20)
# print(f'처리 건수 : {processfunc(inputfunc()) + 1}')



# def inputfunc():
#     datas = [
#         "새우깡,15",
#         "감자깡,20",
#         "양파깡,10",
#         "새우깡,30",
#         "감자깡,25",
#         "양파깡,40",
#         "새우깡,40",
#         "감자깡,10",
#         "양파깡,35",
#         "새우깡,50",
#         "감자깡,60",
#         "양파깡,20",
#     ]
#     return datas


# def pro():
#     sae = 0
#     gam = 0
#     yang = 0
#     for i in inputfunc() :
#         j = i.split(',')
#         if j[0] == '새우깡' :
#             dan = 450
#             sae += int(j[1])
#         elif j[0] == '감자깡' :
#             dan = 300 
#             gam += int(j[1])
#         else : 
#             dan = 450
#             yang += int(j[1])
#         j.append(dan)
#         j.append(dan * int(j[1]))
#         for k in j :
#             print(k, end = ' ')
#         print()
    
#     print(i)
    
    








# 문제 1
def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas

def processfunc(datas):
    CURRENT_YEAR = 2026

    for data in datas:
        emp_no, name, base_pay, hire_year = data            ##이 방법 보기

        work_years = CURRENT_YEAR - hire_year

        if work_years <= 3:
            bonus = 150000
        elif work_years <= 8:
            bonus = 450000
        else:
            bonus = 1000000

        salary = base_pay + bonus

        if salary >= 3000000:
            tax_rate = 0.5
        elif salary >= 2000000:
            tax_rate = 0.3
        else:
            tax_rate = 0.15

        tax = int(salary * tax_rate)
        net_pay = salary - tax

        data.append(work_years)
        data.append(bonus)
        data.append(tax)
        data.append(net_pay)

    print("사번  이름    기본급    근무년수  근속수당  공제액    수령액")
    print("-" * 75)

    for d in datas:
        print(f"{d[0]:<4} {d[1]:<6} {d[2]:<8} {d[4]:<8} {d[5]:<8} {d[6]:<8} {d[7]}")    ###몇칸 띄우는지 나타내는 것

    print("-" * 75)
    print(f"처리 건수 : {len(datas)} 건")


datas = inputfunc()
processfunc(datas)






# 문제 2번
def inputfunc_2():                  #csv
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

def solution_func_second():
    price_by_name = {"새우깡":450, "감자깡":300, "양파깡": 450}

    arr_items = inputfunc_2()

    len_arr = len(arr_items) # 12개

    count_by_name = {name: 0 for name in price_by_name}
    # {'새우깡': 0, '감자깡': 0, '양파깡': 0}

    # amt_by_name == amount_by_name
    amt_by_name = {name: 0 for name in price_by_name}
    # {'새우깡': 0, '감자깡': 0, '양파깡': 0}

    names = []; cnts = []
    for arr_item in arr_items:

        # nms_dt == Names_data, cs_dt == cnts_data
        nms_dt, cs_dt = arr_item.split(",")
        names.append(nms_dt); cnts.append(cs_dt)
        # 이름, 갯수 모음

        int_cd, int_pp = int(cs_dt), int(price_by_name[nms_dt])
        # 정수형 변환

        count_by_name[nms_dt] += int_cd     
        # {'새우깡': 135, '감자깡': 115, '양파깡': 105}

        amt_by_name[nms_dt] += int_cd * int_pp
        # {'새우깡': 60750, '감자깡': 34500, '양파깡': 47250}

    # print(names); print(cnts) # 이름과 갯수의 리스트

    order_table = [[0] * 4 for _ in range(len_arr)] # 상품의 출력 보드

    for row, item in enumerate(arr_items):
        int_cnts, int_pp = int(cnts[row]), int(price_by_name[names[row]])

        order_table[row][0] = names[row]
        order_table[row][1] = cnts[row]
        order_table[row][2] = price_by_name[names[row]]
        order_table[row][3] = int_cnts * int_pp

    # print(order_table)

    print("출력 형태:")
    print(f"{'상품명':<6} {'수량':>6} {'단가':>5} {'금액':>6}")
    print("-" * 35)
    for row in range(len_arr):
        print(f"{order_table[row][0]:<6}  {order_table[row][1]:>6}  {order_table[row][2]:>6}  {order_table[row][3]:>8}")

    print("\n소계")

    sum_eps = 0; sum_as = 0
    for name in price_by_name:
        print(f"{name} : {count_by_name[name]}건   소계액 : {amt_by_name[name]}원")
        sum_eps += int(count_by_name[name])
        sum_as += int(amt_by_name[name])

    print("총계")
    print(f"총 건수 : {sum_eps}")
    print(f"총 액   : {sum_as}")

if __name__ == "__main__":
    solution_func_second()
