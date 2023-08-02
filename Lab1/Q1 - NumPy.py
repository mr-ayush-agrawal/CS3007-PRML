import numpy as np

# Making Menu for the operation
def menu():
    print("Main Menu.....")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Scalar Matrix Multiplication")
    print("4. Elementwise Matrix Multiplication")
    print("5. Matrix Multiplication")
    print("6. Matrix Transpose")
    print("7. Trace of a Matrix")
    print("8. Solve System of Linear Equations")
    print("8. Solve System of Linear Equations")
    print("9. Determinant")
    print("10. Inverse")
    print("11. Eigen Value and Eigen Vector")
    print("12. Exit")

    choice = int(input("Select the option from the above menu "))

    if choice == 1 :
        result = Addition()
    elif choice ==2 :
        result = Subtraction()
    elif choice ==3 :
        result = Scalar()
    elif choice ==4 :
        result = ElMulti()
    elif choice ==5 :
        result = Multiplication()
    elif choice ==6 :
        result = Transpose()
    elif choice ==7 :
        result = Trace()
    elif choice ==9 :
        result = Determinant()
    elif choice ==10 :
        result = Inverse()
    elif choice ==11 :
        result = Eigen()
    elif choice ==12 :
        exit()
    else :
        print("Select a valid operation ")
        return

 
    print("The result of the operation is \n", result)
    
    return

def Addition():
    """
    This allows the user to Enter 2 matrices and return the sum of the Matrices
    """

    print("You have selected the Addition ")
    M = int(input("Enter the number of rows in the matrix "))
    N = int(input("Enter the number of columns in the matrix "))

    try :
        ele = input(f"Enter the {M*N} elements of the matrix 1, seprated by ',' ").split(",")
        ele = [int(x) for x in ele]
        Matrix1 = np.array(ele).reshape(M,N)
    except :
        print("Your elements doesn't match the numbers of elements in the matrix ")
        return None

    try :
        ele = input(f"Enter the {M*N} elements of the matrix 2, seprated by ',' ").split(",")
        ele = [int(x) for x in ele]
        Matrix2 = np.array(ele).reshape(M,N)
    except :
        print("Your elements doesn't match the numbers of elements in the matrix ")
        return None

    return Matrix1 + Matrix2


def Subtraction():
    """
    This allows the user to Enter 2 matrices and return the diffence of the Matrices
    """

    print("You have selected the Subtraction ")
    M = int(input("Enter the number of rows in the matrix "))
    N = int(input("Enter the number of columns in the matrix "))

    try :
        ele = input(f"Enter the {M*N} elements of the matrix 1, seprated by ',' ").split(",")
        ele = [eval(x) for x in ele]
        Matrix1 = np.array(ele).reshape(M,N)
    except :
        print("Your elements doesn't match the numbers of elements in the matrix ")
        return None

    try :
        ele = input(f"Enter the {M*N} elements of the matrix 2, seprated by ',' ").split(",")
        ele = [eval(x) for x in ele]
        Matrix2 = np.array(ele).reshape(M,N)
    except :
        print("Your elements doesn't match the numbers of elements in the matrix ")
        return None

    return Matrix1 - Matrix2

def Scalar():
    """
    This allows the user to Enter a matrix and return the scalar multiplicaton with a entered number
    """

    print("You have selected the Scalar Matrix Multiplication ")
    M = int(input("Enter the number of rows in the matrix "))
    N = int(input("Enter the number of columns in the matrix "))

    try :
        ele = input(f"Enter the {M*N} elements of the matrix, seprated by ',' ").split(",")
        ele = [eval(x) for x in ele]
        Matrix1 = np.array(ele).reshape(M,N)
    except :
        print("Your elements doesn't match the numbers of elements in the matrix ")
        return None

    slr = int(input("Enter the scalar you want to multiply to the matrix "))

    return Matrix1 * slr

def ElMulti():
    """
    This allows the user to Enter 2 matrices and return the Element wise multiplication of the matrix
    """

    print("You have selected the Subtractionf ")
    M = int(input("Enter the number of rows in the matrix "))
    N = int(input("Enter the number of columns in the matrix "))

    try :
        ele = input(f"Enter the {M*N} elements of the matrix 1, seprated by ',' ").split(",")
        ele = [eval(x) for x in ele]
        Matrix1 = np.array(ele).reshape(M,N)
    except :
        print("Your elements doesn't match the numbers of elements in the matrix ")
        return None

    try :
        ele = input(f"Enter the {M*N} elements of the matrix 2, seprated by ',' ").split(",")
        ele = [eval(x) for x in ele]
        Matrix2 = np.array(ele).reshape(M,N)
    except :
        print("Your elements doesn't match the numbers of elements in the matrix ")
        return None

    return Matrix1 * Matrix2






if __name__ == "__main__" :
    menu()
