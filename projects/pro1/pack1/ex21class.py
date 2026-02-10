kor = 100   #모듈의 전역변수

def abc():
    print('모듈의 멤버 함수')

class My :
    kor = 80                        ##함수 내의 지역변수
    
    def abc(self) :
        print('My 멤버 메소드')

    def show(self) :
        ##kor = 77                  ###메소드 내에 지역변수
        print(kor)                  ##메소드 내 지역 변수를 찾고 없으면 모듈의 변수로 간다.
        print(self.kor)             ##함수 내 지역변수가 찍힌다.
        self.abc()                  ##클래스 내부에 있는 함수 호출 가능
        abc()                       ##클래스 외부에 있는 함수 호출 가능



my = My()
my.show()
print('-----'*10)

print(My.kor)
tom = My()
print(tom.kor)
tom.kor = 88
print(tom.kor)

oscar = My()
print(oscar.kor)

