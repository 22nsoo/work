# 클래스의 다중 상속
# 부모가 두명 이상이다.
# 호랑이랑 사자랑 결혼해서 아이를 낳았다. 타이거의 기능도 갖고 라이언의 기능도 갖는다.

class Tiger:
    data = '호랑이 세계'


    def cry(self):
        print('호랑이 : 어흥!')


    def eat(self):
        print('맹수는 고기를 좋아함')

class Lion:
    def cry(self):
        print('사자 : 으르렁!')

    def hobby(self):
        print('백수의 왕 낮잠은 취짐')


class Liger1(Tiger, Lion):                  ##다중 상속
    pass

a1 = Liger1()
print(a1.data)
a1.eat()
a1.hobby()
a1.cry()                                    ##어흥이 나온다. 먼저 적어주는 애의 멤버를 우선적으로 취한다.
print('----------------')
class Liger2(Lion, Tiger):
    data = '라이거 만세' 

    def ply(self):
        print('라이거 고유 메소드')

    def hobby(self):                        ##메소드 오버라이드
        print('라이거는 공원 걷기를 좋아함')

    def showData(self):
        self.hobby()
        super().hobby()
        self.eat()
        super().eat()
        print(self.data + ' ' + super().data)

a2 = Liger2()
a2.cry()
a2.showData()