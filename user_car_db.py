class car():
    car_brand =''
    car_color = ''
    car_year = ''
    car_price = ''
    def __init__(self, c_brand, c_color, c_year, c_price):
        self.car_brand = c_brand
        self.car_color = c_color
        self.car_year = c_year
        self.car_price = c_price

    def __str__(self):
        print("\tCar Brand: " + str(self.car_brand))
        print("\tCar Color: " + str(self.car_color))
        print("\tCar Year: " + str(self.car_year))
        print("\tCar Price: " + str(self.car_price))
        return ''

    def get_brand(self):
        return self.car_brand


class person(car):
    def __init__(self,p_name, p_car_brand, p_car_color, p_car_year, p_car_price):
        self.p_name =p_name
        super(person, self).__init__(p_car_brand, p_car_color, p_car_year, p_car_price)

    def __str__(self):
        print("")
        print("Person Name: " + str(self.p_name))
        print("persons car details are below")
        super().__str__()
        return ''

    def get_person(self):
        return self.p_name


db = [person('murali','fortuner','white', 2011, '25L'),
      person('krish','skoda','black', 2008, '15L'),
      person('sai','benz','black', 2010, '35L'),
      person('subbu', 'skoda', 'black', 2018, '15L')]

print(db)


while True:
    choice = int(input("\nSelect your choice \n"
                       "1 => To get persons of a car \n"
                       "2 => To get car brand used by a person:\n"))
    if choice == 1:
        car_name = input("Enter the car name/brand: ")
        print("\nPeople having car brand " + str(car_name))
        for p_obj in db:
            if p_obj.get_brand() == car_name:
                print(p_obj.get_person())
    elif choice == 2:
        person_name = input("Enter the person name: ")
        for p_obj in db:
            if p_obj.get_person() == person_name:
                print(p_obj)
