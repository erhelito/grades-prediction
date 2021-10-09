import csv

estimated_grades_column = []
subjects_list = []

with open("grades.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        estimated_grades_column.append(row[3])
        subjects_list.append(row[0])
        
    del estimated_grades_column[0] #delete the label of the column

    for grade in estimated_grades_column :

