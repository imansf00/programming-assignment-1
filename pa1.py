import math

def sa_cube(length):
    return 6 * (length**2)
def v_cube(length):
    return length**3
def sa_cylinder(radius, height):
    return (math.pi * (radius**2) * 2) + (2 * math.pi * radius * height)
def v_cylinder(radius, height):
    return math.pi*(radius**2)*height
def sa_rp(length,width,height):
    return (2*length*width) + (2*length*height) + (2*width*height)
def v_rp(length,width,height):
    return length*width*height
def v_sphere(radius):
    return 4/3*math.pi*(radius**3)
def sa_sphere(radius):
    return 4*math.pi*(radius**2)
def sa_cone(radius,slant):
    return (math.pi*radius*slant) + (math.pi*(radius**2))
def v_cone(radius,height):
    return 1/3*math.pi*(radius**2)*height
def main():
    print ("""
1. Cube
2. Cylinder
3. Rectangle (prism)
4. Sphere
5. Cone
          """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        length = float(input("Enter side length value: "))
        print("The surface area of the cube is %d" %(sa_cube(length)))
        print("The volume of the cube is %d" %(v_cube(length)))
    elif choice == 2:
        radius = float(input("Enter the radius value: "))
        height = float(input("Enter the height value: "))
        print("The surface area of the cylinder is %d" %(sa_cylinder(radius,height)))
        print("The volume of the cylinder is %d" %(v_cylinder(radius,height)))
    elif choice == 3:
        length = float(input("Enter the length of the prism: "))
        width = float(input("Enter the width of the prism: "))
        height = float(input("Enter the heigh of the prism: "))
        print("The surface area of the prism is %d" %(sa_rp(length,width,height)))
        print("The volume of the prism is %d" %(v_rp(length,width,height)))
    elif choice == 4:
        radius=float(input("Enter the radius value: "))
        print("The surface area of the sphere is %d" %(sa_sphere(radius)))
        print("The volume of the sphere is %d" %(v_sphere(radius)))
    elif choice == 5:
        radius=float(input("Enter the radius value: "))
        height=float(input("Enter the height value: "))
        slant=float(input("Enter the slant value: "))
        print("The surface area of the cone is %d" %(sa_cone(slant,radius)))
        print("The volume of the cone is %d" %(v_cone(height,radius)))
    else:
        print ("Please enter a relevant choice")
        pass
        
l=1
while l==1:
    main()
