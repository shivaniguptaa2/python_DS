class Animal:
    def __init__(self):
        pass

    def breath(self):
        print('Inhale Exhale')
    
    def walk(self):
        print('Walking')
    
class Fish(Animal):
    def __init__(self):
        super().__init__() #The call to super() in the initialiser is recommended, but not strictly required.

    def swim(self):
        print('Swim in water')
    
    def breath(self):
        super().breath()
        print('Breath under water!')


animal = Animal()
animal.breath()
fish = Fish()
fish.walk()
fish.swim()