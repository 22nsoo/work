class ElecProduct :
    volume = 0

    def volumeControl(self, volume):
        print(f'소리 크기는 {volume}')




class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        print(f'TV의 소리 크기는 {volume}')



class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        print(f'라디오의 소리 크기는 {volume}')



for e in [ElecTv(), ElecRadio()] :
    e.volumeControl(20)



print('----------------------')

class Animal:
    name = '동물'
    def move(self):
        print('동물이 앞으로 이동')


class Dog(Animal):
    name = '개과'
    def move(self):
        print('개가 앞으로 이동')


class Cat(Animal):
    name = '고양이과'
    def move(self):
        print('고양이가 앞으로 이동')

class Wolf(Dog, Cat):
    pass


class Fox(Cat, Dog):
    def move(self):
        print('여우가 앞으로 이동')

    def foxMethod(self):
        print('여우의 method')


for ani in [Dog(), Cat(), Wolf(), Fox()]:
    print('')
    print(ani.name)
    ani.move()
