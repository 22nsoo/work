"""
문3) 성별 직원 현황 출력 : 성별(남/여) 단위로 직원 수와 평균 급여 출력
성별 직원수 평균급여
남 3 8500
여 2 7800
pickle을 이용하기
"""

import pickle
import MySQLdb

with open('mydb.dat', mode = 'rb') as obj:
    config = pickle.load(obj)

def myFunc1():
    try: 
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        sql = """
        select jikwongen as 성별, count(*) as 직원수, avg(jikwonpay) as 평균급여 from jikwon where jikwongen is not null group by jikwongen 
        """

        cursor.execute(sql)
        data = cursor

        for a, b, c in data:
            print(a, b, c)


    except Exception as e:
        print('err : ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def myFunc2():
    try: 
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        sql = """
        select jikwonno as 직원번호, jikwonname as 직원명, count(gogekno) as 관리고객수 from jikwon inner join gogek on jikwonno = gogekdamsano
        group by jikwonno
        """

        cursor.execute(sql)
        data = cursor

        for a, b, c in data:
            print(a, b, c)


    except Exception as e:
        print('err : ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__' :
    myFunc2()