__author__ = 'acpb859'
import random

# Define 1 random 2 digit number. Ask for it and give prices

number1 = str(random.randint(10,99))
number1a = number1[:1]
number1b = number1[1:]


request1 = str(input('Insert a 2 digit number: '))
request1a = request1[:1]
request1b = request1[1:]



if(request1 == number1):
    print('Congrats, your number is the lotto one, and your price is 10000£')
elif(request1a == number1a or request1a == number1b) and (request1b == number1a or request1b == number1b):
    print('Congrats, your numbers are the lotto ones, but not in order, still win 3000£ though')
elif(request1a == number1a or request1a == number1b) or (request1b == number1a or request1b == number1b):
    print('Congrats, you got a number right, and win 1000£')
else:
    print('You win NOTHING!')