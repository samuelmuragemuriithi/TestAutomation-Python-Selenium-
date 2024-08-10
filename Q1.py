"""
1. Problem-solving with Python

Write a python program that reads a list of integers from the console, remove all duplicates, sort the list in 
descending order, and prints the result.
"""
def process_integers():
    # Read a list of integers from the console
    input_str = input("Enter a list of integers separated by spaces: ")
    
    # Convert the input string to a list of integers
    int_list = list(map(int, input_str.split()))
    
    # Remove duplicates by converting the list to a set, then back to a list
    unique_int_list = list(set(int_list))
    
    # Sort the list in descending order
    unique_int_list.sort(reverse=True)
    
    # Print the result
    print("Processed list:", unique_int_list)

# Call the function to execute
process_integers()
