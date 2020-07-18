#chapter 5 Try It Yourself Exercises
#5-1
age = 20

print("Is age == '20'? I predict True")
print(age == 20)

favorite_book = "India"

print("Is my favorite book != 'Database Design'? I predict True")
print(favorite_book != "database design")

favorite_pizzas = ["Everything Pizza", "Pepperoni", "Sausage"]

print("Cheese pizza is one of my favorite pizzas. I predict false")
print("cheese pizza" in favorite_pizzas)

print("Everything Pizza is one of my favorite pizzas. I predict true!")
print('Everything Pizza' in favorite_pizzas)

age = 36
print("Age is not equal to 40. I predict true")
print(age != 40) 

print("Age is less than 12. I predict true")
print(age < 12)

print("Age is greater than 30. I predict true")
print(age > 30)

print("Age is equal to 34. I predict false")
print(age == 34)

print("Age is greater than equal to 40. I predict false")
print(age >= 40)

print("Age is greater than 36. I predict false")
print(age > 36)

#5-2
computer = ["Lenova", "Macbook"]
print(computer == 'lenova')
print(computer != "Macbook Air")

name = "Mindy"
print(name.lower() == 'mindy')

year = 2020 
print(year == 2021)
print(year != 2030)
print(year < 2020)
print(year > 2025)
print(year >= 2020)
print(year <= 2020)

account_number1 = 2016
account_number2 = 2045

#this will read false as neither of these statements are true 
print(account_number1 > 2019 or account_number2 < 2040)

#this will read true because one of the statements is true
print(account_number1 <= 2017 and account_number2 >= 2044)

street_names = ['Piper', 'Beech', 'David']

#This statement will tell me if the street name is in the list or not 
print('Toefer' in street_names)
print('David' in street_names)

#5-3 Alien Colors #1
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print('Player has just earned 5 points.')

if 'purple' in alien_color:
    print()

#5-4 Alien Colors #2
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color: 
    print("Player has just earned 5 points")
else: 
    print('Player has just earned 10 points')

if 'purple' in alien_color:
    print("Player has just earned 5 points")
else:
    print('Player has just earned 10 points')

#5-5 Alien Colors #3 
alien1 = 'yellow'
alien2 = 'green'
alien3 = 'red'
if alien1 == 'green':
    print("player has earned 5 points")
elif alien1 == 'yellow':
    print("player has earned 10 points")
elif alien1 == 'red':
    print('player has earned 15 points')

if alien2 == 'green':
    print("player has earned 5 points")
elif alien2 == 'yellow':
    print("player has earned 10 points")
elif alien2 == 'red':
    print('player has earned 15 points')

if alien3 == 'green':
    print("player has earned 5 points")
elif alien3 == 'yellow':
    print("player has earned 10 points")
elif alien3 == 'red':
    print('player has earned 15 points')


#5-6
age = 35

if age < 2: 
    print('this is a baby')
elif age >= 2 and age < 4: 
    print('this person is a toddler')
elif age >= 4 and age < 13:
    print("this person is a kid")
elif age >= 13 and age < 20: 
    print("this person is a teenager")
elif age >= 20 and age < 65: 
    print("this person is an adult")
elif age >= 60: 
    print("this person is an elder")


#5-7
favorite_fruits = ['Watermelon', 'Strawberry', 'Kiwi']

if 'orange' in favorite_fruits: 
    print("I love oranges")
elif 'Strawberry' in favorite_fruits: 
    print("I love strawberries")
elif 'peaches' in favorite_fruits: 
    print('I love peaches')
elif 'Watermelon' in favorite_fruits: 
    print('I love Watermelon')
elif 'Mangos' in favorite_fruits: 
    print("I love mangos")


#5-8
usernames = ['admin', 'mbazzell' , 'valendiar', 'gbazzell', 'msmearse']

for name in usernames:
    if name == 'admin': 
        print("Hello " + name + " would you like to see a status report")
    else: 
        print("Hello " + name + " thank you for logging in again")


#5-9 
usernames_5_9 = []

if usernames_5_9: 
    for usernames_5_9 in usernames_5_9: 
        print("hello " + usernames_5_9 + ' thank you for logging in again')
else: 
    print("We need to find some users!")

#5-10
current_users = ['admin', 'mbazzell', 'valendiar', 'gbazzell', 'msmearse']
new_users = ['MBadmin', 'mbazzell', 'valendiar', 'spaatz1201', 'earhart12664']

for new_users in new_users: 
    if new_users in current_users:
        print("Please pick a different username " + new_users)
    else:
        print("Username is availabe " + new_users)

#5-11
ordinal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in ordinal: 
    if number == 1: 
        print(str(number) + 'st')
    elif number == 2: 
        print(str(number) +'nd')
    elif number == 3: 
        print(str(number) + 'rd')
    else: 
        print(str(number) + 'th')
