'''
print("Hi Barak")
print('8'* 10)
'''
'''
#using variables
#Program to check in a patient to a hospital
name = "John Smith"
age=20
new_patient=True
'''
'''
name=input("whats yor name:")
colour=input("whats your fav colour?")
print(" Hi ",name,colour," is your lucky colour! ")
'''
'''
#Type conversion
birth_year=(input("Enter your birth year:"))
age= 2025 - int(birth_year)
print(age)
'''
'''
#how to print characters in python
Characterss = 'Asap Rocky'
print(Characterss[0])
print(Characterss[-1])
print(Characterss[0:5])
name = 'jennifer'
print(name[1:-1])#the answer is ennife
'''
'''
#the len function
course = 'Python for beginners'
print(len(course))#answer is the total no of characters which is 20
print(course.upper())# . is a special function bcoz it refers to specific characters thus its called a method.in this case its upper case
#for all the characters you can try w 0 or 1
print(course.replace('P'), ('J') )#replaces capital P with J there are many other types of . method other than eg upper lower replace
'''
'''
#some other math functions
x = -2.9
print(abs(x))#Absolute makes the number +ve so ans =2.9
y=2.7
print(round(y))#round is a rounding off function so its 3
'''
'''
#if statements built on conditions
is_hot = False
is_cold = False

if is_hot:
    print("its a hot day")
    print("Drink plenty of water ") 
elif is_cold: 
    print("Its a cold day")
    print("Wear Warm clothes")
       
else:
          
    print("its a lovely day")
    
good_credit = False



if good_credit:
    print(' Hello your down payment is ',0.1*1000000,'Usd')
else :
    print('Hello your down payment',0.2*1000000,'Usd')
    '''
'''
#Logical operators used in situations w multiple conditions
#AND,OR,NOT Logical operators
has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:#Both conditions must be true for python to run
    print("eligible for loan")
 
if has_high_income or has_good_credit:#Only one of the conditions must be true for python to run
    print("eligible for loan")
    '''
'''
has_high_income = True
has_criminal_record = True
#so basically the not operator changes the bool of the variable next to it to the opposite of what it is ie true becomes fals
if has_high_income and not has_criminal_record:
    print("Eligible for loan")
else:
    print("not eligible")
    '''
'''
    #Comparison Operators
temperature = 35

if temperature > 30:
    print("its a hot day") 
else:
    print("cool day")       
    
name = "j"
if len(name) < 3:
     print('name must be atleast 3 characters')
elif len(name) > 50:
    print('Name max of 50 letters')  
else:
    print('looks good') 
    ''' 
'''     
#while loops    they are used to execute  a block of code multiple times
#starts with wile then the condition yo want to be repeated.
#while condition
guess_count=1
while guess_count <= 5:
    print('*' * guess_count)
    guess_count = guess_count + 1
print('done')

secret_number =  9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_count = int(input('Guess: '))
    guess_count += 1
    if guess_count == secret_number:
        print("you won!")
        break
else:print('sorry you failed') 
'''
''''
#For loops iterates each character in a string
#for item in ' "string":
#   print(item)
for item in [1,2,3]:
    print(item)
for item in range(10):# we use the range function if we wanna like write out many nos in a rane
    print (item)   
for item in range(5, 10, 2):#meansfive to ten but now we skip two numberscoz of the 2 now output is 5,7,9
    print(item)
    '''
'''
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        print("car")
    else:
        print(fruit)
        '''
'''
# Program to find the sum of all numbers stored in a list
# List of numbers
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# variable to store the sum
sum = 0
# iterate over the list
for val in numbers:
    sum = sum+val
print("The sum is", sum) 
'''
'''
def tonyy(age):
    """
This function tells a person his age by including 
the value in the parameter to a statement

    """
    print('Your age is', tonyy)
tonyy('21')
'''
  #to forc erange funvtion to print out the numbers in the range use list() function        

    
     
     


       
    
    