class Car: 
    mark = "AZLK"
    model = "Troyka"
    year = 1973
    fuel = 70
    odometr = 0
    def __init__(self, way):
        self.way = way
        self.drive()
    
    def drive(self):
        if self.way > 700:
            print("Не хватает бензина!") 
        else:
            self.__add_distance()
            self.__substract_fuel()
            print("lets drive!")
            print(f"Поездка окончаена, израсходовано: {self.way / 10} литров, остаток бензина {self.fuel} литра, вы проехали: {self.odometr} км")             

    def __add_distance(self):
        self.odometr += self.way
    
    def __substract_fuel(self):
        spended_fule = self.way / 10
        self.fuel -= spended_fule

r = int(input("Введите расстояние в км: "))
car1 = Car(r)
