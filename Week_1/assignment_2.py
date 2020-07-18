#list of all the courses I have been required to take at Walsh College
courses = ["acc 300", "ecn 201", "mgt 201", "com 300", "com 210", "it 201", "it 402", "qm 301"]

courses.sort()

#Looping thorugh the courses and marking them  with I have taken message. Also converting courses to caps
for course in courses:
    message = "I have taken "
    message_1 = " at Walsh College"
    course_print = message + course.upper() + message_1 
    print(course_print)

#Upcoming courses and merging two lists into one complete list 
courses_upcoming = ["com 340","it 408", "it 412", "it 417"] 
courses_complete = courses + courses_upcoming 
courses_complete.sort()
print(courses_complete)

#Upcoming courses or courses I am taking right now 
for i in courses_upcoming:
    message_2 = "This is my course of study with upcoming courses added: "
    message_3 = message_2 + i.upper()
    print(message_3)

#clearing the original list of courses that were taken and then marking them as such 
for courses_taken in courses_complete:
   courses.clear() 
   message_4 = "I do not have to take these courses: "
   message_5 = message_4 + courses_taken
   print(message_5)

#Using the list to tell you that i am taking these courses in the upcoming term.
for upcoming in courses_upcoming:
   message_6 = "I plan to take the following courses next term "
   message_7 = message_6 + upcoming
   print(message_7)

#list with numbers in range from 0 to 1000
numbers =list(range(0,1000))

#showing the list of numbers that are divisible by 6 
num = []
for value in range(6,1000,6):
    six =  value 
    num.append(six)
    message_8 = "Here are twenty numbers divisible by 6:"

#printing the first 20 numbers that are divisible  by 6 
print(message_8 , num[0:20])

#max value in the list
print("The maximum value in th list is: "  , max(numbers))

#sum of the number between 10 and 50 
message_9 = "Here is the sum of several values in the list: "
print(message_9 ,sum(numbers[10:50]))

#overwriting my original list of courses with my range of numbers 
courses = numbers
print(courses)