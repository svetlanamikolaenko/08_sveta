import random

class Dish(): #(object)
    register = [] 
    
    def __new__(cls, name):
        name = name.strip().capitalize()
        if name:
            if name not in cls.register:
                cls.register.append(name)
                return super().__new__(cls)  #(Dish, cls)
        
    def __init__(self, name):
        self.name = name.strip().capitalize()
        self.cook_time = self.calc_time()
        
                            
    def calc_time(self):
        return str(random.randint(0, 200))

    def print_dish_time(self):
        if self.name:
            print(self.name + "......" + self.cook_time + "min")

   

unsplit_list = input("What would\n ")  # "str"
if not unsplit_list.strip():
    print ("The input is empty")
else:   
    split_list = unsplit_list.split(',')  # [] 
    dish_list = [Dish(dish_name) for dish_name in split_list ] # [Dish, Dish, ...]
    dish_list = [d for d in dish_list if d]
    for elem in dish_list:
        elem.print_dish_time()
    
