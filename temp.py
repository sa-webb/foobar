#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(
        open(csv_file_location), dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list


employee_list = read_employees('./employees.csv')

l = len(employee_list)

departments = []
usernames = []
full_names = []


for i in range(0, l):
    values = employee_list[i].values()
    for i in range(0, 3):
        if i == 0:
            departments.append(values[i])
        if i == 1:
            usernames.append(values[i])
        if i == 2:
            full_names.append(values[i])

result = []

for i in range(0, l):
    temp_dict = {
        'Department': departments[i], 'Username': usernames[i], 'Full Name': full_names[i]}
    result.append(temp_dict)

print(result)

new_list = []
for i in employee_list:
    print(employee_list[0])
    # print(i)
print(len(employee_list))
print(new_list)


def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
        department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(
            department_name)
    return department_data


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()


employee_list = read_employees('../data/employees.csv')
dictionary = process_data(employee_list)
write_report(dictionary, '../data/report.txt')
