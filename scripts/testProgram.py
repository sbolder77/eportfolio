from datetime import date

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

birthName = input('Enter your name: ')

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

myage = Age(birthDay, birthMonth, birthYear, birthName)
myage.ageData()