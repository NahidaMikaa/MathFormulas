import math
import numpy as np

def distance_between_two_points():
    x1, y1 = input("\nEnter the first coordinate \033[0;35;40m(x, y)\033[0;37;40m: ").split()
    x1, y1 = float(x1), float(y1)

    x2, y2 = input("\nEnter the second coordinate \033[0;34;40m(x, y)\033[0;37;40m: ").split()
    x2, y2 = float(x2), float(y2)
    
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(f"\nThe distance between the two points is: \033[0;32;40m{distance} u \033[0;37;40m")

def Area():
    whichtype = input("\nHow many coordinates do you want to enter: ")
    whichtype = int(whichtype)

    if whichtype == 3:
        x1, y1 = input("\nEnter the first coordinate \033[0;35;40m(x, y)\033[0;37;40m: ").split()
        x1, y1 = float(x1), float(y1)

        x2, y2 = input("\nEnter the second coordinate \033[0;34;40m(x, y)\033[0;37;40m: ").split()
        x2, y2 = float(x2), float(y2)

        x3, y3 = input("\nEnter the second coordinate \033[0;36;40m(x, y)\033[0;37;40m: ").split()
        x3, y3 = float(x3), float(y3)

        area = abs(((y1 * x2) + (y2 * x3) + (y3 * x1)) - ((y1 * x3) + (y3 * x2) + (y2 * x1)))

        print(f"\nThe area of this figure is: \033[0;32;40m{area/2} u² \033[0;37;40m")
        
    elif whichtype == 4:
        x1, y1 = input("\nEnter the first coordinate \033[0;35;40m(x, y)\033[0;37;40m: ").split()
        x1, y1 = float(x1), float(y1)

        x2, y2 = input("\nEnter the second coordinate \033[0;34;40m(x, y)\033[0;37;40m: ").split()
        x2, y2 = float(x2), float(y2)

        x3, y3 = input("\nEnter the second coordinate \033[0;36;40m(x, y)\033[0;37;40m: ").split()
        x3, y3 = float(x3), float(y3)

        x4, y4 = input("\nEnter the fourth coordinate \033[0;31;40m(x, y)\033[0;37;40m: ").split()
        x4, y4 = float(x4), float(y4)
        
        area = abs(((y1 * x2) + (y2 * x3) + (y3 * x4) + (y4 * x1)) - ((y1 * x4) + (y4 * x3) + (y3 * x2) + (y2 * x1)))

        print(f"\nThe area of this figure is: \033[0;32;40m{area/2} u² \033[0;37;40m")

    else:
        print("\nInvalid choice.")
        print("\nPlease enter a valid choice (\033[0;35;40m3\033[0;37;40m/\033[0;31;40m4\033[0;37;40m)\033[0;37;40m.")

def ratio_of_a_line_segment():
    p1p, pp2 = input("\nEnter the value of \033[0;35;40mP₁P\033[0;37;40m and \033[0;34;40mPP₂\033[0;37;40m: ").split()
    p1p, pp2 = float(p1p), float(pp2)

    r = p1p/pp2

    print(f"\nThe value of the ratio is \033[0;35;40m{p1p}\033[0;37;40m/\033[0;31;40m{pp2}\033[0;37;40m or \033[0;36;40m{r}\033[0;37;40m ")

def coordinates_of_ratio():
    r1, r2 = input("\nEnter the value of the \033[0;31;40mratio\033[0;37;40m: ").split()
    r1, r2 = int(r1), int(r2)

    x1, y1 = input("\nEnter the first coordinate \033[0;35;40m(x, y)\033[0;37;40m: ").split()
    x1, y1 = float(x1), float(y1)

    x2, y2 = input("\nEnter the second coordinate \033[0;34;40m(x, y)\033[0;37;40m: ").split()
    x2, y2 = float(x2), float(y2)

    r = r1/r2
    x = ((x1 + (r*x2))/(1+r))
    y = ((y1 + (r*y2))/(1+r))

    print(f"\nThe coordinates of the ratio are (\033[0;35;40m{x}\033[0;37;40m, \033[0;31;40m{y}\033[0;37;40m)\033[0;37;40m.")

def midpoint_of_a_line_segment():
    x1, y1 = input("\nEnter the first coordinate \033[0;35;40m(x, y)\033[0;37;40m: ").split()
    x1, y1 = int(x1), int(y1)

    x2, y2 = input("\nEnter the second coordinate \033[0;34;40m(x, y)\033[0;37;40m: ").split()
    x2, y2 = int(x2), int(y2)

    Xm = (x1 + x2) / 2
    Ym = (y1 + y2) / 2

    print(f"\nThe coordinates of the midpoint is (\033[0;35;40m{Xm}\033[0;37;40m, \033[0;31;40m{Ym}\033[0;37;40m)\033[0;37;40m.")


def slope():
    x1, y1 = input("\nEnter the first coordinate \033[0;35;40m(x, y)\033[0;37;40m: ").split()
    x1, y1 = int(x1), int(y1)

    x2, y2 = input("\nEnter the second coordinate \033[0;34;40m(x, y)\033[0;37;40m: ").split()
    x2, y2 = int(x2), int(y2)
    
    if y1 == y2:
        print("\nThe slope is \033[0;32;40mzero\033[0;37;40m.") #both Y value are at the same position
    elif x1 == x2:
        print("\nThe slope is \033[0;31;40mundefinite\033[0;37;40m.") #both X value are at the same position
    else:
        m = ((y2-y1)/(x2-x1))
    
        #print(f"\nThe slope of this line is: \033[0;32;40m{m} \033[0;37;40m")

    
        if m > 0:
            print("\nThe slope is positive")
            
            m = ((y2-y1)/(x2-x1))
    
            print(f"\nThe slope of this line is: \033[0;32;40m{m} \033[0;37;40m")
            angle = math.atan(m)
            angle2 = math.degrees(angle)
            print(f"\nThe slope of this line is: \033[0;36;40m{angle2} \033[0;37;40m")

        elif m < 0:
            print("\nThe slope is negative")

            m = ((y2-y1)/(x2-x1))
    
            print(f"\nThe slope of this line is: \033[0;32;40m{m} \033[0;37;40m")

            angle = math.atan(m)
            angle2 = math.degrees(angle)
            print(f"\nThe slope of this line is: \033[0;36;40m{angle2} \033[0;37;40m")

def slope_from_angle():
    θ = input("\nEnter the angle of the slope \033[0;35;40m θ \033[0;37;40m: ")
    θ = float(θ)
    
    m = math.tan(math.radians(θ))

    print(f"\nThe slope of this line is: \033[0;32;40m{m} \033[0;37;40m")

def angle_between_lines():
    m1, m2 = input("\nEnter the value of the slope of both lines \033[0;35;40m(m₁, m₂)\033[0;37;40m: ").split()
    m1, m2 = float(m1), float(m2)

    α = math.degrees(math.atan(abs((m2-m1)/(1+(m1*m2)))))

    print(f"\nThe angle between the two lines is: \033[0;36;40m{α} \033[0;37;40m degrees")

def sets():
    #https://www.programiz.com/python-programming/methods/set/union
    
    A = {"apple", "grape", "pear"}
    B = {"apple"}

    print(f"A = B: {B.issubset(A)}") 
