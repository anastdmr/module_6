import random
class Animal:
    live = True
    sound = None
    _degree_of_danger = 0
    def __init__(self, speed, _cords = [0, 0, 0]):
        self._cords = _cords
        self.speed = speed

    def move (self, dx, dy, dz):
        if dz * self.speed < 0:
            print ("К сожалению, я не умею копать землю:(")
            self._cords[0] = dx * self.speed
            self._cords[1] = dy * self.speed
        else:
            self._cords[0] = dx * self.speed
            self._cords[1] = dy * self.speed
            self._cords[2] = dz * self.speed

    def get_cords (self):
        print (f'x: {self._cords[0]}, y: {self._cords[1]}, z: {self._cords[2]}')

    def attack (self):
        if self._degree_of_danger < 5:
            print ("Прости, я мирный!")
        else:
            print ("Будь осторожен, я атакую тебя 0_0")

    def speak (self):
        print (self.sound)

class Bird (Animal):
    beak = True

    def lay_eggs (self):
        print ("У меня для тебя есть ", random.randint(1, 4), " яйца!")

class AquaticAnimal (Animal):
    _degree_of_danger = 3

    def dive_in (self, dz):
        self._cords[2] =- (abs(dz)*self.speed)/2

class PoisonousAnimal (Animal):
    _degree_of_danger = 8

class Duckbill (Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()