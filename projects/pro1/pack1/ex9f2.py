###사용자 정의 함수
""""

def 함수명(가인수,,,):
    return 반환값               ###1개만 반환, return이 없으면 return None


    
함수명(실인수,,,)           ###함수 호출

"""

def doFunc1():
    print('doFunc1 수행')
    return None

def doFunc2(name):
    print('name : ', name)
    return None

def doFunc3(arg1, arg2):
    re = arg1 + arg2
    return re

def doFunc4(a1, a2) :
    imsi = a1 + a2
    
    if imsi % 2 == 1 :
        return
    else :
        return imsi

doFunc1()                           ###함수 호출
print(doFunc1)                      ##함수의 주소를 찍음
print('함수 주소는 ', id(doFunc1))
imsi = doFunc1
imsi()
print(doFunc1())                    ##None (함수가 들고 오는게 반드시 있음 none 들고 온것)

print()

doFunc2(2)
doFunc2('이인수')




print('-----------' * 10)
doFunc3('대한', '민국')
print(doFunc3('대한','민국'))
print(doFunc3(5,6))
result = doFunc3('5','6')
print(result)


print(doFunc4(3,4))
print(doFunc4(3,5))
print('------'*10)

def triArea (a, b) :
    c = a*b/2
    triAreaPrint(c)                 ###다른 함수 호출

def triAreaPrint(cc) :
    print('삼각형 면적은' , cc)

triArea(20, 30)
print('------'*10)

def passResult(kor, eng):
    ss = kor + eng
    if ss >= 50 :
        return True
    else :
        return False

if passResult(30, 20):
    print('합격')
else :
    print('불합격')

print('------'*10)
def swapFunc(a, b):
    return b, a             ###return(b, a)     두개를 return 하는게 아니라 하나를 묶음으로 반환함 여기선 tuple

a = 10
b = 20
print(a, '', b)
print(swapFunc(30, 20))

print('------'*10)
def funcTest():
    print('funcTest 멤버 처리')
    def funcInner():
        print('내부 함수')
    funcInner()                         ###함수 내부에 함수를 선언할 수 있다.


funcTest()

###if 조건식 안에 함수 사용
def isOdd(para):
    return para % 2 == 1             ###홀수이면 True 반환 짝수이면 False


mydict = {x:x for x in range(11) if isOdd(x)}           ###key, val
print(mydict)


print('변수의 생존 범위(scope rule) ----------')
###변수가 저장되는 이름공간은 변수가 어디서 선언되었는가에 따라 생존 시간이 다름
###전역, 지역 변수



###Local > Enclosing function > Global > Built-in
player = '전국대표'
name = '한국인'
def funcSoccer():
    name = '홍길동'
    player = '지역대표'
    city = '서울'
    print(f'이름은 {name} 수준은 {player}')
    print(f'지역은 {city}')

funcSoccer()
print(f'이름은 {name} 수준은 {player}')


print()

a = 10 ; b = 20 ; c = 30
def Foo() :
    a = 7
    def Bar() :
            global c                ##bar 함수의 멤버가 아니라 모듈의 멤버가 됨
            b = 8
            print(f'함수 수행 후 a : {a} , b : {b}, c : {c}')
    Bar()
    print(f'foo 수행 후 a : {a} , b : {b}, c : {c}')
Foo()

print(f'함수 수행 후 a : {a} , b : {b}, c : {c}')

print()
g = 1
print('g : ', g)
def func():
    global g
    a = g                   #####a는 g라는 값을 갖게 됨
    g = 2                 #####func 안에서 g라는 변수가 지역변수로 선언되어버림, 값을 치환하는 순간 지역변수로 바뀜
    return a
print(func())
print('g : ', g)            #####쭉 진행을 하면서 문법적으로 이상이 있는지 확인하고, 선언함 그후 실행함