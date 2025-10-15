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
for i in range(1,len(grades)+1):
    temp_class += grades[i-1]
gpa = temp_class / len(grades)
gpa = round(gpa, 2)
type_out("\n")
type_out(f"Based on the {len(grades)} classes you provided, your gpa is sitting at {gpa}\n")

