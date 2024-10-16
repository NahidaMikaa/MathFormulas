import time 
import mathformulas as mathF

def yearselector():
    print("[","\033[0;35;40m1","\033[0;37;40m] 1°Year")
    print("[","\033[0;36;40m2","\033[0;37;40m] 2°Year")
    print("[","\033[0;32;40m3","\033[0;37;40m] 3°Year")
    print("[","\033[0;33;40m0","\033[0;37;40m] Exit") 

def firstyear_semesterselector():
    print("\n[","\033[0;35;40m1","\033[0;37;40m] 1°Semester")
    print("[","\033[0;36;40m2","\033[0;37;40m] 2°Semester")
    print("[","\033[0;33;40m0","\033[0;37;40m] Back\n")

def final_firstyear_semesterselector():
    firstyear_semesterselector()

    semester = input("Enter the semester: ")
    semester = int(semester)

    if semester == 1:
        firstsemester_partialselector() 
    elif semester == 2:
        secondsemester_partialselector()
    elif semester == 0:
        print("\nReturning to the main menu...\n")
        time.sleep(2)
        years()
    else:
        print("Invalid semester!")

def secondyear_semesterselector():
    print("\n[","\033[0;35;40m3","\033[0;37;40m] 3°Semester")
    print("[","\033[0;36;40m4","\033[0;37;40m] 4°Semester")
    print("[","\033[0;33;40m0","\033[0;37;40m] Back\n")

def final_secondyear_semesterselector():
    secondyear_semesterselector()

    semester = input("Enter the semester: ")
    semester = int(semester)

    if semester == 3:
        thirdsemester_partialselector() 
    elif semester == 4:
        fourthsemester_partialselector()
    elif semester == 0:
        print("\nReturning to the main menu...\n")
        time.sleep(2)
        years()
    else:
        print("Invalid semester!")

def thirdyear_semesterselector():
    print("\n[","\033[0;35;40m5","\033[0;37;40m] 5°Semester")
    print("[","\033[0;36;40m6","\033[0;37;40m] 6°Semester")
    print("[","\033[0;33;40m0","\033[0;37;40m] Back\n")

def final_thirdyear_semesterselector():
    thirdyear_semesterselector()

    semester = input("Enter the semester: ")
    semester = int(semester)

    if semester == 5:
        fifthsemester_partialselector() 
    elif semester == 6:
        sixthsemester_partialselector()
    elif semester == 0:
        print("\nReturning to the main menu...\n")
        time.sleep(2)
        years()
    else:
        print("Invalid semester!")

def partialselector():
    print("\n[","\033[0;35;40m1","\033[0;37;40m] Partial 1")
    print("[","\033[0;36;40m2","\033[0;37;40m] Partial 2")
    print("[","\033[0;32;40m3","\033[0;37;40m] Partial 3")
    print("[","\033[0;34;40m4","\033[0;37;40m] Partial 4")
    print("[","\033[0;33;40m5","\033[0;37;40m] Institutional Exam")
    print("[","\033[0;31;40m0","\033[0;37;40m] Back")

def firstsemester_partialselector():
    partialselector()
    firstsemesterpartials = input("\nEnter the partial: ")
    firstsemesterpartials = int(firstsemesterpartials)

    if firstsemesterpartials == 1:
        final_Firstyear_Firstsemester_Firstpartial_themeselector()
    elif firstsemesterpartials == 2:
        print("Partial 2")
    elif firstsemesterpartials == 3:
        print("Partial 3")
    elif firstsemesterpartials == 4:
        print("Partial 4")
    elif firstsemesterpartials == 5:
        print("Institutional Exam")
    elif firstsemesterpartials == 0: #Back
        time.sleep(2)
        final_firstyear_semesterselector()
    else:
        print("Invalid input.")
def secondsemester_partialselector():
    partialselector()
    secondsemesterpartials = input("\nEnter the partial: ")
    secondsemesterpartials = int(secondsemesterpartials)

    if secondsemesterpartials == 1:
        print("Partial 1")
    elif secondsemesterpartials == 2:
        print("Partial 2")
    elif secondsemesterpartials == 3:
        print("Partial 3")
    elif secondsemesterpartials == 4:
        print("Partial 4")
    elif secondsemesterpartials == 5:
        print("Institutional Exam")
    elif secondsemesterpartials == 0: #Back
        time.sleep(2)
        final_firstyear_semesterselector()
    else:
        print("Invalid input.")

def thirdsemester_partialselector():
    partialselector()
    thirdsemesterpartials = input("\nEnter the partial: ")
    thirdsemesterpartials = int(thirdsemesterpartials)

    if thirdsemesterpartials == 1:
        final_Secondyear_Thirdsemester_Firstpartial_themeselector()
    elif thirdsemesterpartials == 2:
        final_Secondyear_Thirdsemester_Secondpartial_themeselector()
    elif thirdsemesterpartials == 3:
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector()
    elif thirdsemesterpartials == 4:
        print("Partial 4")
    elif thirdsemesterpartials == 5:
        print("Institutional Exam")
    elif thirdsemesterpartials == 0: #Back
        time.sleep(2)
        final_secondyear_semesterselector()
    else:
        print("Invalid input.")

