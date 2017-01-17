import random
name = input("What would you like?")
dishes_list = name.split(',')
dishes_list =[x.strip() for x in dishes_list]
dish_dict = {a:random.randint(0,100) for a in dishes_list}
for key, value in dish_dict.items():
    print ("%s \t \t %s" % (key, value))
