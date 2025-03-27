'''
a =int(input('Enter a number: '))
if a < 0:
    print('The number is positive')


b =int(input('Enter another number: '))
if b < 0:
    print('The number is positive')

c =int(input('Enter another number: '))
if c < 0:
    print('The number is positive')
 
s = (a + b + c)/2
area = (s(s-a)*(s-b)*(s-c))**1/2

print(
    'The area of the triangle is', area
)
'''
'''
def car (make, model):
    return f" This is a, {make} specifically, {model}"
    
       
n = car('Toyota', 'Corolla')
print(n)
'''
''''
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.
    
'''
# Given list
numbers = [10, 25, 36, 47, 58, 69]
# Number to find index of
find_num = 47
# Get index if number exists

try:
    index = numbers.index(find_num)
    print(f"The number {find_num} is at index {index}.")
except ValueError:
    print(f"The number {find_num} is not in the list.")