import numpy as np
import random
import matplotlib.pyplot as plt 
from matplotlib import style


def main():
    max_range = 100
    min_range = 1
    size_of_set = 10000
    # For numbers 1-100, cannot raise more than to the power of 4 or else numbers become negative and int overflow issues arrise
    expontial_raise = 3

    # Creating randomly generate set of ints
    test_set = np.random.randint(min_range, max_range, size_of_set)

    # Parsing first digit from the set and then finding number frequency
    first_test = count_first(test_set)
    print(f"Original set: {first_test}")

    # Above repeated for exponentially raised set
    raised_set = raise_exponentially(test_set, expontial_raise)
    second_test = count_first(raised_set)
    print(f"Raised set: {second_test}")
    
    # Mapping the result
    map_dict(first_test, 'Original Set')
    map_dict(second_test, 'Raised Set')
    # map_dict(first_test, 'Original Test,=', second_test, 'Raised test')

def count_first(test_set):
    # Instead of creating empty dict to be filled by unordered set:
    # ex: count = {} or count = dict()    
    # This creates a dict with keys already converted to str and ordered from 1-10 so result will be ordered: 
    # dict is created with key i : 0 and only after the dict is initiated with that structure is the in-line loop initiated to repeat range of i 
    # 1-10. And then i is cast as str.
    count = {str(i): 0 for i in range(1,9)}

  
    # Cannot slice an int, each num must be cast to str first to use the slice function
    first_digits = [(str(num)[0]) for num in test_set]

    for digit in first_digits :

        # -----
        # This line replaces this whole for loop:
        # Such common syntax that get function was created to replace this...
        # for digit in first_digits:
        #     if digit not in count:
        #         count[digit] = 1
        #     else:
        #         count[digit] += 1
        count[digit] = count.get(digit, 0) + 1
   
    return count


def raise_exponentially(original_set, e):
    raised_list = original_set**e
   
    return raised_list


def map_dict(set, legend_label):
    plt.bar(list(set.keys()), list(set.values()), label=legend_label, width=0.5)
    
    plt.title('First Digit Distributions')
    plt.xlabel('First Digit')
    plt.ylabel('Frequency')
    plt.legend()

    plt.show

# def map_dict(set1, legend1, set2, legend2):
#     x = np.arange(len(set1))
#     width = 0.5
#     fig, ax = plt.subplots()
#     graph1 = ax.bar(x - width/2, set1.values, width, label=legend1)
#     graph2 = ax.bar(x + width/2, set2.values, width, label=legend2)

#     plt.title('First Digit Distributions')
#     plt.xlabel('First Digit')
#     plt.ylabel('Frequency')
#     plt.legend()

#     plt.show

def compare_frequencies(set1, set2):
    ...

main()