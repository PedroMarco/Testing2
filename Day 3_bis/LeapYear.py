# Receive an input
year = eval(input("Enter a year number!: "))
if year %4 == 0 and year %100 !=0:
    print('year '+str(year) + ' is a leap year')
else:
    print('year ' +str(year) + ' is not a leap year')