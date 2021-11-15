# Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage.
# Display the equivalent Grade/Mark and Description.

print("Welcome Isko/Iska!")

def User_grade():
    grade_percentage = float(input("Grade percentage: "))
    return grade_percentage



def grade_equivalent():
    if grade >= 97 and grade <=100:
        print("Grade/Mark: 1.0, Description: Excellent")
        
    elif grade >= 94 and grade <=96:
        print("Grade/Mark: 1.25, Description: Excellent")
        
    elif grade >= 91 and grade <=93:
        print("Grade/Mark: 1.5, Description: Very Good")
        
    elif grade >= 88 and grade <=90:
        print("Grade/Mark: 1.75, Description: Very Good")
        
    elif grade >= 85 and grade <=87:
        print("Grade/Mark: 2.0, Description: Good")
        
    elif grade >= 82 and grade <=84:
        print("Grade/Mark: 2.25, Description: Good")
        
    elif grade >= 79 and grade <=81:
        print("Grade/Mark: 2.5, Description: Satisfactory")
        
    elif grade >= 76 and grade <=78:
        print("Grade/Mark: 2.75, Description: Satisfactory")
        
    elif grade == 75:
        print("Grade/Mark: 3.0, Description: Passing")
        
    elif grade >= 65 and grade <=74:
        print("Grade/Mark: 5.0, Description: Failure")
    return grade
       
       
                   
# Consider having options 1, 2, and 3 for other students to insert
# when the percentage is unavailable but asked in the system.
def Other_results():
    if grade == 1:
        print("Grade/Mark: Unavailable, Description: Incomplete")
    elif grade == 2:
        print("Grade/Mark: Unavailable, Description: Withdrawn")
    elif grade == 3:
        print("Grade/Mark: Unavailable, Description: Dropped")
    return grade



def display_result():
    if grade >= 75 and grade <= 100:
        print("Congrats for passing! Padayon!")
    elif grade >= 65 and grade <=74:
        print("Let's do better next time! Padayon!")
    elif grade == 1:
        print("You have missing outputs.")
    elif grade == 2:
        print("You are no longer a student of the university.")
    elif grade == 3:
        print("You are no longer a student of the university.")
    return grade



grade = User_grade()
grade_equivalent()
Other_results()
display_result()