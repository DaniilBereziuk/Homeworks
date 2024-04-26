import random

class Cat:

    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.dexterity = 50
        self.happy = 20
        self.LoveToCat = 100
        self.alive = True

    def to_go_for_a_walk(self):
        print('Cat go for a walk..')
        self.energy -= 2.5
        self.dexterity += 0.5
        self.happy += 0.25
        self.LoveToCat -= 5

    def to_sleep(self):
        print('Cat will sleep')
        self.energy += 1.5
        self.happy += 0.5

    def go_eat(self):
        print('Cat go eat')
        self.dexterity -= 1
        self.LoveToCat += 1.25
        self.energy += 1.5

    def go_fight(self):
        print('Cat find the enemy')
        self.energy -= 5
        self.dexterity -= 2.5
        self.happy -= 2

    def go_to_wash(self):
        print('Family get cat to wash him')
        self.LoveToCat += 2.5
        self.happy -= 1

    def is_alive(self):
        if self.LoveToCat <= 30:
            print('The cat was abandoned...')
            self.alive = False
        elif self.energy <= 10:
            print('The cat is overtired...')
            self.alive = False
        elif self.dexterity <= 5:
            print('It became difficult for the cat to live...')
            self.alive = False
        elif self.happy <= 0:
            print('The cat was very hard...')
            self.alive = False
        elif self.energy > 10:
            print('Passed!')
            self.alive = True

    def end_of_day(self):
        print(f'Energy - {self.energy}')
        print(f'Dexterity - {self.dexterity}')
        print(f'happy - {self.happy}')
        print(f'Love to cat - {self.LoveToCat}')

    def live(self, day):
        day = f'Day {day} of {self.name} life'
        print(f'{day:=^50}')
        cube = random.randint(1,5)
        if cube == 1:
            self.to_go_for_a_walk()
        elif cube == 2:
            self.to_sleep()
        elif cube == 3:
            self.go_eat()
        elif cube == 4:
            self.go_fight()
        elif cube == 5:
            self.go_to_wash()

        self.end_of_day()
        self.is_alive()

Barsik = Cat(name='Barsik')
for day in range(1, 365):
    if not Barsik.alive:
        break
    Barsik.live(day)