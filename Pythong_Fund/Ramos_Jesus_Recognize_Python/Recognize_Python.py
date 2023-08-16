num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #data type primitive boolean
string = 'Hello World' #data type string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuples
print(type(fruit)) #tupple access value
print(pizza_toppings[1]) #list access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #dictionary access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #NameError: name <variable name> is not defined
print(fruit[2]) #tuple access value

if num1 > 45: #conditionale if 
    print("It's greater") 
else: #conditional else
    print("It's lower")

if len(string) < 5: #conditional if <<>> NameError
    print("It's a short word!")
elif len(string) > 15: #conditional else if
    print("It's a long word!")
else: #conditional else
    print("Just right!")

for x in range(5): #for loop start
    print(x)
for x in range(2,5): #for loop start|stop
    print(x)
for x in range(2,10,3): #for loop start|stop|increment
    print(x)
x = 0 #variable declaration
while(x < 5): #while loop start
    print(x)
    x += 1 #while loop increment

pizza_toppings.pop() #pops last item in list
pizza_toppings.pop(1) #pops item in index 1

print(person)
person.pop('eye_color') #pops eyecolor in dictionary
print(person)

for topping in pizza_toppings:  #for loop start
    if topping == 'Pepperoni': #conditional if
        continue #continue
    print('After 1st if statement')
    if topping == 'Olives': #IndentationError
        break #beark

def print_hello_ten_times(): #function
    for num in range(10): #for loop start
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #function parameter
    for num in range(x): #for loop with parameter
        print('Hello')

print_hello_x_times(4) #4 is the parameter

def print_hello_x_or_ten_times(x = 10): #functino with parameter variable defined
    for num in range(x): #for loop start with parameter
        print('Hello')

print_hello_x_or_ten_times() #Function called 
print_hello_x_or_ten_times(4) #function called


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)