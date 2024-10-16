import math
import numpy as np
import decimal
from fractions import Fraction

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
    x1, y1 = float(x1), float(y1)

    x2, y2 = input("\nEnter the second coordinate \033[0;34;40m(x, y)\033[0;37;40m: ").split()
    x2, y2 = float(x2), float(y2)
    
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
            print(f"\nThe angle of this line is: \033[0;36;40m{angle2} \033[0;37;40m")

def slope_from_angle():
    θ = input("\nEnter the angle of the slope \033[0;35;40m θ \033[0;37;40m: ")
    θ = float(θ)
    
    m = math.tan(math.radians(θ))

    print(f"\nThe slope of this line is: \033[0;32;40m{m} \033[0;37;40m")

def angle_between_lines():
    m1, m2= input("\nEnter the value of the slope in fraction \033[0;35;40m\033[0;37;40m: ").split("/")
    m1, m2 = int(m1), int(m2)
    
    mA = (m1/m2)
    #print(mA)
    
    m3, m4 = input("\nEnter the value of the slope in fraction \033[0;35;40m\033[0;37;40m: ").split("/")
    m3, m4 = int(m3), int(m4)
    
    mB = (m3/m4)
    #print(mB)

    μ = (1+(mA*mB))
    print(f"\n{μ}")
    if μ == 0:
        print(f"\nThe angle between the two lines is: \033[0;36;40m90° \033[0;37;40m degrees")
    else:
        alpha = math.atan((mB-mA)/μ)
        alpha2 = math.degrees(alpha)
    
        if mA == mB:
            print("\nThis lines are parralel")
        elif (mA*mB) == -1:
            print("\nThis lines are perpendicular")
        elif (mA*mB) != -1 and mA != mB:
            print("\nThis lines are oblique")
    
        print(f"\nThe angle between the two lines is: \033[0;36;40m{alpha2} \033[0;37;40m degrees")

def sets():
    #https://www.programiz.com/python-programming/methods/set/union
    
    A = {"apple", "grape", "pear"}
    B = {"apple"}

    print(f"A = B: {B.issubset(A)}") 

def point_slope_equaton_of_a_line():
    x1, y1 = input("\nEnter the first coordinate \033[0;35;40m(x, y)\033[0;37;40m: ").split()
    x1, y1 = int(x1), int(y1)

    m1, m2= input("\nEnter the value of the slope in fraction \033[0;35;40m\033[0;37;40m: ").split("/")
    m1, m2 = int(m1), int(m2)

    m = (m1/m2)

    first = (-(y1))
    if first <= -1:
        print(f"y {first}")
    elif first >= 1:
        print(f"y + {first}")
    
    second = (-(x1))
    if second <= -1:
        xd =(f"x {second}")
        print(xd)
    elif second >= 1:
        xd = (f"x + {second}")
        print(xd)

    third = (m*second)
    print(third)
    fourth = (f"{m}x")
    print(fourth)

    if first <= -1:
        fifth = (third + (first*-1))
        print(fifth)
    if first >= 1:
        fifth = (third - first)
        print(fifth)
    
    m_in_fraction = Fraction(m).limit_denominator()
    string_m_in_fraction = str(Fraction(m).limit_denominator())
    print(m_in_fraction)
    
    
    fifth_in_fraction = Fraction(fifth).limit_denominator()
    string_fifth_in_fraction = str(Fraction(fifth).limit_denominator())
    print(fifth_in_fraction)

    ordinary = (f"y = {m_in_fraction}x {fifth_in_fraction}")
    print(ordinary)

    d1, d2 = string_m_in_fraction.split("/")
    d1, d2 = int(d1), int(d2)

    d3, d4 = string_fifth_in_fraction.split("/")
    d3, d4 = int(d3), int(d4)
    
    if d2 == d4:
        B = d2
    if d2 != d4:
        B = (d2*d4)

    A = d1 
    C = d3

    if A <= -1:
        A = (d1*-1)
        B_alpha = B
        C = (d3*-1)
    elif A >= 1:
        A = d1
        B_alpha = (B*-1)
        C = d3

    General = (f"{A}x {B_alpha}y {C} = 0")
    print(General)

def Equation_of_a_line_that_passes_through_2_points():
    x1, y1 = input("\nEnter the first coordinate \033[0;35;40m(x, y)\033[0;37;40m: ").split()
    x1, y1 = float(x1), float(y1)

    x2, y2 = input("\nEnter the second coordinate \033[0;34;40m(x, y)\033[0;37;40m: ").split()
    x2, y2 = float(x2), float(y2)

    m = ((y2-y1)/(x2-x1))

    first = (-(y1))
    if first <= -1:
        print(f"y {first}")
    elif first >= 1:
        print(f"y + {first}")
    
    second = (-(x1))
    if second <= -1:
        xd =(f"x {second}")
        print(xd)
    elif second >= 1:
        xd = (f"x + {second}")
        print(xd)

    third = (m*second)
    print(third)
    fourth = (f"{m}x")
    print(fourth)

    if first <= -1:
        fifth = (third + (first*-1))
        print(fifth)
    if first >= 1:
        fifth = (third - first)
        print(fifth)
    
    m_in_fraction = Fraction(m).limit_denominator()
    string_m_in_fraction = str(Fraction(m).limit_denominator())
    print(m_in_fraction)
    
    
    fifth_in_fraction = Fraction(fifth).limit_denominator()
    string_fifth_in_fraction = str(Fraction(fifth).limit_denominator())
    print(fifth_in_fraction)

    ordinary = (f"y = {m_in_fraction}x {fifth_in_fraction}")
    print(ordinary)

    d1, d2 = string_m_in_fraction.split("/")
    d1, d2 = int(d1), int(d2)

    d3, d4 = string_fifth_in_fraction.split("/")
    d3, d4 = int(d3), int(d4)
    
    if d2 == d4:
        B = d2
    if d2 != d4:
        B = (d2*d4)

    A = d1 
    C = d3

    if A <= -1:
        A = (d1*-1)
        B_alpha = B
        C = (d3*-1)
    elif A >= 1:
        A = d1
        B_alpha = (B*-1)
        C = d3

    General = (f"{A}x {B_alpha}y {C} = 0")
    print(General)

Equation_of_a_line_that_passes_through_2_points()