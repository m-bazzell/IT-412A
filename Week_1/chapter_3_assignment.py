# Chapter 3 Try it Yourself Exercises

#3-1
friends = ["Kelly", "George", "Alexandra", "Mallory", "Andy", "Brandon", "Donovan"]

for friend in friends:
    print(friend)

#3-2
friends = ["Kelly", "George", "Alexandra",
           "Mallory", "Andy", "Brandon", "Donovan"]

for friend in friends:
    print("Hello and welcome to It 412, " + friend)

#3-3 
vehicles = ["Corvette", "Jeep Wrangler", "Spyder", "Toyota 4 Runner"]

for vehicle in vehicles:
    print(" I would love to own: " + vehicle)

#3-4
guest_list = ["Buddha", "Abraham Lincoln", "Queen Elizabeth I", "Ellen Degeneras"]

for guest in guest_list:
    print("Please join me at my home for a dinner party "  + guest)

#3-5 

guest_list = ["Buddha", "Abraham Lincoln",
              "Queen Elizabeth I", "Ellen Degeneras"]

for guest in guest_list:
    print("Please join me at my home for a dinner party " + guest)


print(guest_list[1] + " Can't make it to the party")

guest_list.remove("Abraham Lincoln")
guest_list.append("Mary Queen of Scots")

for guest in guest_list: 
    print("Please join me at my home for a dinner party " + guest)

#3-6
for guest in guest_list:
    print("Please join me at my home for a dinner party " + guest)
    print("I have obtained a bigger table to enjoy our dinner " + guest)

guest_list.insert(0, "George Washington")
guest_list.insert(3, "Alexandra")
guest_list.append("Plato")

print(guest_list)

for guest in guest_list:
    print("Please join me at my home for a dinner party: " + guest)

#3-7 
for guest in guest_list:
    print("My new table won't arrive in time so I only have room for two guests at my home: " + guest)
    
for guest in guest_list: 
   popped_guest = guest_list.pop()
   print("I am sorry I will be unable to entertain you at my home " + popped_guest)

for guest in guest_list:
    del guest_list[:] 
    print(guest_list)


#3-8 
places = ["Greece", "Paris", "Italy", "Mount Rushmore", "Ireland", "Belize"]
print(places)

print(sorted(places))

print(places)

print(sorted(places))

print(sorted(places, reverse=True))

print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

#3-9
guest_list = ["Buddha", "Abraham Lincoln",
              "Queen Elizabeth I", "Ellen Degeneras"]

for guest in guest_list:
    print("Please join me at my home for a dinner party " + guest)


print(guest_list[1] + " Can't make it to the party")

guest_list.remove("Abraham Lincoln")
guest_list.append("Mary Queen of Scots")

for guest in guest_list:
    print("Please join me at my home for a dinner party " + guest)

print(len(guest_list))

#3-10
states_lived = ["Arizona", "Missouri" , "California", "Minnesota", "Indiana", "Michigan", "Georgia", "Ohio"]

for state in states_lived:
    print("I have lived in this state: " + state)

states_lived.append("West Virgina")

for state in states_lived:
    print("These are the states I have lived in: " + state)

states_lived.remove("West Virgina")

for state in states_lived:
    print("These are the states I have lived in: " + state)

print(sorted(states_lived))
