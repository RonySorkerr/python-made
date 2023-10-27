'''fahrenheit = float(input("Please inter the fahrenheit temperature"))
celcius = (fahrenheit - 32)/1.8
print('%0.1f degree fahrenheit is = %0.1f degree celsius' % (fahrenheit, celcius))
'''
'''fahrenhiet = float(input("Enter the fahrenheit : "))
celsius = (fahrenhiet-32)/5.9
print(celsius)'''
#making an age calculator
byear = int(input("Please enter the year you bornt : "))
bmonth = int(input("Please enter the month you bornt : "))
bday = int(input("Please enter your birth date : "))
pyear = int(input("Please enter the current year : "))
pmonth = int(input("Please enter the current month : "))
pday = int(input("Please enter the current day : "))
year = pyear-byear
month = pmonth-bmonth
day = pday-bday
print("You are ", year , "years " , month , "months and " , day , "days old")