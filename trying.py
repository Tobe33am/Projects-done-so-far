#Welcoming the user to the program
print("Welcome to this Factorial Program")
#Using the input function but making sure that the input data type is an integer
userinput = int(input( " Enter a factorial you would like to evaluate: "))
#Describing the range that i am using to save the userinput number.here i have used the user input as the start of the range and 
#the stop is zero so that the last value is 1.-1 is the step as the inputed no reduces by -1
rangename4theinputfactorial = range(userinput,0,-1)
#i have made this variable to store the current value of the loop after it runs
factorial_answer = 1
#Here i have used the for loop to help calculate the factorial everytime the loop runs the factor is multiplied by the value of 
#variable factorial_answer
for factors in rangename4theinputfactorial:
     factorial_answer*= factors
#finally i have positioned the print function out of the for loop so that the user can only get to see the final answer after the loop runs     
print( 'The factorial of ', userinput,'is',factorial_answer)
#This is a comment to show that I have made a change in this filegit    
    
    