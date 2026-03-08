#!/opt/anaconda3/envs/myproject/bin/python
import sys
sys.stdout.reconfigure(encoding = 'utf-8')

import MySQLdb
import pickle
import os

BASE = os.path.dirname(__file__)
with open(os.path.join(BASE, "mydb.dat"), "rb") as obj:
    config = pickle.load(obj)


##행은 tr 열은 td
print("Content-Type: text/html; charset=utf-8")
print()
print("<html><body><b>** 상품정보 **</b><br/>")
print("<table border='1'>") #두께가 1
print("<tr><td>코드</td><td>상품명</td><td>수량</td><td>단가</td></tr>") #td는 열

try : 
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()

    cursor.execute("select * from sangdata order by code desc")
    datas = cursor.fetchall()
    for code, sang, su, dan in datas:
        print("""
            <tr>                         
                <td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td>            
            </tr>
            """.format(code, sang, su, dan))


except Exception as e:
    print("err: ", e)

finally: 
    cursor.close()
    conn.close()

print("</table>")
print("</body></html>")