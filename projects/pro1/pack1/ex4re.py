import re       #정규표현식 지원 모듈

ss = "1234 abc가나다abcABC_123555집에가나78요_6'Python is fun'"
print(ss)
print(re.findall(r'123', ss))           ##정규표현식에서는 r을 선행해라. findall의 return type은 list이다.
print(re.findall(r'가나', ss))    
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss))
print(re.findall(r'[0-9]*', ss))
print(re.findall(r'[0-9]?', ss))
print(re.findall(r'[0-9]{2}', ss))
print(re.findall(r'[0-9]{2,3}', ss))
print(re.findall(r'[a-zA-z]+', ss))
print(re.findall(r'[가-힣]+', ss))
print(re.findall(r'\d+', ss))
print(re.findall(r'\D+', ss))