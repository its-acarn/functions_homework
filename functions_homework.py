#functions

#what is a function?
    #takes input > performs task > returns output
    #two types of functions:
    # 1 - something that performs a task and finishes (i.e. adds to a list)
    # 2 - perform some logic and send back a result

#why do we use functions?
    # - organisation
    # - re-usability (DRY - Dont Repeat Yourself)
    # - abstraction
    # - encapsulation

#creating a function

def greet():
    print("Hey")


#calling a function

greet()


#returning a value from a function

def greet():
    return "Hey"


greeting = greet()
print(greeting)

#returning 'None'
    #'None' is a special object in python. It is returned when a python function does not hit a return statement.

def greet():
    print("Hey")


greeting = greet()
print(greeting)

#parameters and arguments
    #parameters are pieces of information taken in by a function
    
def greet(name):
    return "Hey " + name


greeting = greet("Bob")
print(greeting)

    #when we give the function the information it is called an argument

#multiple parameters
    #functions can take more than one parameter.
    #multiple parameters are seperated by a comma

def greet(name, time_of_day):
    return "Good " + time_of_day + ", " + name


greeting = greet("Bob", "morning")
print(greeting)

#passing variable as arguments
    #so far we've only passed in string values as arguments. We can also pass variables into the arguments.

def greet(name, time_of_day):
  return "Good " + time_of_day + ", " + name


name_1 = "Bob"
time_of_day_1 = "morning"
greeting = greet(name_1, time_of_day_1)
print(greeting)

name_2 = "Ada"
time_of_day_2 = "afternoon"
greeting = greet(name_2, time_of_day_2)
print(greeting)

#scope
    #a function has it's own internal world and does not share it's variables with other functions.

#a more complex example
    #In the example we have a list of chickens and the farmer would like to go through all the chickens, 
    #collecting the eggs and getting the total number of eggs collected:

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

total_eggs = 0

for chicken in chickens:
    total_eggs += chicken["eggs"]
    chicken["eggs"] = 0 # eggs have been collected

print(f"{total_eggs} eggs collected")   

    #This is a good piece of standalone code.
    #However if we got another farms egg data it would not be efficient to write this all out again.
    #Therefore we can make the code become a function as shown below:

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def count_eggs( list ):
    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0 # eggs have been collected

    return f"{total_eggs} eggs collected"


print(count_eggs(chickens))