## 클래스의 상속관계 : 자원의 재활용을 목적으로 특정 클래스의 멤버(속성, 행위)를 가져다 쓰는 것
## 코드 재사용
## 확장성 - 기존 클래스에 새 기능을 추가한 새로운 클래스 생성
## 구조적 설계 - 공통개념은 부모 클래스, 구체적인 내용은 자식 클래스에서 구현
## 다형성 구사 - 메소드 오버라이딩

class Animal:                   ## 동물들이 가져야할 공통 속성과 행위 - Animal:부모, 조상, super, parent
    
    age = 1
    def __init__(self):
        print('Animal 생성자')

    def move(self):
        print('움직이는 생물이다.')

class Dog(Animal):              ## 부모 클래스를 괄호 안에 넣어주면 상속 - Dog:자식, 자손, 파생, sub, child
    def __init__(self):
        print('Dog 생성자')
    
    def my(self):
        print('댕댕이라고 해요')


dog1 = Dog()
dog1.my()
dog1.move()                     ## 처음부터 animal로 가는게 아니라 dog에서 먼저 뒤지고 없으면 animal로 가서 찾음(local - global 관계)
print('age : ', dog1.age)
print()
dog2 = Dog()
dog2.my()
dog2.move()
print()


class Horse(Animal):
    pass


horse1 = Horse()                ## 자식 클래스의 생성자를 실행할때 생성자가 명시적으로 적어지지 않으면, 부모 클래스의 생성자를 수행한다.
horse1.move()



## 강결합 - 상속(유지보수비가 많이 든다.)   But 다형성을 구사할 땐 상속을 쓴다 = 오버라이딩 가능, 다형성은 goat
## 약결합 - 포함(많이 쓴다.)

