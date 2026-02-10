## 예외처리 : 파일, 네트워크, DB작업, 실행에러 등의 에러 대처
## 에러 뜰거 같으면 무조건 걸어라

def divide(a, b):
    return a/b


print('이런 저런 작업 진행 ...')
# c = divide(5, 2)
# c = divide(5, 0)        ##0으로는 나눌 수가 없음(에러)
# print(c)


try :                       ###예외 발생가능 구문
    c = divide(5,2)
    print(c)
    aa = [1,2]
    print(aa[0])
    print(aa[3])
    

    open("/opt/anaconda3")

except ZeroDivisionError:           ##예외 종류 관련 클래스
    print('두번째 값은 0을 주면 안돼요')        ##예외 발생 처리 구문

except IndexError as err:
    print('참조범위 오류', err)

except Exception as eeeee : 
    print('에러', eeeee)

finally :
    print('에러 유무에 상관없이 반드시 수행된다.')

print('end')