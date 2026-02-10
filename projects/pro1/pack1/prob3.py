#재귀문제 :  리스트 자료 v = [7, 9, 15, 43, 32, 21] 에서 최대값 구하기 - 재귀 호출 사용 
v = [7, 9, 15, 43, 32, 21]

def find_max(v, n) :
    if n == 1 :
        return v[0]
    
    if v[n-1] >= m   :
        m = v[n-1]
    
print(find_max(v, len(v)))