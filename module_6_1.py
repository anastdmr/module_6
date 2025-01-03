class Animal:
    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat (self, food):
        if food.check_edible() == 'съедобное':
            print (f'{self.name} съел {food.name}.')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}.')
            self.alive = False

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name
        self.check_edible()

    def check_edible (self):
        ch_edible = ''
        if self.edible:
            ch_edible = 'съедобное'
        else:
            ch_edible = 'несъедобное'
        return ch_edible

class Mammal (Animal):
    pass

class Predator (Animal):
    pass

class Flower (Plant):
    pass

class Fruit (Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

#print (p1.edible)
#print (p2.edible)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)