import math

def distance_between_two_points():
    x1, y1 = input("\nEnter the first coordinate (x, y): ").split()
    x1, y1 = float(x1), float(y1)

    x2, y2 = input("Enter the second coordinate (x, y): ").split()
    x2, y2 = float(x2), float(y2)
    
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(f"The distance between the two points is: \033[0;32;40m{distance} u \033[0;37;40m")