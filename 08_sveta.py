import random
class DishClass():
    def __init__(self, name):
        self.dish_name = name
name = input("What would you like? ")
dishes_list = name.split(',')
if name.strip() !=(""):
    dishes_list =[x.strip() for x in dishes_list if x.strip()!=("")]#запамятати пусті рядки
    if dishes_list == []:#якщо все ж таки ми ввели пусті рядки, то вивести
        print("Input was empty")
    else:        
        dish_dict = {a.capitalize():random.randint(0,100) for a in dishes_list}#де а -елемент списку, в якому тип кожного елементу стрінг 
        for key, value in dish_dict.items():
            print ("%s \t \t %s" % (key, value))
else:
    print ('No input')
