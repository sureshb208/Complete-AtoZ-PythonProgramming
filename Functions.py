
# Creating a siple class and onject function
class myFunction():

    def __init__(self, fname, lastname):
        self.fname = fname
        self.lastname = lastname

    def hello(self):
        print("Hi {} is this your last name {} ?". format(self.fname, self.lastname))


s1 = myFunction("neethu", "Vignesh")
s1.hello()

#Unpack and perform highest value tuple from list of tuples     
my_list = [("john", 1000), ("lisa", 2300),("Ava", 2400)]

def largerthan(my_list):

    max_time = 0
    best_name = ''

    for name, time in my_list:
        if time > max_time:
            max_time = time
            best_name = name
        else :
            best_name = "Phoneix"
            max_time = 1200
    return best_name, max_time

name, time = largerthan(my_list)
print(name, time)

#Dynamically Checking the arugments before passing into the function
def add_numbers(a,b):
    a = int(a)
    b =int(b)
    return str(a + b)

res = add_numbers('66',4.7)
print(res)

#Return True if any number is even inside a list

my_lst =[1,2,4,8,9,12]
### List Comprehension
empty_lst = [j for j in my_lst if j % 2 ==0 ]
print(empty_lst)

def checkeven_number(my_lst):
    empty_lst = []
    for i in my_lst:
        print(i)
        if i % 2 == 0 :
            empty_lst.append(i)
        else :
            pass #return "No Even Number"
    return empty_lst

result = checkeven_number(my_lst)
print(result)

#parameter and Arguments

#parameters while defining the function
def hello_name(name, age):
    return 'Welcome ' +name+ ' your age is ' +str(age)+ '. Have a nice time.'  #here name and age is variable

#here it is arguments or invoking or calling the function
print(hello_name("neethu", 27))


#Default parameter and keyword arguments
def hello_name(name="joey", age=78):
    return 'Welcome ' +name+ ' your age is ' +str(age)+ '. Have a nice time.' 


print(hello_name("chandler", 77))
print(hello_name("monica", 79))
print(hello_name("phoebe")) #default parameter
print(hello_name(age= 27, name="rachel"))  #keyword arguments
print(hello_name())


#Problem Practice:
#age = input("What is your age?: ")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.


def checkDriverAge(age =0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

print(checkDriverAge(92))


#Methods Vs Functions

#docstrings

def test_a(a):
    '''
    This function describes about the parameter a

    '''
    return a

print(test_a('((((ppp)))'))

#*args, **kwargs

def super_func(*args, **kwargs):
    print(args)
    total = 0
    for i in kwargs.values():
        total += i

    return sum(args) + total

print(super_func(1,2,3,45,55, num=11, num2 = 77))



def highest_even(li):
    li = sorted(li)
    lst = []
    for i in li:
        if i%2 == 0:
            lst.append(i)
    return (lst)[-1]


print(highest_even([10000,13,-19,30,100]))


#Walrus Operator :=

#Scope - What variables do I have access to ?
#who has access to who?


#Global keyword
#nonlocal keyword









