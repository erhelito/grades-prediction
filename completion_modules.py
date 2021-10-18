import pandas

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