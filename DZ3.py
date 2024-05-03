from random import randint
import  time

class Math:
    def __init__(self, number1, number2, number3):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3

    def edit(self):
        prnt = True
        pop = input()
        while prnt == True:
            GG_1 = randint(1, 4)
            if GG_1 == 1:
                self.number1 += randint(1, 9)
            elif GG_1 == 2:
                self.number1 -= randint(1, 9)
            elif GG_1 == 3:
                self.number1 *= randint(1, 9)
            elif GG_1 == 4:
                self.number1 /= randint(1, 9)

            GG_2 = randint(1, 4)
            if GG_2 == 1:
                self.number2 += randint(1, 9)
            elif GG_2 == 2:
                self.number2 -= randint(1, 9)
            elif GG_2 == 3:
                self.number2 *= randint(1, 9)
            elif GG_2 == 4:
                self.number2 /= randint(1, 9)

            GG_3 = randint(1, 4)
            if GG_3 == 1:
                self.number3 += randint(1, 9)
            elif GG_3 == 2:
                self.number3 -= randint(1, 9)
            elif GG_3 == 3:
                self.number3 *= randint(1, 9)
            elif GG_3 == 4:
                self.number3 /= randint(1, 9)

            if pop == 'print':
                prnt = False
                break

        if prnt == False:
            print(self.number1)
            print(self.number2)
            print(self.number3)


Numbers = Math(number1=5, number2=8, number3=9)

Numbers.edit()