def fourthsemester_partialselector():
    partialselector()
    fourthsemesterpartials = input("\nEnter the partial: ")
    fourthsemesterpartials = int(fourthsemesterpartials)

    if fourthsemesterpartials == 1:
        print("Partial 1")
    elif fourthsemesterpartials == 2:
        print("Partial 2")
    elif fourthsemesterpartials == 3:
        print("Partial 3")
    elif fourthsemesterpartials == 4:
        print("Partial 4")
    elif fourthsemesterpartials == 5:
        print("Institutional Exam")
    elif fourthsemesterpartials == 0: #Back
        time.sleep(2)
        final_secondyear_semesterselector()
    else:
        print("Invalid input.")

def fifthsemester_partialselector():
    partialselector()
    fifthsemesterpartials = input("\nEnter the partial: ")
    fifthsemesterpartials = int(fifthsemesterpartials)

    if fifthsemesterpartials == 1:
        print("Partial 1")
    elif fifthsemesterpartials == 2:
        print("Partial 2")
    elif fifthsemesterpartials == 3:
        print("Partial 3")
    elif fifthsemesterpartials == 4:
        print("Partial 4")
    elif fifthsemesterpartials == 5:
        print("Institutional Exam")
    elif fifthsemesterpartials == 0: #Back
        time.sleep(2)
        final_thirdyear_semesterselector()
    else:
        print("Invalid input.")

def sixthsemester_partialselector():
    partialselector()
    sixthsemesterpartials = input("\nEnter the partial: ")
    sixthsemesterpartials = int(sixthsemesterpartials)

    if sixthsemesterpartials == 1:
        print("Partial 1")
    elif sixthsemesterpartials == 2:
        print("Partial 2")
    elif sixthsemesterpartials == 3:
        print("Partial 3")
    elif sixthsemesterpartials == 4:
        print("Partial 4")
    elif sixthsemesterpartials == 5:
        print("Institutional Exam")
    elif sixthsemesterpartials == 0: #Back
        time.sleep(2)
        final_thirdyear_semesterselector()
    else:
        print("Invalid input.")

def years():
    yearselector()
    year = input("\nEnter your year of study: ")
    year = int(year)

    if year == 1:
        final_firstyear_semesterselector()

    elif year == 2:
        final_secondyear_semesterselector()
    
    elif year == 3:
        final_thirdyear_semesterselector()
    
    elif year == 0:
        print("\nExiting...")
        time.sleep(2)
        print("Thank for using it.")
        exit()
    else:
        print("Invalid input.")

def Secondyear_Thirdsemester_Firstpartial_themeselector():
    print("\n[","\033[0;35;40m1","\033[0;37;40m] Distance between two points")
    print("[","\033[0;36;40m2","\033[0;37;40m] Area")
    print("[","\033[0;33;40m3","\033[0;37;40m] Ratio of a line segment")
    print("[","\033[0;34;40m4","\033[0;37;40m] Coordinates of ratio in a line segment")
    print("[","\033[0;32;40m5","\033[0;37;40m] Midpoint of a line segment")
    print("[","\033[0;31;40m0","\033[0;37;40m] Back\n")

def final_Secondyear_Thirdsemester_Firstpartial_themeselector():
    Secondyear_Thirdsemester_Firstpartial_themeselector()

    thirdsemesterFirstPartialTheme = input("\nEnter the theme: ")
    thirdsemesterFirstPartialTheme = int(thirdsemesterFirstPartialTheme)

    if thirdsemesterFirstPartialTheme == 1:
        mathF.distance_between_two_points()
        time.sleep(5)
        final_Secondyear_Thirdsemester_Firstpartial_themeselector()
    elif thirdsemesterFirstPartialTheme == 2:
        mathF.Area()
        time.sleep(5)
        final_Secondyear_Thirdsemester_Firstpartial_themeselector()
    elif thirdsemesterFirstPartialTheme == 3:
        mathF.ratio_of_a_line_segment()
        time.sleep(5)
        final_Secondyear_Thirdsemester_Firstpartial_themeselector()
    elif thirdsemesterFirstPartialTheme == 4:
        mathF.coordinates_of_ratio()
        time.sleep(5)
        final_Secondyear_Thirdsemester_Firstpartial_themeselector()
    elif thirdsemesterFirstPartialTheme == 5:
        mathF.midpoint_of_a_line_segment()
        time.sleep(5)
        final_Secondyear_Thirdsemester_Firstpartial_themeselector()
    elif thirdsemesterFirstPartialTheme == 0: #Back
        time.sleep(2)
        thirdsemester_partialselector()
    else:
        print("Invalid input.")

def Firstyear_Firstsemester_Firstpartial_themeselector():
    #Sets may be added later
    print("[","\033[0;31;40m0","\033[0;37;40m] Back\n")

