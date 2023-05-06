################ Function Definitions ################


# Shows the user what options they have
def displayMenu():

  print("\n")
  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")
  print("\n")
  print("\n")


# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function


def getNumberGradeFromUser():

  val = None

  while (val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None

  return val


def addStudent():
  newStudent = input("Enter new student name: ")
  studentDict[newStudent] = []
  print(f"\n{newStudent} added\n")
  print(f"After new addition {studentDict}")


def removeStudent():
  removalStudent = input("\nEnter name of the student you want to remove: \n")
  if (removalStudent == None or removalStudent not in studentDict.keys()):
    try:
      print(
        "\nError, Either that student is undefined or is not in the the dictionary\n"
      )
    except:
      print("\nyou somehow broke the code\n")
  else:
    print(f"\n{removalStudent} removed")
    del studentDict[removalStudent]
    print(f"Updated version of student dictionary. {studentDict}")


def addGrades():
  addGradesStudent = input(
    "\nEnter name of the student you want to add a grade to: \n")
  if (addGradesStudent == None or addGradesStudent not in studentDict.keys()):
    try:
      print(
        "\nError, Either that student is undefined or is not in the the dictionary\n"
      )
    except:
      print("\nyou somehow broke the code\n")
  else:
    grades = getNumberGradeFromUser()
    print(f"\n{grades} added\n")
    studentDict[addGradesStudent].append(grades)
    print(f"Updated version of student dictionary. {studentDict}")


def listGrades():
  listGrades = input(
    "\nEnter name of the student you want to list his/her grade : \n")
  if (listGrades == None or listGrades not in studentDict.keys()):
    try:
      print(
        "\nError, Either that student is undefined or is not in the the dictionary\n"
      )
    except:
      print("\nyou somehow broke the code\n")
  else:

    print(f"\n{listGrades}  Quizzes\n")
    for grad in studentDict[listGrades]:
      #print(grad + "\n", end="\n") #invalid statement raises typeerror because float and str incompatible
      print(grad, end="\n")

    print(f"Updated version of student dictionary. {studentDict}")


def getAvgGrade():
  student = input(
    "Please enter student name you want to retrieve letter grade for: ")
  if (student == None or student not in studentDict.keys()):
    try:
      print(
        "\nError, Student unavaible, undefined, or not in the dictionary\n")
    except:
      print("\You somehow broke the code\n")
  else:
    avg = 0
    sum = 0
    count = len(studentDict[student])
    for g in studentDict[student]:  #wrong addition ->.values():
      sum += g
    avg = sum / count
    if (avg >= 90):
      print(f"\n{student} current grades is A \n")
    elif (avg >= 80 ): #or avg < 90): # false logic instead of using or replace with and boundedness scope entry L valid mistake for else if chain below
      print(f"\n{student} current grades is B \n")
    elif (avg >= 70 ): #or avg < 80):
      print(f"\n{student} current grades is C \n")
    elif (avg >= 60 ):#)or avg < 70):
      print(f"\n{student} current grades is D \n")
    elif (avg >= 50 ):#or avg < 60):
      print(f"\n{student} current grades is E \n")
    else:
      print(f"{student} current grades is F ")


################ Main Program ################
studentDict = {}
displayMenu()
optionSelection = input("Please select an option: ")

# Application Loop

while (optionSelection != "Quit" and optionSelection != "6"):

  # Prompt the user to select an option
  print()
  #displayMenu()
  if (optionSelection == "1"):
    addStudent()
  elif (optionSelection == "2"):
    removeStudent()
  elif (optionSelection == "3"):
    addGrades()
  elif (optionSelection == "4"):
    listGrades()
  elif (optionSelection == "5"):
    getAvgGrade()
  else:
    print(f"That is an invalid operation terminating the loop")
    break

  displayMenu()
  #inside of indefinite iteration always need a new selection for the loop body after the if/else chain
  optionSelection = input("Once again, Please select an option: ")

print("\noutside while loop")
