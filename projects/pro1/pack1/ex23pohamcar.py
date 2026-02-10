#여러 개의 부품 객체를 조립해서 완성차 생서
#클래스의 포함 관계 사용
#다름 클래스를 마치 자신의 멤버처럼 선언하고 사용

from ex23pohamhandle import PohamHandle

class PohamCar :
    turnShowMessage = "정지"

    def __init__(self, ownerName):
        #ownerName = ownerName              ##이거랑은 완전히 다른 것이다
        self.ownerName = ownerName
        self.handle = PohamHandle()         ##클래스의 포함관계 전형적인 모습

    def turnHandle(self, q) :
        if q > 0 :
            self.turnShowMessage = self.handle.rightTurn(q)

        elif q < 0 :
            self.turnShowMessage = self.handle.leftTurn(q)

        elif q == 0 :
            self.turnShowMessage = '직진'

if __name__ == '__main__' :
    tom = PohamCar('미스터 톰')
    tom.turnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + ' ' + str(tom.handle.quantity))

    john = PohamCar("미스터 존")
    john.turnHandle(-10)
    print(john.ownerName + '의 회전량은 ' + john.turnShowMessage + ' ' +str(john.handle.quantity))

    john = PohamCar("미스터 존")
    john.turnHandle(0)
    print(john.ownerName + '의 회전량은 ' + john.turnShowMessage + ' ' +str(john.handle.quantity))