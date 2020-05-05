class Airplane: 
    mark = "TU"
    model = "154"
    year = 1971
    max_speed = "300 km per hour"
    odometr = 0
    is_flying = False
    def __init__(self, way):
        self.way = way
    def take_off(self): 
        self.is_flying = True
        print(f"Двигатель заведен!!! Борт {self.mark} {self.model}, год выпуска {self.year}.")

    def fly(self):
        self.odometr += self.way
        print(f"Мы летим, максимальная скорость: {self.max_speed}, Приятного полета!")

    def land(self): 
        self.is_flying = False
        print(f"Полет на расстоянии: {self.odometr}, длился {self.odometr/300} часов")



r = int(input("Добро пожаловать на самолет! \nВведите расстояние для полета: "))
flight = Airplane(r)
r2 = input("Введите слово <<GO>> для начала полета! ")
if r2.upper() == "GO":
    for i in range(10):
        if i % 2 == 0:
            print("ТРЫХ, ТРЫХ, ТРЫХ")
        else:
            print("ВЖУХ, ВЖУХ, ВЖУХ")
    flight.take_off()
    flight.fly()
    input("Для посадки нажмите любую клавишу: " )

    flight.land()
    
    print("пасибо за выбор нашей компании")

else:
    print("Полет отменен!")

    

