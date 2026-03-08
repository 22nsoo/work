print('파일 처리 ----------------')
import os

try :                       #파일 작업 할 때 try except는 꼭 걸고 해라
    print('파일 로딩 ----------------')
    print(os.getcwd())      #/Users/insu/Desktop/work/projects/pro1/pack2
    # f1 = open(os.getcwd() + '/ftext.txt', encoding = 'utf-8')           #이게 맞다.
    # f1 = open('ftext.txt', encoding = 'utf-8')                          #이렇게 써도 된다.
    f1 = open('ftext.txt', mode = 'r', encoding = 'utf-8')                #이게 제일 맞다. mode는 'r', 'w', 'a', 'b'등이 있다 
    print(f1)               #이건 객체이다.                                   read write append binary 등등
    print(f1.read())
    f1.close()
    
    print('파일 저장 ----------------')
    f2 = open('ftext2.txt', mode = 'w', encoding = 'utf-8')
    f2.write('내 친구들 \n')
    f2.write('홍길동, 한국인 \n')
    f2.close()
    print('파일 저장 완료')

    f3 = open('ftext2.txt', mode ='a', encoding = 'utf-8')
    f3.write('\n사오정')
    f3.write('\n저팔계')
    f3.write('\n손오공')
    f3.close()
    print('파일 저장 성공')

    f4 = open('ftext2.txt', mode = 'r', encoding = 'utf-8')
    print(f4.read())
    f4.close()
except Exception as e:
    print('파일 처리 오류 : ', e)