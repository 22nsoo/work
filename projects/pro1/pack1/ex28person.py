# 상속

class Person:
    say = '난 사람이야~~~'                              ##접근 권한 : public
    nai = '20'
    __msg = 'good : private member'                 ##접근 권한 : private

    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai

    def printInfo(self):                                
        print(f'나이:{self.nai}, 이야기:{self.say}')

    def helloMethod(self):
        print('안녕')
        print('hello : ', self.say, self.nai, self.__msg)


print(Person.say, Person.nai)
per = Person('25')
per.printInfo()
per.helloMethod()
print('------'*10)

class Employee(Person):
    subject = '근로자'
    say = '일하는 동물'


    def __init__(self):
        print('Employee 생성자')

    def printInfo(self):
        print('Employee 클래스의 printInfo 호출됨')

    def ePrintInfo(self):
        print(self.subject, self.say, self.nai)       ##self.say, nai는 일단 자식 클래스에서 찾고 없으면 부모클래스로 감
        #print(self.__msg)                            ##에러 뜸 private 멤버이다. 이건 person에서만 유효하다.
        self.helloMethod()
        self.printInfo()
        print(super().say)
        super().printInfo()                           ##super().를 쓰면 무조건 바로 이전 부모를 본다.

emp = Employee()
print(emp.subject, emp.nai, emp.say)                  ##local이 우선이다.
emp.ePrintInfo()

class Worker(Person):
    def __init__(self, nai):        ##부모의 생성자에 nai를 인자로 받기 때문에 nai를 인자로 받음
        print('Worker 생성자')
        super().__init__(nai)       ##부모 클래스의 생성자 호출
    
    def wPrintInfo(self):
        print('Worker - wPrintInfo 처리')
        #self.printInfo()            ##자식의 영역을 뒤지다가 없으면 부모로 감
        super().printInfo()         ##다이렉트로 부모로 감

wor = Worker('30')
print(wor.say, wor.nai)
wor.wPrintInfo()

print('------'*10)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        super().__init__(nai)           #Bound call
        # Worker.__init__(self, nai)    #unbound call

    def pPrintInfo(self):
        print('Programmer - pPrintInfo 처리하였음')

    def wPrintInfo(self):               #부모 메소드와 동일 메소드 선언
        print('Programmer에서 overriding')

    

pro = Programmer(35)
print(pro.say, pro.nai)
pro.pPrintInfo()
pro.wPrintInfo()

print('\n 클래스 타입 확인')
a = 3; print(type(a))
print(type(pro))
print(type(wor))
print(Person.__base__)
print(Worker.__base__)
print(Programmer.__base__)