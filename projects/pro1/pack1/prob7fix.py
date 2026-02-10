# from abc import *

# class Employee(metaclass = ABCMeta):
#     def __init__(self, irum, nai):
#         self.irum = irum
#         self.nai = nai

#     @abstractmethod
#     def pay(self):
#         pass
#     @abstractmethod
#     def data_print(self):
#         pass
#     def irumnai_print(self):
#         print(f'이름 : {self.irum}, 나이 : {self.nai}',end = ', ')


# class Temporary(Employee):
#     def __init__(self, irum, nai, day, don):
#         Employee.__init__(self, irum, nai)
#         self.day = day
#         self.don = don


#     def pay(self):
#         return self.day * self.don


#     def data_print(self):
#         super().irumnai_print()
#         print(', 월급 : '+str(self.pay()))


# class Regular(Employee):
#     def __init__(self, irum, nai, salary):
#         Employee.__init__(self, irum, nai)
#         self.salary = salary


#     def pay(self):
#         pass

#     def data_print(self):
#         super().irumnai_print()
#         print(f'급여 : {self.salary}')

# class Salesman(Regular):
#     def __init__(self, irum, nai, salary, sil, susu):
#         Employee.__init__(self, irum, nai)
#         Regular.__init__(self, irum, nai ,salary)
#         self.sil = sil
#         self.susu = susu

#     def pay(self):
#         return super().pay() + (self.sil * self.susu)

#     def data_print(self):
#         super().irumnai_print()
#         print(', 수령액 : '+str(self.pay()))

# t = Temporary('홍길동', 25, 20, 15000)
# t.data_print()
# r = Regular('한국인', 27, 3500000)
# r.data_print()
# s = Salesman('손오공', 29, 1200000, 5000000, 0.25)
# s.data_print()


#일수와 일당은 안넘기고 계산 이름 나이는넘김
#이름 나이는 추클에서 함
#계산은 pay가 함
#출력은 다 data print 다 오버라이딩 해줘야 한다.
#템포러리는 이름나이 월급 찍고 싶음 

# 추상 클래스 연습문제
from abc import *

class Employee(metaclass=ABCMeta):  # 추상클래스
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai

    @abstractmethod
    def pay(self):     #추상메소드
        pass

    @abstractmethod
    def data_print(self):     #추상메소드
        pass

    def irumnai_print(self):  # 이름, 나이 출력용
        print('이름:' + self.irum + ', 나이:' + str(self.nai), end=' ')

class Temporary(Employee):
    def __init__(self,irum,nai,ilsu,ildang):
        Employee.__init__(self, irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang

    def pay(self):
        return self.ilsu * self.ildang
        
    def data_print(self):
        super().irumnai_print()
        print(', 월급: ' + str(self.pay()))

t = Temporary('홍길동',25,20,150000)
t.data_print()


class Regular(Employee):
    def __init__(self,irum,nai,salary):
        super().__init__(irum,nai)
        self.salary = salary

    def pay(self):
        return self.salary 
        
    def data_print(self):
        super().irumnai_print()
        print(', 급여: ' + str(self.pay()))

r = Regular('한국인', 27, 3500000)
r.data_print()


class Salesman(Regular):
    def __init__(self,irum,nai,salary,sales,commission):
        super().__init__(irum,nai,salary)
        self.sales = sales
        self.commission = commission

    def pay(self):
        return super().pay() + (self.sales * self.commission)

    def data_print(self):
        super().irumnai_print()
        print('수령액: ' + str(round(self.pay())))

s = Salesman('손오공',29,1200000, 5000000, 0.25)
s.data_print()