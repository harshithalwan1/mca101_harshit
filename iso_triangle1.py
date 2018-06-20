def iso_triangle(sy,blank_spc=5,draw=1):
    """
    Objective : to draw a isosceles triangle
    Input parameters : 
                       sy -> symbol to be used to draw the triangle
    Approach : using recursion
    """
    print(' '*blank_spc + sy*draw)
    if(blank_spc>0):
        iso_triangle(sy,blank_spc-1,draw+2)
def main():
    """
    Objective : to draw a isosceles triangle
    Input parameters : 
                       sy -> symbol to be used to draw the triangle
    Approach : calling iso_triangle function
    """
    sy = input("Enter the symbol to be used for drawing triangle : ")
    iso_triangle(sy)
if __name__=="__main__":
    main()
    print("End program")
    
