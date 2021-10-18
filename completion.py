import pandas
from statistics import mean

reader = pandas.read_csv(r"grades.csv")

def get_subject_with_index(index):
    return reader.Subject[index]

def get_subject_index(subject) :
    grades_index = []

    index = 0
    for subject_label in reader.Subject :
        if subject_label == subject :
            grades_index.append(index)

        index += 1

    return grades_index

def get_list_of_grades(grades_index):
    grades = reader.Grade

    list_of_grades = []
    for index in grades_index :
        list_of_grades.append(grades[index])

    list_of_grades_integer = []
    for grade in list_of_grades :
        try :
            if str(grade) != "nan" :
                list_of_grades_integer.append(float(grade))

        except :
            pass

    return list_of_grades_integer



def get_grades_for_subject(subject):
    grades_index = get_subject_index(subject)
    list_of_grades = get_list_of_grades(grades_index)

    return list_of_grades


def get_human_estimation(index):
    human_estimation = int(reader.Estimated_grade[index])
    return human_estimation


index = 0
for grade in reader.Estimated_grade_by_bot :
    if str(grade) == "nan":
        subject = get_subject_with_index(index)
        print(f"subject to complete : {subject}")

        list_of_grades = get_grades_for_subject(subject)
        print(f"list of grades : {list_of_grades}")

        average = None
        
        try :
            average = mean(list_of_grades)

        except :
            print("There is no grades")

        print(f"average : {average}")


        human_estimation = get_human_estimation(index)
        print(f"estimation : {human_estimation}")

        estimations_list = []

        if average != None :
            estimation1 = ((human_estimation *2)+ average)/3
            estimation2 = (human_estimation + average)/2
            estimation3 = (human_estimation + (average *2))/3

            estimations_list.append(estimation1)
            estimations_list.append(estimation2)
            estimations_list.append(estimation3)

        else :
            estimation1 = "NaN"
            estimation2 = human_estimation
            estimation3 = "NaN"

            estimations_list.append(estimation2)

        estimations_list.sort()

        if len(estimations_list) == 1 :
            print(f"Estimation : {estimations_list[0]}")

            reader.Estimated_grade_by_bot[index] = estimations_list[0]

        else :
            print(f"Low estimation : {estimations_list[0]}")
            print(f"Middle estimation : {estimations_list[1]}")
            print(f"High estimation : {estimations_list[2]}")

            reader.Estimated_grade_by_bot_low[index] = estimations_list[0]
            reader.Estimated_grade_by_bot[index] = estimations_list[1]
            reader.Estimated_grade_by_bot_high[index] = estimations_list[2]

        print("\n")

    index += 1

reader.to_csv("grades.csv", index=False)