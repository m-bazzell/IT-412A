#chapter 6 Try it Yourself Ex

#6-1
first_name = "Mindy" 
last_name = "Bazzell" 
age = 35
city = "Eastpointe" 

person = ({"First Name ": first_name, "Last Name ": last_name, "Age ": age, "City ": city })


print(person)

#6-7
people = {'mbazzell ': {"First ": 'Mindy', "Last ": 'Bazzell', "Age ": 35, "Location ": 'Eastpointe'}, 'gbazzell ': {"First ": 'George', "Last ": 'Bazzell', "Age ": 59, "Location ": 'Eastpointe'}, 'EMearse ': {"First ": 'Elizabeth', "Last ": 'Mearse', "Age ": 12, "Location ": 'Valparaiso'}, 'bbazzell ': {"First ": 'Brian', "Last ": 'Bazzell', "Age ": 30, "Location ": 'Ann Arbor'},  'dbazzell ': {"First ": 'Devin', "Last ": 'Bazzell', "Age ": 28, "Location ": 'Southfield'}}

for username, user_info in people.items(): 
    print("\nUsername: " + username)
    full_name = user_info["First "] + "  " + user_info["Last "]
    age = user_info["Age "]
    location = user_info['Location ']
    
    print("\tFull Name: " + full_name.title())
    print("\tAge " + str(age))
    print("\tLocation " + location)


#6-8
pets = {"G'Kar": {"Owner ": 'Mindy', "Kind ": 'cat'},
       "Na'torh": {"Owner ": 'Mindy', "Kind ": 'cat'}, "Dewey": {"Owner ": 'Devin', "Kind ": 'cat'}}

for pet, pet_info in pets.items():
    print("\nPet Name : " + pet)
    pet_owner = pet_info["Owner "]
    pet_type = pet_info["Kind "]

    print("\tPet Owner: " + pet_owner)
    print("\tPet Kind: " + pet_type)

#6-9 
#make a dictionary callled favorite_places. Think of three names to use as keys in the dictionary, and store on to three favorite plaes for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person's names and their favorite places. 

favorite_places = {"Mindy": {"1st Place ": 'Gettysburg', "2nd Place ": 'Traverse City', "3rd Place ": "Marine City"}, "George": {
    "1st Place ": 'Traverse City', "2nd Place ": 'London', "3rd Place ": "Hawaii"}, "Jean ": {"1st Place ": 'Northern Minnesota', "2nd Place ": 'Lake St Helen', "3rd Place ": "Washington D.C "}}

for places, favorite_info in favorite_places.items():
    print("\n Name : " + places)
    favorite_1st = favorite_info["1st Place "]
    favorite_2nd = favorite_info["2nd Place "]
    favorite_3rd = favorite_info["3rd Place "]
    
    print("\t1st Place : " + favorite_1st)
    print("\t2nd Place:  " + favorite_2nd)
    print("\t3rd Place: " + favorite_3rd)
