def area_rectangle(length,breadth):
    """
    Objective : to find the area of a rectangle 
    Input parameters : length - length of the rectangle
                     : breadth - breadth of the rectangle
    Return : area of the rectangle
    Approach : multiplying length and breadth
    """
    area = length * breadth
    return area
def main():
    '''
    Objective : To compute the area of a rectangle.
    User Inputs : 
    length: length of the rectangle.
    breadth: breadth of the rectangle.
    Approach : Use of areaRectangle function.
    Return : value of the area of rectangle.
    '''
    length = int(input("Enter the length of rectangle : "))
    breadth = int(input("Enter the breadth of rectangle : "))
    area_rectangle(length,breadth)
    print("The area of the rectangle is ",area_rectangle(length,breadth))
if __name__=="__main__":
    main()
    print("End of program!")
