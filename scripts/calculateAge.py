from datetime import date

# Loops to allow users to enter their birthdate
# each loop will force user to only enter numerical values
# representing their day, month and year of birth
while True:
    try:
        birthDay = int(input('Enter your birth day (numeric): '))
        break
    except ValueError:
        print("Please input integer only...")
        continue

while True:
    try:
        birthMonth = int(input('Enter your birth month (numeric): '))
        break
    except ValueError:
        print("Please input integer only...")
        continue

while True:
    try:
        birthYear = int(input('Enter your birth year (numeric): '))
        break
    except ValueError:
        print("Please input integer only...")
        continue

# Variable to hold the users name
birthName = input('Enter your name: ')

# Class to hold values for personal data
# with method to calculate the age in years of the user
class Age:

    def __init__(self, day, month, year, name):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        self.name = name.upper()
    
    def ageData(self):
        _today = date.today()
        _age = _today.year - self.year - ((_today.month, _today.day) < (self.month, self.day))
        print(self.name + " - you are: " + str(_age) + " years old")

# New object of the Age class
myage = Age(birthDay, birthMonth, birthYear, birthName)

# Call to class method to display the calcualted age in years of the user
myage.ageData()
