import csv

with open('conditions.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    categorized_conditions = []
    condition_names = []
    condition_type = []
    for i in csv_reader:
        categorized_conditions.append(i)
        condition_names.append(i[0])
        if i[1] in condition_type:
            continue 
        else: 
            condition_type.append(i[1])
print(categorized_conditions)