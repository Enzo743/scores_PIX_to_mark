# Projet n°1
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

students_name = []
students_scores = []
students_marks = []


def read():
    file = open('données.csv', encoding="utf8")
    line = file.readline()

    for line in file:
        elements = line.strip().split(';')
        students_name.append(elements[4])
        students_scores.append(int(elements[8]))
    file.close()


def average_score(list):
    sum = 0
    len = 0
    for i in list:
        sum = sum + i
        len = len + 1
    return sum / len


def maximum_score(list):
    max = list[0]
    for i in list:
        if i >= max:
            max = i
    return max


def minimum_score(list):
    min = list[0]
    for i in list:
        if i <= min:
            min = i
    return min


def maths():
    a = (average - 20) / (average_score(students_scores) - maximum_score(students_scores))
    b = 20 - ((average - 20) / (average_score(students_scores) - maximum_score(students_scores))) * maximum_score(students_scores)

    for i in students_scores:
        mark = a * i + b
        students_marks.append(mark.__round__(1))


def graphical():
    ticks = range(0, len(students_name))
    figsize = (11, 9)

    plt.figure(figsize=figsize)
    plt.plot(students_scores, marker="+", linestyle="None", color='blue')
    plt.xticks(ticks=ticks, labels=students_name, rotation='vertical')
    plt.xlabel('Noms des élèves')
    plt.ylabel('Scores')
    plt.title('Scores PIX des élèves')
    plt.show(block=True)
    plt.close()

    plt.figure(figsize=figsize)
    plt.plot(students_marks, marker="+", linestyle="None", color='blue')
    plt.xticks(ticks=ticks, labels=students_name, rotation='vertical')
    plt.xlabel('Noms des élèves')
    plt.ylabel('Notes')
    plt.title('Scores converti en Notes')
    plt.show(block=True)
    plt.close()


average = int(input("Quelle est la moyenne souhaitée ?"))
read()
maths()
graphical()
