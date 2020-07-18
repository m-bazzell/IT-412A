#First Name lower case
name_low = " mindy"

#Last name all capilatizes
lastname_cap = " BAZZELL"

#print statement with lower and upper case letters as requested
print("Hello," + name_low.upper() + lastname_cap.lower())

#print statement with new lines
print("Hello," +"\n" + name_low.upper()+"\n" + lastname_cap.lower())

#quote using correction puncuation
quote = "\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible\""

print(quote)

#two decimal values 
decimal_1 = .25
decimal_2 = .87

#addition of the two decimal variables
add = decimal_2 + decimal_1
print(add)

#subtraction of the two decimal variables
sub = decimal_1 - decimal_2
print(sub)

#multiplication of the two decimal variables
multiplication = decimal_1 * decimal_2
print(multiplication)

#division of the two decimal variables 
division = decimal_1 / decimal_2
print(division)

#Month and day of the month statement 
Today  = "\n\t\t Today is day "
month = "June"
day = 30
month_statement = " of the month of "

#concatenating the previous variables and strings into welcome statement 
welcome_statement =  Today + str(day) + month_statement + month  
print( welcome_statement)
