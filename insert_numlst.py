def insert_num(lst,number,counter=0):
    """
    Objective : To insert a given number in a sorted list
    Input parameters :
                        lst -> Given sorted list
                        number -> number to be inserted in the sorted list
                        counter -> index counter for inserting purpose
    Return : Sorted list with the number
    Approach : Using recursion
    """
    if(number<lst[counter]):
        lst.insert(counter,number)
        return lst
    elif counter==len(lst):
        lst.append(number)
    else:
        return insert_num(lst,number,counter+1)
    
def main():
    """
    Objective : To insert a given number in a sorted list
    Return : Sorted list with the number
    Approach : Using insert_sum function
    """
    lst=[1,3,4,8,10]
    print(lst)
    number=int(input("Enter the number to be inserted in the list "))
    insert_num(lst,number)
    print(lst)
    
if __name__=="__main__":
    main()
    print("End of program")
