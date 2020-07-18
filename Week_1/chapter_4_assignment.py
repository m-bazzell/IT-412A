#chapter 4 try it yourself exercises
#4-1 
pizzas = ["Pepperoni Lovers", "Meat Lovers", "Veggie Lovers", "Everything but the kitchen Sink Pizza"]

for pizza in pizzas: 
    print("I absolutely love this type of pizza! " + pizza)

print('I absolutely love pizza of any kind!')


#4-2
animals = ["Dog", "Cat", "Bunny", "Lizard"]

for animal in animals: 
    print(animal)


for animal in animals:
    print( "A " + animal + " would make an absolutely wonderful pet for any child!")

print("All of these animals are considered normal small animal pets for any child.")

#4-3
numbers = range(0,21)

for number in numbers: 
    print(number)

#4-4
number_var = range(0,1000001)

for number in number_var:
    print(number)

#4-5
number_variable = range(1,1000001)
print(min(number_variable))
print(max(number_variable))
print(sum(number_variable))

#4-6
number_variable = list (range(1,21,2))
for number in number_variable:
    print(number)

#4-7
number_three = list(range(3,30,3))

for number in number_three:
    print(number)

#4-8
cube = [value**3 for value in range(1,11)]
for number in cube:
    print("Here is the cube value of each number by 3! " + str(number))

#4-9
cube = [value**3 for value in range(1, 11)]
print(cube)

#4-10
cube = [value**3 for value in range(1, 11)]
for number in cube:
    print("Here is the cube value of each number by 3! " + str(number))

print("Here are the first three values of cubed integers!")
for number in cube[:3]:
    print(number)

print("Here are the middle three values of cubed integers!")
for number in cube[3:6]:
    print(number)

print("Here are the last three values of cubed integers!")
for number in cube[7:10]:
    print(number)

#4-11
friends_pizzas = ["Pepperoni Lovers", "Meat Lovers",
          "Veggie Lovers", "Everything but the kitchen Sink Pizza"]

pizzas = ["Pepperoni Lovers", "Meat Lovers",
          "Veggie Lovers", "Everything but the kitchen Sink Pizza"]

pizzas.append("Sausage")
friends_pizzas.append("Haiwaiin Pizza")

for pizza in pizzas:
    print("My favorite pizzas are: " + pizza)

for pizza in friends_pizzas:
    print("My friends favorite pizzas are: " + pizza)

#4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for food in my_foods: 
    print("Here are my favorite foods: " + food)

for food in friend_foods:
    print("Here are my friends favorite foods: " + food)

#4-13
buffet_food = ('Mac and Cheese', 'Pizza', 'Mashed Potatos', 'Roast Beef', 'Veggies')

#buffet_food.append('Ice Cream')

for food in buffet_food:
    print("These are the items avaialbe to eat: " + food)

buffet_food = ('Fried Chicken', 'Pizza',
               'Mashed Potatos', 'Roast Beef', 'Ice Cream')

for food in buffet_food:
    print('These are the new food items at the buffet:  ' + food)