###반복분 for

# for i in [1,2,3,4,5] :          ####묶음형 자료(list, tuple, set, dict)에 사용 하나씩 꺼내줌 없으면 탈출
# for i in (1,2,3,4,5) :
# for i in {1,2,3,4,5} :
#     print(i, end ='')


print('\n분산/표준편차 ------')
# numbers = [1,3,5,7,9]
numbers = [-3,4,5,7,12]
# numbers = [3,4,5,6,7]
tot = 0
for i in numbers :
    tot += i
print(f'합은 {tot}, 평균은 {tot/len(numbers)}')
avg = tot/len(numbers)

##편차의 합 구하기
hap = 0
for i in numbers :
    hap += (i - avg) ** 2
print(hap)
vari = hap / len(numbers)
print(f'분산은 {vari}')
print(f'표준편차는 {vari ** 0.5}')


print()
colors = ['r', 'g', 'b']
for v in colors :
    print(v, end = ' ')




print('iter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수')
iterator = iter(colors)
for v in iterator :
    print(v,end =', ')

print()
for idx, d in enumerate(colors) :               ##인덱스와 값을 반환한다 enumerate
    print(idx, ' ', d)
print('사전형 -------')

datas = {'python' : '만능어', 'java' : '웹용어', 'mariadb' : 'RDBMS'}
for i in datas.items() :
    print(i[0], '~~', i[1])


for k, v in datas.items() :
    print(k, '~~', v)


for k in datas.keys() :
    print(k)

for v in datas.values():
    print(v, end = '')



print('다중 for -------')
for n in [2,3] :
    print('-- {}단 --'.format(n))
    for i in [1,2,3,4,5,6,7,8,9] :
        print('{} * {} = {}'.format(n,i,n*i))



print('continue, break --------')
nums = [1,2,3,4,5]

for i in nums :
    if i == 2:
        continue
    # elif i == 4 :
    #     break
    print(i, end = ' ')
else :
    print('정상 종료')


print('정규 표현식 + for')

str = """이 최고위원은 이날 국회에서 열린 최고위원회의에서 “국민들이 이재명 정부의 중도·실용 노선을 신뢰하고 압도적 지지를 보내고 있는데
자꾸 당이 독자 노선을 추구하거나 당내 노선 갈등이 심각히 벌어진다면 당과 대통령의 지지율 계속 디커플링되다 결국 대통령 국정 지지까지 흔들리게 될 수밖에 없다”며 이렇게 말했다.
이 최고위원은 “하늘 아래 2개의 태양 있을 수 없단 게 진리”라며 “이 사안의 정치적 본질은 대통령 지지율이 매우 높고 대통령의 권한이 강력한 임기 초반에 2·3인자들이 판을 바꿔 당권·대권에 대한 욕망이 표출된 결과임을
부인하기 어렵다”고도 주장했다. hdshfwfjwepif"""

import re
str2 = re.sub(r'[^가-힣\s]','',str)           ##한글과 공백 이외의 문자는 공백처리 대괄호 안에 ^이 있으면 부정

print(str2)

str3 = str2.split(' ')                       ### 공백을 기준으로 문자 분리
print(str3)
cou = {}

for i in str3 : 
    if i in cou :
        cou[i] += 1                                 ##같은 단어가 있으면 누적
    else :
        cou[i] = 1                                  ###최초 단어일 경우 '단어' : 1

print(cou)

print('정규 표현식 좀 더 연습')

for test_ss in ['111-1234', '일이삼-일이삼사', '222-1234', '333&1234'] :
    if re.match(r'^\d{3}-\d{4}$', test_ss) :
        print(test_ss, "전화번호 맞아요")                     ###대괄호 밖에 ^이 있으면 처음이 라는 뜻, $는 끝
    
    else :
        print('전화번호 아니다.')


print('comprehension : 반복문 + 조건문 + 값 생성을 한줄로 표현')
a = [1,2,3,4,5,6,7,8,9,10]
li = []
for i in a :
    if i % 2 == 0 :
        li.append(i)

print(li)
print(list(i for i in a if i % 2 == 0))                 ###위와 같음


datas = [1, 2, 'a', True, 3.0]
datas = {1, 2, 'a', True, 3.0, 1, 2, 1, 2}
li2 = [i*i for i in datas if type(i) == int]
print(li2)


id_name = {1:'tom', 2:'oscar'}
name_id = {val:key for key, val in id_name.items()}

print(name_id)


print()
print([1,2,3])
print(*[1,2,3])                 ###unpack
aa = [(1,2), (3,4), (5,6)]

for a, b in aa :
    print(a + b)


print([a + b for a, b in aa])                    ##[3, 7, 11]
print(*[a + b for a, b in aa])                  ##3 7 11
print(*[a + b for a, b in aa], sep='\n')


print('\n 수열 생성 : range')
print(tuple(range(1,6,2)))                     ##1부터 6미만 반환 step size = 2, range(1,6,2)



print(tuple(range(-10,-100,-20)))     

print(set(range(1,6)))

for i in range(6) :
    print(i, end = ' ')



tot = 0
for i in range(1,11) :
    tot = tot + i

print('\ntot : ' , tot)
print('tot : ', sum(range(1,11)))

for i in range(1,10) :
    print(f'2 * {i} = ', 2 * i)

##문제 1 : 2~9 구구단 출력(단은 행 단위 출력)
##문제 2 : 주사위를 두번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력


print('\nend')



