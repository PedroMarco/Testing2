__author__ = 'acpb859'
import random

# Define 1 random 2 digit number. Ask for it and give prices

number1 = str(random.randint(1,9))
number2 = str(random.randint(1,9))

lotto = number1,number2

request1 = str(input('Insert a number: '))
request2 = str(input('Insert a number: '))

result = request1, request2

if(lotto == result):
    print('Congrats, your price is 1000€')