def area_triangle(base,height):
    """
    Objective : to find the area of a triangle
    Input parameters : base -> length of the base of triangle
                       height -> height of the triangle
    Return value : area of the triangle
    Approach : multiplying base and height and dividing by two
    """
    area = base * height / 2
    return area
def main():
    """
    Objective : to find the area of a triangle
    Input parameters : base -> length of the base of triangle
                       height -> height of the triangle
    Return value : area of the triangle
    Approach : calling the area_triangle function
    """
    base = int(input("Enter the length of the base of the triangle : "))
    height = int(input("Enter the height of the triangle : "))
    print("Area of the triangle with base ",base," and height ",height," is ",area_triangle(base,height))
    
if __name__=="__main__":
    main()
    print("End of program")
