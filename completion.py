import csv

grade_for_estimating = []
list_

with open("notes.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        grade_for_estimating.append(row[3])
        
del grade_for_estimating[0] #delete the label of the column
liste_matieres.sort()

previous_element = ""

for element in liste_matieres :
    print(element)
    if element == previous_element :
        liste_matieres.remove(element)

    previous_element = element

print(liste_matieres)