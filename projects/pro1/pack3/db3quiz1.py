# 문1) jikwon 테이블 자료 출력
# 키보드로부터 부서번호를 입력받아, 해당 부서에 직원 자료 출력
# 부서번호 입력 : _______
# 직원번호 직원명 근무지역 직급
# 1 홍길동 서울 이사
# ...
# 인원 수 :

import MySQLdb
import pickle



"""
config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8'
}
"""

with open('mydb.dat', mode = 'rb') as obj:
    config = pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        bu_no = input("부서번호 입력 : ")
        sql = """
        select jikwonno as 직원번호, jikwonname as 직원명, buserloc as 근무지역, jikwonjik as 직급
        from jikwon inner join buser on buserno = busernum where busernum = {0}
        """.format(bu_no)                   ##sql 문장 완성
        # print(sql)
        cursor.execute(sql)

        datas = cursor.fetchall()
        # print(datas)
        if len(datas) == 0 :
            print(bu_no + "번 부서는 없어요")
            return 
        

        for jikwonno, jikwonname, buserloc, jikwonjik in datas:
            print(jikwonno, jikwonname, buserloc, jikwonjik)
        print('인원수 : ', len(datas))


    except Exception as e:
        print('err : ', e)
    finally:
        cursor.close()
        conn.close()

def chulbal1():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()



        sql = """
        select jikwonno as 직원번호, jikwonname as 직원명, busername as 부서명, busertel as 부서전화, jikwonjik as 직급, jikwongen as 성별
        from jikwon inner join buser on buserno = busernum where busernum = (select busernum where jikwonno = {0}) group by jikwonjik order by jikwonjik asc 
        """.format(jik_num)

        cursor.execute(sql)
        data = cursor.fetchall()

        if len(data) == 0:
            print('로그인 실패')
            return
        else:
            print('로그인 성공')
            for a, b, c, d, e, f in data :
                print(a, b, c, d, e, f)


        print('직원수 : ', len(data))


    except Exception as e:
        print('err : ', e)
    finally:
        cursor.close()
        conn.close()


def chulbal2():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        sql = """
        select gogekno as 고객번호, gogekname as 고객명, gogektel as 고객전화, truncate((127 - substring(gogekjumin, 1, 2)),0) as 나이
        from gogek inner join jikwon on gogekdamsano = jikwonno where jikwonname = '{0}' and jikwonno = {1}    
        """.format(jik_irum, jik_num)

        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data) == 0:
            print('고객수 없음')
        else:
            for a, b, c, d in data :
                print(a, b, c, d)


        print('관리 고객수 : ', len(data))


    except Exception as e:
        print('err : ', e)
    finally:
        cursor.close()
        conn.close()



if __name__ == '__main__':
    # jik_num = input('직원번호 입력 : ')
    # jik_irum = input('직원명 입력 : ')
    # print('직원번호 직원명 부서명 부서전화 직급 성명')
    # chulbal1()
    # print()
    # print('고객번호 고객명 고객전화 나이')
    # chulbal2()
    chulbal()

