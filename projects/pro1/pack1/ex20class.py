class Car :
    handle = 1                                  
    speed = 0

    def __init__(self, name, speed):
        self.name = name                        ##현재 객체의 name에게 name(지역변수) 인자값 치환
        self.speed = speed                      ##self가 밑에서는 car1임 그래서 car1.name에 'tom'이 들어가는 것

    def showData(self):                         
        km = '킬로미터'
        msg = '속도 : ' + str(self.speed) + km
        return msg
    
    def printHandle(self) :
        return self.handle                      ##클래스 내 멤버를 부를 땐 self를 붙여야 함 안붙이면 지역변수를 찾음
    

print(Car.handle)                               ##원형(prototype) 클래스의 멤버 호출
car1 = Car('tom', 10)                           ##생성자 호출 후 객체 생성
print('car1 : ',car1.name, ' ', car1.speed, car1.handle)        ##핸들이 __init__에 없음 그래서 핸들이 없는 놈임. 그럼 class내 전역으로 감 따라서 0
print('car1 객체 주소 : ', car1)

car2 = Car('john', 20)                          ##생성자 호출 후 객체 생성
print('car2 : ',car2.name, ' ', car2.speed, car2.handle)        ##항상 지역을 먼저 뒤지고 없으면 전역으로 간다.
print('car2 객체 주소 : ', car2)
#https://seulhee030.tistory.com/56  읽어보기

car1.color = '파랑'
print('car1.color : ', car1.color)               ##car1에 파랑이 추가 됨 기능이 추가가 됨 차에 튜닝하면 나만 가질 수 있는 것

print(id(Car), id(car1), id(car2))
print(car1.__dict__)
print(car2.__dict__)

print('-------메소드----------')
print('car1 speed : ', car1.showData())             ##self는 각자의 주소를 의미한다.
print('car2 speed : ', car2.showData())             ##인터프리터가 car2 객체의 주소를 인수로 자동으로 넣어줌.

car1.speed = 80
car2.speed = 110

print('car1 speed : ', car1.showData())             ##속도 변경
print('car2 speed : ', car2.showData())             ##속도 변경

print('car1 handle : ', car1.printHandle())
print('car2 handle : ', car2.printHandle())         ##로컬(init)을 먼저 뒤지고 없으면 public으로 감(handle)


