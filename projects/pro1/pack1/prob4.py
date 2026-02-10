# class CoinIn :
#     coin = 0
#     change = 0

#     def putCoin(self) :
#         self.coin = int(input('돈을 넣어주세요 : '))
        
    
#     def selectCof(self, num):
#         self.change = self.coin - 200 * num
#         if self.change > 0 :
#             print(f'커피 {num}잔 출력, 잔돈 {self.change}원을 받아주세요:)')
#         self.change = 0


# class Machine :
#     def actMachine(self):
#         self.machine = CoinIn()
#         self.machine.putCoin()
#         if self.machine.coin >= 200:
#             num = int(input('몇 잔 뽑으실건가요? : '))
#             self.machine.selectCof(num)
        



# M1 = Machine()
# M1.actMachine()



class CoinIn:
    def showData(self, don):
        self.coin = don
        print(f'돈이 {self.coin}원 있습니다.')


    def selectCoffee(self, jan):
        self.change = self.coin - jan * 200


class Machine:
    def __init__(self):
        self.num = int(input('동전을 넣어주세요 : '))
        self.dongto = CoinIn()
        self.dongto.showData(self.num)
        
        if self.dongto.coin >= 200:
            self.jan = int(input('\n몇잔을 뽑으시겠습니까? : '))
            if self.dongto.coin >= 200 * self.jan :
                self.dongto.selectCoffee(self.jan)
                print(f'\n커피 {self.jan}을 뽑으셨습니다. 잔돈 {self.dongto.change}를 받아가세요 :)')
                self.dongto.change = 0
        else: print('돈이 부족합니다.')

M1 = Machine()

# print('-----'*100)


# class CoinIn:
#     coin = 0
#     change = 0

#     def putCoin(self, don):
#         self.coin = don
#         print(f'돈이 {self.coin}원 있습니다.')


#     def selectCoffee(self, jan):
#         self.change = self.coin - jan * 200


# class Machine:
#     def __init__(self):
#         num = int(input('동전을 넣어주세요 : '))
#         dongto = CoinIn()
#         dongto.putCoin(num)
        
#         if dongto.coin >= 200:
#             jan = int(input('\n몇잔을 뽑으시겠습니까?'))
#             if dongto.coin >= 200 * jan :
#                 dongto.selectCoffee(jan)
#                 print(f'\n커피 {jan}을 뽑으셨습니다. 잔돈 {dongto.change}를 받아가세요 :)')
#                 dongto.change = 0
#         else:
#             print('돈이 부족합니다.')

# M1 = Machine()




