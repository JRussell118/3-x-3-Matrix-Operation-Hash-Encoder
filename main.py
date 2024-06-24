"""This program reads and validates a phone number and zipcode from the user,
and performs the specified operation with two 3x3 matrices from the user."""
import numpy as np


def print_mean(result):
    """Prints the mean of the rows and columns in result"""
    print("The row and column mean values of the results are:")
    np.set_printoptions(precision=2)
    print(f"Rows: {np.mean(result, axis=0)}")
    print(f"Columns: {np.mean(result, axis=1)}")


def print_trans(result):
    """Prints the transpose of the result"""
    print("The Transpose is:")
    print(result.transpose())


def element_mul(first_m, second_m):
    """Calculates the multiplication of the elements of first_m
    and second_m, then prints and returns the product"""
    print("You selected Element Multiplication. The results are:")
    product_m = first_m * second_m
    print(product_m)
    return product_m


def matrix_mul(first_m, second_m):
    """Calculates the multiplication of the matrices of first_m
    and second_m, then prints and returns the product"""
    print("You selected Matrix Multiplication. The results are:")
    product_m = np.matmul(first_m, second_m)
    print(product_m)
    return product_m


def matrix_sub(first_m, second_m):
    """Calculates the subtraction of the elements of first_m
    and second_m, then prints and returns the difference"""
    print("You selected Subtraction. The results are:")
    diff_m = first_m - second_m
    print(diff_m)
    return diff_m


def matrix_add(first_m, second_m):
    """Calculates the addition of the elements of first_m
    and second_m, then prints and returns the sum"""
    print("You selected Addition. The results are:")
    sum_m = first_m + second_m
    print(sum_m)
    return sum_m


def get_matrix():
    """Creates and returns a 3x3 matrix using list inputs from the user"""
    print("Enter your 3x3 matrix:")
    check = 0
    list1 = []
    list2 = []
    list3 = []
    while check == 0:
        try:
            list1 = list(map(int, input().split()))
            list2 = list(map(int, input().split()))
            list3 = list(map(int, input().split()))
            check = 1
        except ValueError:
            print("The values you entered were invalid. Please re-enter.")

    matrix = np.array([list1, list2, list3])
    np.reshape(matrix, (3, 3))
    return matrix


def get_input():
    """Gets and returns an input from the user"""
    user_in = input()
    while user_in not in ('n', 'y', 'Y', 'N'):
        print("Your input was invalid, please re-enter.")
        user_in = input()
    return user_in


def get_zip():
    """Gets and validates a zipcode input from the user"""
    print("Please enter your zipcode + 4. (XXXXX-XXXX)")
    num = input()
    while len(num) < 10 or num.find('-') == -1 or not num.replace('-', '').isdigit():
        print("Your zipcode is not in correct format. Please re-enter.")
        num = input()
    return num


def get_phone():
    """Gets and validates a phone number input from the user"""
    print("Please enter your phone number. (XXX-XXX-XXXX)")
    num = input()
    while len(num) < 12 or num.find('-') == -1 or not num.replace('-', '').isdigit():
        print("Your phone number is not in correct format. Please re-enter.")
        num = input()
    return num


def main():
    """Defines the code of the program in main"""
    print(f"{'Welcome to the Matrix Expression Program':*^100}")
    print("Do you want to use this program?(y/n)")
    choice = get_input()
    while choice not in ('n', 'N'):
        p_num = get_phone()

        z_num = get_zip()

        matrix1 = get_matrix()

        print("Your first 3x3 matrix is:")
        print(matrix1)

        matrix2 = get_matrix()

        print("Your second 3x3 matrix is:")
        print(matrix2)

        print("Select a Matrix Operation from the list below:")
        print("a. Addition\nb. Subtraction\nc. Matrix Multiplication")
        print("d. Element by element multiplication")

        o_choice = ''
        result_m = []
        while o_choice not in ('a', 'A', 'b', 'B', 'c', 'C', 'd', 'D'):
            o_choice = input()
            if o_choice in ('a', 'A'):
                result_m = matrix_add(matrix1, matrix2)
            elif o_choice in ('b', 'B'):
                result_m = matrix_sub(matrix1, matrix2)
            elif o_choice in ('c', 'C'):
                result_m = matrix_mul(matrix1, matrix2)
            elif o_choice in ('d', 'D'):
                result_m = element_mul(matrix1, matrix2)
            else:
                print("Please enter one of the valid choices.")

        print_trans(result_m)
        print_mean(result_m)

        print("Do you still want to use this program?(y/n)")
        choice = get_input()

    print(f"{'Thank you for using this program. Goodbye!':*^100}")


main()
