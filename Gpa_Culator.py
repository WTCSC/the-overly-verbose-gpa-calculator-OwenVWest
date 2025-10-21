import time
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
def type_out(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
def gpa_calc(gradescalc):
    gpat = 0.00
    for i in range(1,len(gradescalc)+1):
        gpat += gradescalc[i-1]
    gpat = gpat / len(gradescalc)
    gpat = round(gpat, 2)
    return gpat
type_out("Welcome to the Gpa-culator,\nYour Gpa calculator for idiots!\n-----------------------------------\n\n")
type_out("How many classes are you in (input them in the order that you had them)?: ")
class_count = input("") # main variables
type_out("\n")
grades = []
gpa = 0.0
valid = False
while valid == False:
    if class_count.isdigit() == False: # validates that the input is a number
        type_out("The input that you provided for the number of classes is not a valid input\n")
        type_out("Make sure that your input is in the format of a normal number ex: 3 do not type out the number\n-----------------------------------\n")
        type_out("How many classes are you in?: ")
        class_count = input("")
        type_out("\n")
    elif int(class_count) < 5: # Validates that the input number is positive and 5 or more
        type_out("The input that you provided for the number of classes is not a valid input\n")
        type_out("Make sure that your input is a positive number and is not less than one (you cant have less than 5 classes and be in school according to the one that made this assignment)\n-----------------------------------\n")
        type_out("How many classes are you in?: ")
        class_count = input("")
        type_out("\n")
    else: 
        valid = True
class_count = int(class_count)
temp_class = 1.0
for i in range(1,class_count+1):
    type_out(f"Input your gpa for class {i}: ")
    temp_class = input()
    while is_float(temp_class) == False or len(temp_class) != 3 or float(temp_class) > 4.0 or float(temp_class) < 0.0:
        type_out("The input you provided is not valid\n")
        type_out("Make sure that your input is a decimal number that is 3 characters long ex: 3.0 or ex: 2.6\nextra decimal places are avalible in the non existant paid version!\n")
        type_out("Make sure that your input is between 0.0 and 4.0 (we cant do above 4.0, sorry, this gpa calcualtor is for idiots!)\n-----------------------------------\n")
        type_out(f"Input your gpa for class {i}: ")
        temp_class = input()
    temp_class = float(temp_class)
    grades.append(temp_class)

temp_class = 0
gpa = gpa_calc(grades)
type_out("\n")
type_out(f"Based on the {len(grades)} classes you provided, your gpa is sitting at {gpa}\n\n")
type_out("Which semester would you like to look at (1 or 2)\n1: First half of classes\n2: Second half of classes\n Input 1 or 2: ")
temp_class = input()
while temp_class != "1" and temp_class != "2":
    type_out("The input you provided is not 1 or 2, please provide the input as 1 or 2 as a whole integer without typing them out\n\n")
    type_out("Which semester would you like to look at (1 or 2)\n1: First half of classes\n2: Second half of classes\n Input 1 or 2: ")
    temp_class = input()
temp_class = int(temp_class)
length = len(grades)/2
length = int(round(length, 0))
sem_gpa = 0
temp_list = []
if temp_class == 1:
    sem_gpa = gpa_calc(grades[:length])
    type_out(f"The gpa for the first {length} classes provided is: {sem_gpa}\n")
    if sem_gpa > gpa:
        type_out("\n You are trending downwards, you did better in the first semester than the overall, shame.\n")
elif temp_class == 2:
    sem_gpa = gpa_calc(grades[length:])
    type_out(f"The gpa for the last {length} classes provided is: {sem_gpa}\n")
    if sem_gpa > gpa:
        type_out("\n Nice! You are trending upwards, your seconds semester gpa is higher than the overall.\n")
else:
    type_out("Error in sem_gpa output")
type_out("\nWhat is your goal gpa?: ")
goal_gpa = input()
while is_float(goal_gpa) == False or float(goal_gpa) > 4.0 or float(goal_gpa) < 0.0:
    type_out("The input you provided is not valid\n")
    type_out("Make sure that your input is a decimal number that is 3 characters long ex: 3.0 or ex: 2.6\nextra decimal places are avalible in the non existant paid version!\n")
    type_out("Make sure that your input is between 0.0 and 4.0 (we cant do above 4.0, sorry, this gpa calcualtor is for idiots!)\n-----------------------------------\n")
    type_out("What is your goal gpa?: ")
    goal_gpa = input()
goal_gpa = float(goal_gpa)
for i in range (0,len(grades)):
    gradesTemp = grades[:]
    noneaval = True
    gradesTemp[i] = 4.0
    if gpa_calc(gradesTemp) >= goal_gpa:
        noneaval = False
        type_out(f"\nBy changing grade {i} from {(grades[i])} to 4.0 you can achive a gpa of {gpa_calc(gradesTemp)}\n")
if noneaval:
    type_out(f"There are no single classes that could bring your gpa above your goal gpa of {goal_gpa}")





