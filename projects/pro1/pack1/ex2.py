#연산자
v1 = 3                      #치환 연산자
v1 = v2 = v3 = 5
print(v1, v2, v3)
print('출력 1', end = ', ')  #출력 이어가기
print('출력 2')
print('출력 3')

v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

v1 = 1, 2, 3, 4, 5          #v1 = (1, 2, 3, 4, 5)같은 얘기
print(v1)
print(type(v1))

print('값 할당 : packing 연산')
*v1, v2 = [1,2,3,4,5]       #맨 뒤에거만 v2주고 나머지는 v1가짐
print(v1, v2)

v1, *v2 = [1,2,3,4,5]       
print(v1, v2)

v1, *v2, v3 = [1,2,3,4,5]       
print(v1, v2, v3)




print(format(1.5678, '10.3f'))

print('나는 나이가 %d 이다.'%23)

print('나는 나이가 %s 이다.'%'스물셋')

print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))

print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))

print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))

print('이름은 {0}, 나이는 {1}'.format('한국인', 33))        

print('이름은 {}, 나이는 {}'.format('신선해', 33))          #비우면 앞에서부터 순서대로 들어감

print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))        #{}안의 숫자는 순서


abc = 123
print(f'abc의 값은 {abc}임')                             #요즘 가장 많이 씀

print('\n\t본격적 연산 --------')                          #\n, \b, \t ..게행문자
print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 3 ** 3)
    #8 2 15 1.6666666666666667 1 2 27

print(divmod(5,3))
result = 3 + 4 * 5 + (2 +3) / 2 #() -> ** -> 단항 -> 산술(*, /, -> +, -) -> 관계 -> 논리
print(result)

print(5 > 3, 5 == 3, 5 != 3)

print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 < 3))

print(True and False or False)

print(True or False and False) #and가 or보다 연산순위가 높다

print(4 + 5)
print("4" + "5")
print('한'+'국'+'만세')
print('한국' * 5)

print("누적")
a = 10
a = a + 1
a += 1
a *= 3
print(f"a는 {a}")
#print(a++)      ##증감 연산자 없다
print(--a)
print(-a)
print(a * -1)


# print(("1"+"1")+1)      #type error
print(int("1"+"1")+1)       #int(문자열) -> 정수화
print(float("1"+"1")+1)     #float(문자열) -> 실수화
print(str(1+1)+'1')         #str(숫자) -> 문자화


print("boolean 처리", bool(True), bool(False))
print("boolean 처리", bool(1), bool(1.2), bool('ok'), bool([12]))
print("boolean 처리", bool(0), bool(0.0), bool(''), bool([]), bool(None))

#r 선행문자 게행문자를 문자열로 하고 싶으면 쓴다.
print('aa\tbb')
print('aa\nbb')
print(r'aa\tbb')
print(r'aa\nbb')