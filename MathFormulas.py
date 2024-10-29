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
    
    m3, m4 = input("\nEnter the value of the slope in fraction \033[0;34;40m\033[0;37;40m: ").split("/")
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
    x1, y1 = float(x1), float(y1)

    m1, m2= input("\nEnter the value of the slope in fraction \033[0;34;40m / \033[0;37;40m: ").split("/")
    m1, m2 = float(m1), float(m2)

    m = (m1/m2)

    first = (-(y1))
    if first <= -1:
        dx = (f"y {first}")
    elif first >= 1:
        dx = (f"y + {first}")
    
    second = (-(x1))
    if second <= -1:
        xd =(f"x {second}")
    elif second >= 1:
        xd = (f"x + {second}")
        
    print(f"\nThe formula is:\033[0;32;40m {dx} = {m}({xd})\033[0;37;40m")

    third = (m*second)
    #print(third)
    fourth = (f"{m}x")
    #print(fourth)

    if first <= -1:
        fifth = (third + (first*-1))
        #print(fifth)
    if first >= 1:
        fifth = (third - first)
        #print(fifth)
    
    if m.is_integer() == False and fifth.is_integer() == False:
        m_in_fraction = Fraction(m).limit_denominator()
        string_m_in_fraction = str(Fraction(m).limit_denominator())
        #print(m_in_fraction)
    
    
        fifth_in_fraction = Fraction(fifth).limit_denominator()
        string_fifth_in_fraction = str(Fraction(fifth).limit_denominator())
        #print(fifth_in_fraction)
    
        ordinary = (f"y = {m_in_fraction}x {fifth_in_fraction}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        d1, d2 = string_m_in_fraction.split("/")
        d1, d2 = int(d1), int(d2)
        #print(d1)
        #print(d2)
    
        d3, d4 = string_fifth_in_fraction.split("/")
        d3, d4 = int(d3), int(d4)
        #print(d3)
        #print(d4)

        aM = d1 
        cM = d3

        if d2 == d4:
            bM = d2
        elif d2 != d4:
            bM = (d2*d4)

        if aM <= -1:
            aM = (d1*-1)
            B_alpha = bM
            cM = (d3*-1)
        elif aM >= 1:
            aM = d1
            B_alpha = (bM*-1)
            cM = d3

        General = (f"{aM}x {B_alpha}y {cM} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {General}\033[0;37;40m\n")
        
    elif m.is_integer() == True and fifth.is_integer() == False:
    
        fifth_in_fraction = Fraction(fifth).limit_denominator()
        string_fifth_in_fraction = str(Fraction(fifth).limit_denominator())
        #print(fifth_in_fraction)
    
        ordinary = (f"y = {m}x {fifth_in_fraction}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        d3, d4 = string_fifth_in_fraction.split("/")
        d3, d4 = int(d3), int(d4)
        #print(d3)
        #print(d4)
    
        bM =d4 #y value

        aM = m*d4 
        cM = d3

        if aM <= -1:
            aM = ((m*d4)*-1)
            B_alpha = bM
            cM = (d3*-1)
        elif aM >= 1:
            aM = d1
            B_alpha = (bM*-1)
            cM = m*d4

        General = (f"{aM}x {B_alpha}y {cM} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {General}\033[0;37;40m\n")
    
    elif m.is_integer() == False and fifth.is_integer() == True:
        m_in_fraction = Fraction(m).limit_denominator()
        string_m_in_fraction = str(Fraction(m).limit_denominator())
        #print(m_in_fraction)
    
        ordinary = (f"y = {m_in_fraction}x {fifth}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        d1, d2 = string_m_in_fraction.split("/")
        d1, d2 = int(d1), int(d2)
        #print(d1)
        #print(d2)
        
        bM = d2
        

        aM = d1 
        cM = fifth*d2

        if aM <= -1:
            aM = ((fifth*d2)*-1)
            B_alpha = bM
            cM = (d3*-1)
        elif aM >= 1:
            aM = d1
            B_alpha = (bM*-1)
            cM = fifth*d2

        General = (f"{aM}x {B_alpha}y {cM} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {General}\033[0;37;40m\n")
    
    if m.is_integer() == True and fifth.is_integer() == True:
        
        ordinary = (f"y = {m}x {fifth}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")
    
        bM = 1
        
        aM = m
        cM = fifth

        if aM <= -1:
            aM = (m*-1)
            B_alpha = bM
            cM = (fifth*-1)
        elif aM >= 1:
            aM = m
            B_alpha = (bM*-1)
            cM = fifth

        General = (f"{aM}x {B_alpha}y {cM} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {General}\033[0;37;40m\n")

def Equation_of_a_line_that_passes_through_2_points():
    x1, y1 = input("\nEnter the first coordinate \033[0;35;40m(x, y)\033[0;37;40m: ").split()
    x1, y1 = float(x1), float(y1)

    x2, y2 = input("\nEnter the second coordinate \033[0;34;40m(x, y)\033[0;37;40m: ").split()
    x2, y2 = float(x2), float(y2)

    m = ((y2-y1)/(x2-x1))

    first = (-(y1))
    if first <= -1:
        dx = (f"y {first}")
    elif first >= 1:
        dx = (f"y + {first}")
    
    second = (-(x1))
    if second <= -1:
        xd =(f"x {second}")
        #print(xd)
    elif second >= 1:
        xd = (f"x + {second}")
        #print(xd)

    print(f"\nThe formula is:\033[0;32;40m {dx} = {m}({xd})\033[0;37;40m")

    third = (m*second)
    #print(third)
    fourth = (f"{m}x")
    #print(fourth)

    if first <= -1:
        fifth = (third + (first*-1))
        #print(fifth)
    if first >= 1:
        fifth = (third - first)
        #print(fifth)
    
    if m.is_integer() == False and fifth.is_integer() == False:
        m_in_fraction = Fraction(m).limit_denominator()
        string_m_in_fraction = str(Fraction(m).limit_denominator())
        #print(m_in_fraction)
    
    
        fifth_in_fraction = Fraction(fifth).limit_denominator()
        string_fifth_in_fraction = str(Fraction(fifth).limit_denominator())
        #print(fifth_in_fraction)
    
        ordinary = (f"y = {m_in_fraction}x {fifth_in_fraction}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        d1, d2 = string_m_in_fraction.split("/")
        d1, d2 = int(d1), int(d2)
        #print(d1)
        #print(d2)
    
        d3, d4 = string_fifth_in_fraction.split("/")
        d3, d4 = int(d3), int(d4)
        #print(d3)
        #print(d4)
    
        if d2 == d4:
            bM = d2
        elif d2 != d4:
            bM = (d2*d4)

            aM = d1 
            cM = d3

        if aM <= -1:
            aM = (d1*-1)
            B_alpha = bM
            cM = (d3*-1)
        elif aM >= 1:
            aM = d1
            B_alpha = (bM*-1)
            cM = d3

        General = (f"{aM}x {B_alpha}y {cM} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {General}\033[0;37;40m\n")
        
    elif m.is_integer() == True and fifth.is_integer() == False:
    
        fifth_in_fraction = Fraction(fifth).limit_denominator()
        string_fifth_in_fraction = str(Fraction(fifth).limit_denominator())
        #print(fifth_in_fraction)
    
        ordinary = (f"y = {m}x {fifth_in_fraction}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        d3, d4 = string_fifth_in_fraction.split("/")
        d3, d4 = int(d3), int(d4)
        #print(d3)
        #print(d4)
    
        bM =d4 #y value

        aM = m*d4 
        cM = d3

        if aM <= -1:
            aM = ((m*d4)*-1)
            B_alpha = bM
            cM = (d3*-1)
        elif aM >= 1:
            aM = d1
            B_alpha = (bM*-1)
            cM = m*d4

        General = (f"{aM}x {B_alpha}y {cM} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {General}\033[0;37;40m\n")
    
    elif m.is_integer() == False and fifth.is_integer() == True:
        m_in_fraction = Fraction(m).limit_denominator()
        string_m_in_fraction = str(Fraction(m).limit_denominator())
        #print(m_in_fraction)
    
        ordinary = (f"y = {m_in_fraction}x {fifth}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        d1, d2 = string_m_in_fraction.split("/")
        d1, d2 = int(d1), int(d2)
        #print(d1)
        #print(d2)
        
        bM = d2
        

        aM = d1 
        cM = fifth*d2

        if aM <= -1:
            aM = ((fifth*d2)*-1)
            B_alpha = bM
            cM = (d3*-1)
        elif aM >= 1:
            aM = d1
            B_alpha = (bM*-1)
            cM = fifth*d2

        General = (f"{aM}x {B_alpha}y {cM} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {General}\033[0;37;40m\n")
    
    if m.is_integer() == True and fifth.is_integer() == True:
        
        ordinary = (f"y = {m}x {fifth}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")
    
        bM = 1
        
        aM = m
        cM = fifth

        if aM <= -1:
            aM = (m*-1)
            B_alpha = bM
            cM = (fifth*-1)
        elif aM >= 1:
            aM = m
            B_alpha = (bM*-1)
            cM = fifth

        General = (f"{aM}x {B_alpha}y {cM} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {General}\033[0;37;40m\n")

def Symmetric_equation_to_ordinary():
    a1, a2 = input("\nEnter the value of a in fraction \033[0;34;40m / \033[0;37;40m: ").split("/")
    a1, a2 = int(a1), int(a2)
    #print(a1, a2)

    b1, b2 = input("\nEnter the value of b in fraction \033[0;34;40m / \033[0;37;40m: ").split("/")
    b1, b2 = int(b1), int(b2)
    #print(b1, b2)

    a = (a1/a2)
    b = (b1/b2)
    #print(a, b)

    denominator =  (a*b)
    #print(denominator)

    first = (f"{b}x  {a}y / {denominator} = 1")
    print(f"\n\033[0;31;40m{first}\033[0;37;40m")

    second = (f"{b}x  {a}y = {denominator}")
    print(f"\n\033[0;32;40m{second}\033[0;37;40m")

    denominator_other_side = (denominator*-1)
    general = (f"{b}x  {a}y {denominator_other_side} = 0")
    print(f"\nThe general equation is:\033[0;35;40m {general}\033[0;37;40m")

    m = ((-1*b)/a)
    b_de_la_otra = ((-1*denominator_other_side)/a)
    #print(m, b_de_la_otra)

    if m.is_integer() == False and b.is_integer() == False:
        m_in_fraction = Fraction(m).limit_denominator()
        string_m_in_fraction = str(Fraction(m).limit_denominator())
        b_in_fraction = Fraction(b_de_la_otra).limit_denominator()
        string_b_in_fraction = str(Fraction(b_de_la_otra).limit_denominator())
        ordinary = (f"y = {m_in_fraction}x  {b_in_fraction}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m\n")
    elif m.is_integer() == True and b_de_la_otra.is_integer() == False:
        m = int(m)
        b_in_fraction = Fraction(b_de_la_otra).limit_denominator()
        string_b_in_fraction = str(Fraction(b_de_la_otra).limit_denominator())
        ordinary = (f"y = {m}x  {b_in_fraction}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m\n")
    elif m.is_integer() == False and b_de_la_otra.is_integer() == True:
        b_de_la_otra = int(b_de_la_otra)
        m_in_fraction = Fraction(m).limit_denominator()
        string_m_in_fraction = str(Fraction(m).limit_denominator())
        ordinary = (f"y = {m_in_fraction}x  {b_de_la_otra}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m\n")
    elif m.is_integer() == True and b_de_la_otra.is_integer == True:
        m = int(m) 
        b_de_la_otra = int(b_de_la_otra)
        ordinary = (f"y = {m}x  {b_de_la_otra}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m\n")
        
    #p1, p2 = input("Enter the symmetric equation: ").split("+")
    #print(p1, p2)

    #f1, f2 = p1.split("/")
    #f3, f4 = p2.split("/")
    #f2 , f4 = float(f2), float(f4)
    #print(f1, f2) # f2 is the int
    #print(f3, f4) # f4 is the int

    #denominator =  f2*f4
    #print(denominator)

    #first = (f"{f4}x  {f2}y / {denominator} = 1")
    #print(first)

    #second = (f"{f4}x  {f2}y = {denominator}")
    #print(second)

    #denominatorother_side = (denominator*-1)
    #general = (f"{f4}x  {f2}y {denominatorother_side} = 0")
    #print(general)

    #m = ((-1*f4)/f2)
    #b = ((-1*denominatorother_side)/f2)
    #print(m, b)
        
    #if m.is_integer() == False and b.is_integer() == False:
    #    m_in_fraction = Fraction(m).limit_denominator()
    #    string_m_in_fraction = str(Fraction(m).limit_denominator())
    #    b_in_fraction = Fraction(b).limit_denominator()
    #    string_b_in_fraction = str(Fraction(b).limit_denominator())
    #    ordinary = (f"y = {m_in_fraction}x  {b_in_fraction}")
    #    print(ordinary)
    #elif m.is_integer() == True and b.is_integer() == False:
    #    b_in_fraction = Fraction(b).limit_denominator()
    #    string_b_in_fraction = str(Fraction(b).limit_denominator())
    #    ordinary = (f"y = {m}x  {b_in_fraction}")
    #   print(ordinary)
    #elif m.is_integer() == False and b.is_integer() == True:
    #    m_in_fraction = Fraction(m).limit_denominator()
    #    string_m_in_fraction = str(Fraction(m).limit_denominator())
    #    ordinary = (f"y = {m_in_fraction}x  {b}")
    #    print(ordinary)
    #elif m.is_integer() == True and b.is_integer == True:
    #    ordinary = (f"y = {m}x  {b}")
    #    print(ordinary)


    #if m.is_integer() == True and b.is_integer == True:
        #ordinary = (f"y = {m}x - {b}")
        #print(ordinary)
    #elif m.is_integer() == False and b.is_integer() == True:
        #m_in_fraction = Fraction(m).limit_denominator()
        #string_m_in_fraction = str(Fraction(m).limit_denominator())
        #ordinary = (f"y = {m_in_fraction}x - {b}")
        #print(ordinary)
    #elif m.is_integer() == True and b.is_integer() == False:
        #b_in_fraction = Fraction(b).limit_denominator()
        #string_b_in_fraction = str(Fraction(b).limit_denominator())
        #ordinary = (f"y = {m}x + {b_in_fraction}")
        #print(ordinary)
    #elif m.is_integer() == False and b.is_integer() == False:
        #m_in_fraction = Fraction(m).limit_denominator()
        #string_m_in_fraction = str(Fraction(m).limit_denominator())
        #b_in_fraction = Fraction(b).limit_denominator()
        #string_b_in_fraction = str(Fraction(b).limit_denominator())
        #ordinary = (f"y = {m_in_fraction}x + {b_in_fraction}")
        #print(ordinary)    

def general_to_symmetric_equations():
    A1, B1, C1 = input("Enter the value of A, B and C: ").split(" ")

    A2, x_letra = A1.split("x")
    B2, y_letra = B1.split("y")
    C2 = C1

    A, B, C = int(A2), int(B2), int(C2)
    #print(A, B, C)

    if C <= -1 : # C is a negative number
        C_del_otro_lado = (C*-1)
        #print(C_del_otro_lado)

        first = (f"{A}x {B}y = {C_del_otro_lado}")
        print(f"\n\033[0;36;40m{first}\033[0;37;40m")
        second = (f"{A}x/{C_del_otro_lado} {B}y/{C_del_otro_lado} = {C_del_otro_lado}/{C_del_otro_lado}")
        print(f"\n\033[0;35;40m{second}\033[0;37;40m")

        if A != 0 and B != 0: # Both A and B aren't equal to 0
            
            if (C_del_otro_lado/A).is_integer() == True and (C_del_otro_lado/B).is_integer() == True:
                f_A = (C_del_otro_lado/A)
                f_A = int(f_A)

                f_B = (C_del_otro_lado/B)
                f_B = int(f_B)

                symmetric = (f"x/{f_A} y/{f_B} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

            elif (C_del_otro_lado/A).is_integer() == True and (C_del_otro_lado/B).is_integer() == False:
                f_A = (C_del_otro_lado/A)
                f_A = int(f_A)
                
                symmetric = (f"x/{f_A} y/{C_del_otro_lado}/{B} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

            elif (C_del_otro_lado/A).is_integer() == False and (C_del_otro_lado/B).is_integer() == True:
                f_B = (C_del_otro_lado/B)
                f_B = int(f_B)
                
                symmetric = (f"x/{C_del_otro_lado}/{A} y/{f_B} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

            elif (C_del_otro_lado/A).is_integer() == False and (C_del_otro_lado/B).is_integer() == False:
                symmetric = (f"x/{C_del_otro_lado}/{A} y/{C_del_otro_lado}/{B} = {C_del_otro_lado/C_del_otro_lado} ")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

        elif A == 0 and B != 0:
            if (C_del_otro_lado/B).is_integer() == False:
                symmetric = (f"x/{C_del_otro_lado} y/{C_del_otro_lado}/{B} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

            elif (C_del_otro_lado/B).is_integer() == True:
                f_B = (C_del_otro_lado/B)
                f_B = int(f_B)

                symmetric = (f"x/{C_del_otro_lado} y/{f_B} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

        elif A != 0 and B == 0:
            if (C_del_otro_lado/B).is_integer() == False:
                symmetric = (f"x/{C_del_otro_lado}/{A} y/{C_del_otro_lado} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")
                
            elif (C_del_otro_lado/B).is_integer() == True:
                f_A = (C_del_otro_lado/A)
                f_A = int(f_A)
                symmetric = (f"x/{f_A} y/{C_del_otro_lado} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

        elif A == 0 and B == 0:
            symmetric = (f"x/{C_del_otro_lado} y/{C_del_otro_lado} = {C_del_otro_lado/C_del_otro_lado}")
            print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

    if C >= -1 : # C is a positive number
        C_del_otro_lado = (C*-1)
        #print(C_del_otro_lado)

        first = (f"{A}x {B}y = {C_del_otro_lado}")
        print(f"\n\033[0;36;40m{first}\033[0;37;40m")
        second = (f"{A}x/{C_del_otro_lado} {B}y/{C_del_otro_lado} = {C_del_otro_lado}/{C_del_otro_lado}")
        print(f"\n\033[0;35;40m{second}\033[0;37;40m")


        if A != 0 and B != 0: # Both A and B aren't equal to 0
            
            if (C_del_otro_lado/A).is_integer() == True and (C_del_otro_lado/B).is_integer() == True:
                f_A = (C_del_otro_lado/A)
                f_A = int(f_A)

                f_B = (C_del_otro_lado/B)
                f_B = int(f_B)

                symmetric = (f"x/{f_A} y/{f_B} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

            elif (C_del_otro_lado/A).is_integer() == True and (C_del_otro_lado/B).is_integer() == False:
                f_A = (C_del_otro_lado/A)
                f_A = int(f_A)
                
                symmetric = (f"x/{f_A} y/{C_del_otro_lado}/{B} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

            elif (C_del_otro_lado/A).is_integer() == False and (C_del_otro_lado/B).is_integer() == True:
                f_B = (C_del_otro_lado/B)
                f_B = int(f_B)
                
                symmetric = (f"x/{C_del_otro_lado}/{A} y/{f_B} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

            elif (C_del_otro_lado/A).is_integer() == False and (C_del_otro_lado/B).is_integer() == False:
                symmetric = (f"x/{C_del_otro_lado}/{A} y/{C_del_otro_lado}/{B} = {C_del_otro_lado/C_del_otro_lado} ")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

        elif A == 0 and B != 0:
            if (C_del_otro_lado/B).is_integer() == False:
                symmetric = (f"x/{C_del_otro_lado} y/{C_del_otro_lado}/{B} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

            elif (C_del_otro_lado/B).is_integer() == True:
                f_B = (C_del_otro_lado/B)
                f_B = int(f_B)

                symmetric = (f"x/{C_del_otro_lado} y/{f_B} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

        elif A != 0 and B == 0:
            if (C_del_otro_lado/B).is_integer() == False:
                symmetric = (f"x/{C_del_otro_lado}/{A} y/{C_del_otro_lado} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")
                
            elif (C_del_otro_lado/B).is_integer() == True:
                f_A = (C_del_otro_lado/A)
                f_A = int(f_A)
                symmetric = (f"x/{f_A} y/{C_del_otro_lado} = {C_del_otro_lado/C_del_otro_lado}")
                print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

        elif A == 0 and B == 0:
            symmetric = (f"x/{C_del_otro_lado} y/{C_del_otro_lado} = {C_del_otro_lado/C_del_otro_lado}")
            print(f"\nThis is the symmetric equation:\033[0;32;40m {symmetric}\033[0;37;40m\n")

def points_to_general_circumference_equation():
    h, k = input("\nEnter the coordinate \033[0;35;40m(x, y)\033[0;37;40m: ").split()
    h, k = int(h), int(k)

    r = input("\nEnter the radius \033[0;34;40mr\033[0;37;40m: ")
    r = float(r)

    if h <= -1 and k <= -1: # Both are negative
        ordinary = (f"(x + {h*-1})² + (y + {k*-1})² = {r **2}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        F = (((h **2)+(k **2))-(r **2))
        
        general = (f"x² + y² + {2*(h*-1)}x + {2*(k*-1)}y {F} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {general}\033[0;37;40m\n")

    elif h <= -1 and k >= 1: # h is negative and k is positive
        ordinary = (f"(x + {h*-1})² + (y - {k})² = {r **2}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        F = (((h **2)+(k **2))-(r **2))
        
        general = (f"x² + y² + {2*(h*-1)}x  {2*(k)}y {F} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {general}\033[0;37;40m\n")

    elif h >= 1 and k <= -1: # h is positive and k is negative
        ordinary = (f"(x - {h})² + (y + {k*-1})² = {r **2}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        F = (((h **2)+(k **2))-(r **2))
        
        general = (f"x² + y² - {2*(h)}x + {2*(k*-1)}y {F} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {general}\033[0;37;40m\n")

    elif h >= 1 and k >= 1: #Both are positive
        ordinary = (f"(x - {h})² + (y - {k})² = {r **2}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        F = (((h **2)+(k **2))-(r **2))
        
        general = (f"x² + y² - {2*(h)}x - {2*(k)}y {F} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {general}\033[0;37;40m\n")
    
    elif h <= -1 and k == 0: 
        ordinary = (f"(x + {h*-1})² + y² = {r **2}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        F = (((h **2)+(k **2))-(r **2))
        
        general = (f"x² + y² + {2*(h*-1)}x  {F} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {general}\033[0;37;40m\n")

    elif h == 0 and k <= -1: 
        ordinary = (f"x² + (y + {k*-1})² = {r **2}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        F = (((h **2)+(k **2))-(r **2))
        
        general = (f"x² + y² + {2*(k*-1)}y {F} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {general}\033[0;37;40m\n")
    
    elif h >= -1 and k == 0:
        ordinary = (f"(x - {h})² + y² = {r **2}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        F = (((h **2)+(k **2))-(r **2))
        
        general = (f"x² + y² - {2*(h)}x {F} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {general}\033[0;37;40m\n")
    
    elif h == 0 and k >= -1:
        ordinary = (f"x² + (y - {k})² = {r **2}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        F = (((h **2)+(k **2))-(r **2))
        
        general = (f"x² + y² - {2*(k)}y {F} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {general}\033[0;37;40m\n")
    
    elif h == 0 and k == 0:
        ordinary = (f"x² + y² = {r **2}")
        print(f"\nThe ordinary equation is:\033[0;34;40m {ordinary}\033[0;37;40m")

        F = (((h **2)+(k **2))-(r **2))
        
        general = (f"x² + y²0 {F} = 0")
        print(f"\nThe general equation is:\033[0;35;40m {general}\033[0;37;40m\n")

def from_general_to_points():
    D = input("Enter the value of Dx: ")
    E = input("Enter the value of Ey: ")
    F = input("Enter the value of F: ")
    D, E, F = int(D), int(E), int(F)

    if D != 0 and E != 0:
        h = (-1*D)/2
        k = (-1*E)/2

        print(f"\nThe coordinates of the center of the circle are: (\033[0;35;40m{h}\033[0;37;40m, \033[0;34;40m{k}\033[0;37;40m)")

        pre_r = (((h**2) + (k**2))-(F))
        #print(pre_r)
        r = math.sqrt(pre_r)

        print(f"\nThe radius of the circle is: \033[0;32;40m{r}\033[0;37;40m\n")
    
    elif D == 0 and E != 0:
        h = 0
        k = (-1*E)/2
    
        print(f"\nThe coordinates of the center of the circle are: (\033[0;35;40m{h}\033[0;37;40m, \033[0;34;40m{k}\033[0;37;40m)")

        pre_r = (((h**2) + (k**2))-(F))
        #print(pre_r)
        r = math.sqrt(pre_r)

        print(f"\nThe radius of the circle is: \033[0;32;40m{r}\033[0;37;40m\n")
    
    elif D != 0 and E == 0:
        h = (-1*D)/2
        k = 0

        print(f"\nThe coordinates of the center of the circle are: (\033[0;35;40m{h}\033[0;37;40m, \033[0;34;40m{k}\033[0;37;40m)")

        pre_r = (((h**2) + (k**2))-(F))
        #print(pre_r)
        r = math.sqrt(pre_r)

        print(f"\nThe radius of the circle is: \033[0;32;40m{r}\033[0;37;40m\n")
    
    elif E == 0 and F == 0:
        h = 0
        k = 0

        print(f"\nThe coordinates of the center of the circle are: (\033[0;35;40m{h}\033[0;37;40m,\033[0;34;40m{k}\033[0;37;40m)")

        pre_r = (((h**2) + (k**2))-(F))
        #print(pre_r)
        r = math.sqrt(pre_r)

        print(f"\nThe radius of the circle is: \033[0;32;40m{r}\033[0;37;40m\n")

Symmetric_equation_to_ordinary()