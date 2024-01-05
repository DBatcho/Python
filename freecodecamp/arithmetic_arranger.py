#recieves the arithmetic data and seperates the strings into usable variables
def arithmetic_arranger (problems, answers):
    index = 0
    num1 = []
    num2 = []
    artop = []
    plen = []
    equals = []
    largest = 0

    for problem in problems:

        #find position of operator and error check that it is + or -
        if problem.find('+') > 1:
            spos = problem.find('+')
        elif problem.find('-') > 1:
            spos = problem.find('-')
        else:
            print("Error: Operator must be '+' or '-'.")
            quit()
    
        num1.append(str(problem[0 : spos].strip()))
        num2.append(str(problem[spos+1 : ].strip()))
        artop.append(str(problem[spos : spos+1].strip()))

        if len(num1[index]) > len(num2[index]):
            largest = len(num1[index])
        else:
            largest = len(num2[index])

        #Error check that there is not a number input greater than 4 digits long
        if largest > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()

        #finds the answer if user requested and error checks that the nums are numbers
        if answers == True:
            if artop[index] == '+':
                try:
                    equals.append(str(int(num1[index]) + int(num2[index])))
                except:
                    print("Error: Numbers must only contain digits.")
                    quit()
            else:
                try:
                    equals.append(str(int(num1[index]) - int(num2[index])))
                except:
                    print("Error: Numbers must only contain digits.")
                    quit()

            if largest < len(equals[index]):
                largest = len(equals[index])

        plen.append(largest)
        index = index + 1

    #Error checks that there is not more than 5 problems inputed
    if index > 5:
        print ("Error: Too many problems.")
        quit()

    outputA_A(num1, num2, artop, plen, equals)

#prints the problems vertically       
def outputA_A(num1, num2, artop, plen, equals):
    #prints the num1 on the vertical with requested spaces
    index = 0
    for num in num1:
        print ("", end = "  ")
        if len(num) >= plen[index]:
            print (num, end = "    ")
        else:
            space = len(num)
            while (space < plen[index]):
                print ("", end = " ")
                space = space + 1
            print (num, end = "    ")
        index = index + 1

    print()

    #prints num2 and operators on the vertical with requested spaces
    index = 0
    for num in num2:
        print (artop[index], end = " ")
        if len(num) == plen[index]:
            print (num, end = "    ")
        else:
            space = len(num)
            while (space < plen[index]):
                print ("", end = " ")
                space = space + 1
            print (num, end = "    ")
        index = index + 1
    
    print()

    #prints dashes under the equations on the vertical
    for x in plen:
        index = x
        print ("", end = "--")
        while index > 0:
            print("", end = "-")
            index = index - 1
        print ("", end = "    ")

    print()

    #if answers were requested: prints answers on the vertical with requested spaces
    index = 0
    if len(equals) > 0:
        for num in equals:
            print ("", end = "  ")
            if len(num) >= plen[index]:
                print (num, end = "    ")
            else:
                space = len(num)
                while (space < plen[index]):
                    print ("", end = " ")
                    space = space + 1
                print (num, end = "    ")
            index = index + 1

    
artprob = input("Please enter an Artmetic Problem: ")
if len(artprob) < 1 : artprob = ["2 + 698", "3801 - 2", "45 + 43", "123 + 49", "293 + 332"]
answers = input ("Do you want the answers: ")
if len(answers) < 1 : answers = True
arithmetic_arranger(artprob, answers)