import numpy as np
import matplotlib.pyplot as plt

# Setting limits for array

set_size = 10000
low_random_range = 1
high_random_range = 100

# Creates the array
array = np.random.randint(low_random_range, high_random_range, set_size)

print("Original array: ", array)

def count_first_digit(array):
    # Define a dictionary to store the count of each first digit
    count = {str(i): 0 for i in range(1, 10)}

    # Iterate through the array
    for num in array:
        # Get the first digit of the number
        first_digit = str(num)[0]
        # Increment the count of this digit
        if first_digit in count:
            count[first_digit] += 1


    
    # Return the count of each first digit
    return count


# Test the function with a small array

print("Original array count: ")

print(count_first_digit(array))

raised_array = array**2
print("\nOriginal array raised: ")
print(count_first_digit(raised_array))
raised_dict = count_first_digit(raised_array)
# plt.bar(raised_dict.values, raised_dict.keys)

# plt.bar(count_first_digit(raised_array), range(1,10))
# plt.show()

################################################################################################################################################################################################################################################################################

# Now running same script but with exponental raise of the numbers in the array 

# Should be done in numpy, but since it won't import, pandas code is below
array_created_exponentially = np.random.randint(low_random_range, high_random_range, set_size)**3

print("\nExponentially raised array", array)

# Test the function with a small array
print("\nExponentially raised counts: " )
print(count_first_digit(array_created_exponentially))

# TODO: Use matplotlib to chart out the values of both