#Check whether the given year is leap or not using functions

def is_leap(year):

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
     return true
    else:
        return false
    
year = int(input("Enter the year: "))
print(is_leap(year))

