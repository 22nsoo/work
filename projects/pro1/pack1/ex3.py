#기본 자료형 : int, float, bool, complex
#묶음 자료형 : str, list, tuple, set, dict

#1) str : 문자열 묶음 자료형, 순서O, 수정X
s = 'sequence'
print(s, id(s))

print('길이 : ', len(s))
print(s[0], s[2])
print('길이 : ', s.find('e'), s.find('e', 3), s.rfind('e'))
#인덱싱 / 슬라이싱
print(s[5])# 변수명[순서], index는 0 부터
print(s[2:5])
print(s[:], "", s[0:len(s)-1])
print(s[0: 7: 2])
print(s[-1])

#2) List : 다양한 종류의 자료 묶음형, 순서O, 수정O, 중복O
a = [1, 2, 3]
print(a, a[0], a[0:2])
b = [10, a, 10, 20.5, True, '문자열'] #List 안에 List 들어갈 수 있음 잡탕 가능
print(b)
print(b, '', b[1], '', b[1][0]) #b의 1번 인덱스는 List인데 그 안에 0번 인덱스는 1이니까 1 나옴
print()

family = ['엄마', '아빠', '나', '여동생']
print(family)
print(id(family))
family.append("남동생")
print(family)
print(id(family))
family.remove("나")
print(family)
family.insert(0, "할머니")
print(family)
family.extend(['삼촌', '고모', '조카'])
print(family)
family += ['이모']
print(family)
print(family.index('아빠'))
print('엄마' in family)
print('나' in family)
family.remove("아빠")
del family[2]
print(family)

print()
kbs = ['123', '34', '234']
kbs.sort()              #문자열 정렬 오름차순
print(kbs)

mbc = [123, 34, 234]    #숫자 정렬 내림차순
mbc.sort()
print(mbc)

sbs = [123, 34, 234]
ytn = sorted(sbs)
print(sbs)
print(ytn)
print()

name = ['tom', 'james', 'oscar']
name2 = name
print(name)
print(name2)
print(id(name), id(name2))


##깊은 복사 새로운 객체에게 치환 값은 같지만 주소가 다르다
import copy
name3 = copy.deepcopy(name)
print(name3, id(name3))

name[0] = '길동'
print(name)
print(name2)
print(name3)                #영향을 안받는다

##3) tuple : 리스트와 유사, 읽기 전용(수정 불가)
t = (1, 2, 3, 4)
t = 1, 2, 3, 4      #위와 동일
print(t, type(t))
k = (1)                  #하나만 쓰면 int임
print(k, type(k))      
k = (1, )                #이렇게 쓰면 tuple
print(k, type(k))        
print(t[0], '', t[0:2])
##t[0] = 77                   ##Error 뜸 수정 불가
imsi = list(t)                ##리스트로 변환해서 수정하고 튜플로 변환
imsi[0] = 77
t = tuple(imsi)
print(t, type(t))

##4) set : 순서X, 중복X
ss = {1, 2, 1, 3}
print(ss)
ss2 = {3, 4}            ##ss와 ss2의 교집합은 3, 합집합은 1,2,3,4
print(ss.union(ss2))                    #합집합
print(ss.intersection(ss2))             #교집합
print(ss - ss2 | ss2, ss & ss2)         #차, 합, 교집합
##print(ss[0])                          #Error 뜸 순서 X

ss.update({6, 7})                       #값 추가
print(ss)
ss.discard(7)
ss.discard(7)                         #값 삭제(해당 값이 있으면 지우고 없으면 넘어감)
print(ss)                               
ss.remove(6)                          #값 삭제(해당 값이 있으면 지우고 없으면 에러 뜸)
print(ss)

li = ['aa', 'aa', 'bb', 'cc', 'aa']
print(li)
imsi = set(li)
li = list(imsi)
print(li)


print("-----" * 20)
##5) dict : 사전 자료형 {'키' : 값} 형태, 인덱스가 없다(키를 갖고 값을 찾음)
##방법 1
mydic = dict(k1 = 1, k2 = 'ok', k3 = 123.4)
print(mydic, type(mydic))

##방법 2
dic = {'파이썬' : '뱀', '자바' : '커피', '인사' : '안녕'}
print(dic)
print(dic['자바'])
print(dic['인사'])          #키로 값을 검색한다

ff = dic.get('자바')
print(ff, type(ff))

###print(dic[0])               #에러 인덱싱 없다
dic['금요일'] = '와우'              #데이터 추가
print(dic)
del dic['인사']
print(dic)
print(dic.keys())
print(dic.values())
