from abc import *

class Employee(metaclass = ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai

    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def data_print(self):
        pass
    def irumnai_print(self):
        print(f'이름 : {self.irum}, 나이 : {self.nai}',end = ', ')


class Temporary(Employee):
    def __init__(self, irum, nai, day, don):
        self.irum = irum
        self.nai = nai
        self.day = day
        self.don = don
        self.pay()
        self.irumnai_print()


    def pay(self):
        self.ildang = self.day * self.don


    def data_print(self):
        print('월급 : ', self.ildang)


class Regular(Employee):
    def __init__(self, irum, nai, salary):
        self.irum = irum
        self.nai = nai
        self.salary = salary
        self.irumnai_print()

    def pay(self):
        pass

    def data_print(self):
        print(f'급여 : {self.salary}')

class Salesman(Regular):
    def __init__(self, irum, nai, salary, sil, susu):
        self.irum = irum
        self.nai = nai
        self.salary = salary
        self.sil = sil
        self.susu = susu
        self.irumnai_print()
        self.pay()

    def pay(self):
        self.su = self.salary + (self.sil * self.susu)

    def data_print(self):
        print('수령액 :',int(self.su))

t = Temporary('홍길동', 25, 20, 15000)
t.data_print()
r = Regular('한국인', 27, 3500000)
r.data_print()
s = Salesman('손오공', 29, 1200000, 5000000, 0.25)
s.data_print()














#일수와 일당은 안넘기고 계산 이름 나이는넘김
#이름 나이는 추클에서 함
#계산은 pay가 함
#출력은 다 data print 다 오버라이딩 해줘야 한다.
#템포러리는 이름나이 월급 찍고 싶음 