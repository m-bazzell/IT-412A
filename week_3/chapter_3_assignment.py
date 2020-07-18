#Week 2 Assignment

data_list = [1121, "Jackie Grainger", 22.22, 1122, "Jignesh Thrakkar", 25.25, 1127, "Dion Green", 28.75, False,
             24.32, 1132, "Jacob Gerber", "Sarah Sanderson", 23.45, 1137, True, "Brandon Heck", 1138, 25.84, True,
             1152, "David Toma", 22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 1121, 22.22, False,
             22.65, 1152, "David Toma"]

#Lists that are being used through out this program
employee_numbers = []
employee_names = []
employee_salary = []
total_hourly_rate = []
underpaid_salaries = []
company_raises = []
int_list = []
float_list = []
bool_list = []
something_else_list = []
final_list = []

#this for loop nested with if/elif loops sort the data_list into separate lists;
for data in data_list:
    if data not in employee_names and data not in employee_numbers and data not in employee_salary:
        if type(data) is float:
            employee_salary.append(data)
        elif type(data) is int:
            employee_numbers.append(data)
        elif type(data) is str:
            employee_names.append(data)

#these are the separate lists that the information as it was sorted.
print(employee_names)
print(employee_numbers)
print(employee_salary)

#multiplies employee salary by 30%
for salary in employee_salary:
    total = salary * 1.3
    total_hourly_rate.append(total)

#printing out budget concern for max salary
if max(total_hourly_rate) > 37.30:
    print(str(max(total_hourly_rate)) + ' Total Salary is of budget concern ')

print(total_hourly_rate)

#for loop for sorting total hourly rate into a new list if it matches the range listed.
for rate in total_hourly_rate:
    if rate >= 28.15 and rate <= 30.65:
        underpaid_salaries.append(rate)

print(underpaid_salaries)

#checks the range of the salaries and multiplies it to the according to the specific percentages
for total in employee_salary:
    if total >= 22 and total <= 24:
        salary = total * 1.05
        company_raises.append(salary)
    elif total > 24 and total <= 26:
        salary = total * 1.04
        company_raises.append(salary)
    elif total > 26 and total <= 28:
        salary = total * 1.03
        company_raises.append(salary)
    elif total > 28:
        salary = total * 1.02
        company_raises.append(salary)


print(company_raises)

#sorts the data_list into separate lists per type.
for data in data_list:
    if type(data) is int:
        int_list.append(data)
    elif type(data) is float:
        float_list.append(data)
    elif type(data) is bool:
        bool_list.append(data)
    else:
        something_else_list.append(data)


final_list.append( {"Employee Numbers ": employee_numbers, "Employee Names ": employee_names, "Employee Salaries ": employee_salary, "Total Hourly Rate ": total_hourly_rate, "Employee Raises ": company_raises})
print(final_list)
#print("This is the list of integers:" + str(int_list) 
#      " This is the list of floats: " + str(float_list) + " This is the list of booleans: " + str(bool_list) + " This is the list of something else: " + str(something_else_list))

