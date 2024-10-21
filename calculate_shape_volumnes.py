import math 

def calculate_volume(shpe, req):
        if shpe == "S" or shpe == "s": #sphere
            volume = (4/3)* math.pi * req**3
        elif shpe == "C" or shpe == "c": #cube 
            volume = req**3
        elif shpe == "L" or shpe == "l": #cylinder
            h = req[0]
            r = req[1]
            volume = math.pi * h * (r**2)
        return volume

print("What shape do you want to calculate the volume of? Choices are S, C and L for Sphere, Cube and Cylinder \n")
shpe = input("Input S, C or L (case insensitive) ")

if shpe == "S" or shpe == "s": #sphere
    req = float(input("Give me the radius: "))
    if req <= 0:
        print("I'm sorry, but that isn't valid. Exiting now.")
    else:
        print("The volume is ", calculate_volume(shpe, req))
elif shpe == "C" or shpe == "c": #cube 
    req = float(input("Give me the side: "))
    if req <= 0:
        print("I'm sorry, but that isn't valid. Exiting now.")
    else:
        print("The volume is ", calculate_volume(shpe, req))
elif shpe == "L" or shpe == "l": #cylinder
    h = float(input("Give me the height: "))
    r = float(input("Give me the radius: "))
    req = [h,r]
    if req[0] <= 0 or req[1] <= 0:
        print("I'm sorry, but that isn't valid. Exiting now.")
    else:
        print("The volume is ", calculate_volume(shpe, req))
else:
    print("Shape is not defined.")
        