def final_Firstyear_Firstsemester_Firstpartial_themeselector():
    Firstyear_Firstsemester_Firstpartial_themeselector()

    firstsemesterFirstPartialTheme = input("\nEnter the theme: ")
    firstsemesterFirstPartialTheme = int(firstsemesterFirstPartialTheme)

    if firstsemesterFirstPartialTheme == 0: #Back
        time.sleep(2)
        firstsemester_partialselector()
    else:
        print("Invalid input.")

def Secondyear_Thirdsemester_Secondpartial_themeselector():
    print("\n[","\033[0;35;40m1","\033[0;37;40m] Slope")
    print("[","\033[0;36;40m2","\033[0;37;40m] Get Slope from an Angle")
    print("[","\033[0;33;40m3","\033[0;37;40m] Angle between lines")
    print("[","\033[0;31;40m0","\033[0;37;40m] Back\n")

def final_Secondyear_Thirdsemester_Secondpartial_themeselector():
    Secondyear_Thirdsemester_Secondpartial_themeselector()

    thirdsemesterSecondPartialTheme = input("\nEnter the theme: ")
    thirdsemesterSecondPartialTheme = int(thirdsemesterSecondPartialTheme)

    if thirdsemesterSecondPartialTheme == 1:
        mathF.slope()
        time.sleep(5)
        final_Secondyear_Thirdsemester_Secondpartial_themeselector()
    elif thirdsemesterSecondPartialTheme == 2:
        mathF.slope_from_angle()
        time.sleep(5)
        final_Secondyear_Thirdsemester_Secondpartial_themeselector()
    elif thirdsemesterSecondPartialTheme == 3:
        mathF.angle_between_lines()
        time.sleep(5)
        final_Secondyear_Thirdsemester_Secondpartial_themeselector()
    elif thirdsemesterSecondPartialTheme == 4:
        time.sleep(5)
        final_Secondyear_Thirdsemester_Secondpartial_themeselector()
    elif thirdsemesterSecondPartialTheme == 5:
        time.sleep(5)
        final_Secondyear_Thirdsemester_Secondpartial_themeselector()
    elif thirdsemesterSecondPartialTheme == 0: #Back
        time.sleep(2)
        thirdsemester_partialselector()
    else:
        print("Invalid input.")

def Secondyear_Thirdsemester_Thirdpartial_themeselector():
    print("\n[","\033[0;35;40m1","\033[0;37;40m] Point-Slope equation of a line")
    print("[","\033[0;36;40m2","\033[0;37;40m] Equation of a line that passes through 2 points")
    print("[","\033[0;33;40m3","\033[0;37;40m] xx")
    print("[","\033[0;34;40m4","\033[0;37;40m] xx")
    print("[","\033[0;32;40m5","\033[0;37;40m] xx")
    print("[","\033[0;31;40m0","\033[0;37;40m] Back\n")

def final_Secondyear_Thirdsemester_Thirdpartial_themeselector():
    Secondyear_Thirdsemester_Thirdpartial_themeselector()

    thirdsemesterThirdPartialTheme = input("\nEnter the theme: ")
    thirdsemesterThirdPartialTheme = int(thirdsemesterThirdPartialTheme)

    if thirdsemesterThirdPartialTheme == 1:
        mathF.point_slope_equaton_of_a_line()
        time.sleep(5)
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector()
    elif thirdsemesterThirdPartialTheme == 2:
        mathF.Equation_of_a_line_that_passes_through_2_points()
        time.sleep(5)
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector()
    elif thirdsemesterThirdPartialTheme == 3:
        time.sleep(5)
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector()
    elif thirdsemesterThirdPartialTheme == 4:
        time.sleep(5)
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector()
    elif thirdsemesterThirdPartialTheme == 5:
        time.sleep(5)
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector()
    elif thirdsemesterThirdPartialTheme == 0: #Back
        time.sleep(2)
        thirdsemester_partialselector()
    else:
        print("Invalid input.")



print(r'''
 __  __       _   _       _____                          _
|  \/  | __ _| |_| |__   |  ___|__  _ __ _ __ ___  _   _| | __ _ ___
| |\/| |/ _` | __| '_ \  | |_ / _ \| '__| '_ ` _ \| | | | |/ _` / __|
| |  | | (_| | |_| | | | |  _| (_) | |  | | | | | | |_| | | (_| \__ \
|_|  |_|\__,_|\__|_| |_| |_|  \___/|_|  |_| |_| |_|\__,_|_|\__,_|___/

''') 

print(r'''
                ____            _   _       _     _     _
               | __ ) _   _    | \ | | __ _| |__ (_) __| | __ _
               |  _ \| | | |   |  \| |/ _` | '_ \| |/ _` |/ _` |
               | |_) | |_| |_  | |\  | (_| | | | | | (_| | (_| |
               |____/ \__, (_) |_| \_|\__,_|_| |_|_|\__,_|\__,_|
                      |___/
''')
   


years()


