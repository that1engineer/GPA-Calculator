gpa = 4.0
print("Welcome to the GPA Calculator, created by Ethan Edgington!")

def PrintSegment():
    print("----------------------------")

def DisplayGPA():
    # Calculate your up-to-date GPA
    RecalculateGPA()

    # Show the GPA
    print(" ")
    PrintSegment()
    print(f"Your GPA is {gpa}")
    PrintSegment()
    print(" ")

# Add class details to the save file
def AddNewClass(semester, year, name, credits, grade):
    with open("classes.txt", "a") as file:
        file.write(f"{semester},{year},{name},{credits},{grade}\n")

def DeleteClass(class_name):
    try:
        with open("classes.txt", "r") as file:
            lines = file.readlines()
        
        found = False
        with open("classes.txt", "w") as file:
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) >= 3 and parts[2] == class_name.upper():
                    found = True
                else:
                    file.write(line)
        
        if found:
            print(f"Class {class_name} has been deleted.")
        else:
            print(f"Class {class_name} not found.")
    except FileNotFoundError:
        print("No class records found.")

def RecalculateGPA():
    global gpa
    try:
        with open("classes.txt", "r") as file:
            lines = file.readlines()
            
        total_credits = 0
        total_points = 0
        grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 5:
                _, _, _, credits, grade = parts
                credits = int(credits)
                grade = grade.upper()
                
                if grade in grade_points:
                    total_credits += credits
                    total_points += credits * grade_points[grade]
        
        if total_credits > 0:
            gpa = total_points / total_credits
        else:
            gpa = 4.0  # Default if no valid courses
    except FileNotFoundError:
        gpa = 4.0  # Default if no file exists

while True:
    choice = input("What would you like to do? \n(1) Show GPA\n(2) Add new classes\n(3) Delete a class\n(4) Quit\nResponse: ")

    if choice == "1":
        DisplayGPA()

    if choice == "2":
        while True:
            # Semester
            while True:
                PrintSegment()
                semester = input("What semester did this take place?\n(1) Spring\n(2) Summer\n(3) Fall\nResponse: ")
                if semester in ["1", "2", "3"]:
                    break
                else:
                    print(f'"{semester}" is an invalid input')

            # Year
            while True:
                PrintSegment()
                year = input("What year did this take place?\nResponse: ")
                if year.isdigit():
                    break
                else:
                    print(f'"{year}" is an invalid input')

            # Name
            PrintSegment()
            name = input("What is the name of the class? (Ex: ENGR 102)\nResponse: ").upper()

            # Credit hours
            while True:
                PrintSegment()
                credits = input("How many credit hours is this class worth?\nResponse: ")
                if credits.isdigit():
                    break
                else:
                    print(f'"{credits}" is an invalid input')

            # Grade
            while True:
                PrintSegment()
                grade = input("What was your final grade?\nA, B, C, D, or F\nResponse: ").upper()
                if grade in ["A", "B", "C", "D", "F"]:
                    break
                else:
                    print(f'"{grade}" is an invalid input')

            # Add to save file
            AddNewClass(semester, year, name, credits, grade)

            # Ask to add another class
            while True:
                PrintSegment()
                again = input("Would you like to add another class?\n(1) Yes\n(2) No\nResponse: ")
                if again in ["2", "N", "1", "Y"]:
                    break
                else:
                    print(f'"{again}" is an invalid input')
            PrintSegment()
            print(" ")
            if again in ["2", "N"]:
                break
    
    if choice == "3":
        PrintSegment()
        class_name = input("Enter the name of the class you want to delete: ").upper()
        DeleteClass(class_name)
        #print("That action is currently unavailable")
        PrintSegment()
    
    if choice == "4":
        print("\nGoodbye!")
        break
