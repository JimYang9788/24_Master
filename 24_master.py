import itertools
import math

operation = ["+", "-", "*", "/"]
result = []
for i in operation:
    for j in operation:
        for k in operation:
            result = [i + j + k] + result


def operation(operation, n1, n2):
    if n1 == False or n2 == False:
        return False
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif n2 == 0:
        return False
    else:
        return n1 / n2


def twenty_four():
    set = raw_input("Please enter four numbers: ")
    lon = []
    for i in set.split():
        lon = lon + [float(i)]
    subset = itertools.permutations(lon)
    for each in subset:
        Black(each)


def tol(a, b, tolerance):
    return (abs(a - b)) < tolerance


def Black(lon):
    for collection in result:
        o1 = collection[0]
        o2 = collection[1]
        o3 = collection[2]
        first = lon[0]
        second = lon[1]
        third = lon[2]
        fourth = lon[3]
        if tol(operation(o3, (operation(o2, (operation(o1, lon[0], lon[1])), lon[2])), lon[3]), 24, 0.01):
            print (str(lon[0]) + o1 + str(lon[1]) + o2 + str(lon[2]) + o3 + str(lon[3]))
        if tol(operation(o3, operation(o1, first, (operation(o2, second, third))), fourth), 24, 0.01):
            print (str(lon[0]) + o1 + "(" + str(lon[1]) + o2 + str(lon[2]) + ")" + o3 + str(lon[3]))
        if tol(operation(o2, (operation(o1, first, second)), (operation(o3, third, fourth))), 24, 0.01):
            print (str(lon[0]) + o1 + str(lon[1]) + o2 + "(" + str(lon[2]) + o3 + str(lon[3])) + ")"
        if tol(operation(o1, first, (operation(o3, (operation(o2, second, third)), fourth))), 24, 0.01):
            print (str(lon[0]) + o1 + "(" + "(" + str(lon[1]) + o2 + str(lon[2]) + ")" + o3 + str(lon[3])) + ")"
        if tol(operation(o1, first, (operation(o2, second, (operation(o3, third, fourth))))), 24, 0.01):
            print (str(lon[0]) + o1 + "(" + str(lon[1]) + o2 + "(" + str(lon[2]) + o3 + str(lon[3])) + ")" + ")"
        if tol(operation(o1, first, (operation(o2, second, (operation(o3, third, fourth))))), 24, 0.01):
            print (str(lon[0]) + o1 + "(" + str(lon[1]) + o2 + "(" + str(lon[2]) + o3 + str(lon[3])) + ")" + ")"
        if tol((operation(o3, (operation(o1, first, (operation(o2, second, third)))), fourth)), 24, 0.01):
            print ("(" + str(lon[0]) + o1 + "(" + str(lon[1]) + o2 + str(lon[2]) + ")" + ")" + o3 + str(lon[3]))
        continue


twenty_four()         