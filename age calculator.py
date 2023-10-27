'''import calendar
year = int(input("enter the year you want to see the calendar : "))
month = int(input("Enter the month you want to see the calender : "))
day = int(input("Enter the days so that you can see with the days including : "))
print(calendar.month(year,month,day))
'''

'''import calendar

year = int(input("Enter your birth year : "))
month = int(input("Enter your birth month : "))
day = int(input("Enter your birth day : "))

print("you are ", year, "Years ", month, " Months ", day, "Days old")
print("Here is your birth calender")
print(calendar.month(year, month, day))
'''

# So, I have figured out how to make it
'''
1. the year 
2. the month
3. the day is not much necessary
4. print the age in string
5. print the calendar
'''
import math
import calendar
byear = int(input("Enter your birth year : "))
pyear = int(input("Enter the present year : "))
bmonth = int(input("Enter your birht month : "))
pmonth = int(input("Enter the present month : "))
bday = 30
pday = int(input("Enter the presend day : "))
year = pyear-byear
month = abs(pmonth-bmonth)
day = abs(pday-bday)
print("You are " , year , " Years " , month , "Month and " , day , "Days old")
print("Here is your birht calendar")
print(calendar.month(byear,bmonth,bday))
print(calendar.month(pyear,pmonth,pday))
