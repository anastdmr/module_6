class Vehicle:
    color_variants = ['black', 'white', 'green', 'brown']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return print ("Модель: ", self.__model)

    def get_horspower (self):
        return print ("Мощность двигателя: ", self.__engine_power)

    def get_color (self):
        return print ("Цвет: " , self.__color)

    def print_info (self):
        self.get_model()
        self.get_horspower()
        self.get_color()
        print (f'Владелец: {self.owner}')

    def set_color (self, new_color):
        if new_color.lower() in Vehicle.color_variants:
            self.__color = new_color
        else:
            print (f'Нельзя сменить цвет на {new_color}!')

class Sedan (Vehicle):
    __passengers_limit = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')



# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось

vehicle1.print_info()