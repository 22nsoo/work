####매개변수 유형
####위치 매개변수 : 인수와 순서대로 대응
####기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용
####키워드 매개변수 : 실인수와 가인수를 간 동일 이름으로 대응
####가변 매개변수 : 인수의 갯수가 동적인 경우

def showGugu(start, end) :                  ####매개변수, 인자, argument임 두개의 인자를 줘야 한다.
    for dan in range(start, end + 1, 1) :
        print(str(dan) + '단 출력')
        for i in range(1, 10) :
            print(str(dan) + '*' + \
                  str(i) + '=' + str(dan*i), end = ' ')
        print()

showGugu(2, 3)



def showGugu(start, end = 5) :                  ####기본값 매개변수: 값을 주지 않으면 default로 5를 준다
    for dan in range(start, end + 1, 1) :
        print(str(dan) + '단 출력')
        for i in range(1, 10) :
            print(str(dan) + '*' + \
                  str(i) + '=' + str(dan*i), end = ' ')
        print()

showGugu(2, 3)
print()
showGugu(2)
print()
showGugu(start = 7, end = 9)        ###키워드 매개변수 1대1 대응이기 때문에 순서가 바뀌어도 됨
print()
showGugu(end = 9, start = 7)
print()
showGugu(7, end = 9)                ###end만 써줘도 들어감 showGugu(start = 7, 9) or showGugu(end = 9, 7)이건 안됨


print('가변 매개변수 --------------')
def func1(*ar):                     ####'*'은 여러개의 인자를 tuple로 묶어서 받겠다는 의미(packing)
    print(ar)
    for i in ar:
        print('밥 : ', i)

func1('김밥')
func1('김밥','비빔밥','볶음밥','공기밥')
print()

def func2(a, *ar):
    print(a)
    print(ar)

func2('김밥','비빔밥')
func2('김밥','비빔밥','볶음밥','공기밥')

# def func2(*a, ar):                            문법 오류는 아님 runtime error(type error)
#     print(a)
#     print(ar)

# func2('김밥','비빔밥')
# func2('김밥','비빔밥','볶음밥','공기밥')
print()
def func3(w, h, **other) :                      ####'**'이건 dict를 달라고 하는 것
    print(f'몸무게 : {w}, 키는 {h}')
    print(f'기타 : {other}')

func3(80, 180, irum = '신기루', nai = 23)
###func3(80, 180, {'irum' = '신기루', 'nai' = 23})          dict를 미리 만들어서 주면 안됨

print()
def func4(a, b, *c, **d) :
    print(a, b)
    print(c)
    print(d)


func4(1,2)                              ##tuple, dict 비움
func4(1,2,3,4,5)                        ##dict 비움
func4(1,2,3,4,5,kbs = 9, mbc =11)       ##다 채움

print()


###type hint : 함수의 인자와 반환값에 type을 적어 가독성 향상 구속력은 없음 int 넣으라고 했지만 다른거 줘도 됨
def typeFunc(num:int, data:list[str]) -> dict[str, int]:
    print(num)
    print(data)
    result = {}                             ##dict인지 set인지 모름
    for idx, item in enumerate(data, start = 1):
        print(f'idx : {idx}, item : {item}')
        result[item] = idx                  ###dict 확정
    return result

rdata = typeFunc(1, ['일','이','삼'])
print(rdata)
print()
rdata = typeFunc('한개', [10,20,30])
print(rdata)
