#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
my_cat1 = Cat("jim", 78)
my_cat2 = Cat("john", 80)
my_cat3 = Cat("jack", 99)

print(type(my_cat1))
# 2 Create a function that finds the oldest cat

def find_age(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print("The oldest cat is {} years old ".format(find_age((my_cat1.age,my_cat1.name),(my_cat2.age, my_cat2.name),(my_cat3.age, my_cat3.name))))


### __init__ nethod 

class PlayerCharacter():

    def __init__(self, name, age):
        if age > 18 :
            self.name = name
            self.age = age
    
    def shout(self):
        print('Hi {} and my age is {}'.format(self.name, self.age))

player1 = PlayerCharacter("neethu", 100)
player1.shout()
