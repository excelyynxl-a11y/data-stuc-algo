import math

#%% counting sort helper ot be used in radix sort
def helper_count_sort(new_list, col, base = 10):
    print('Unsorted list = ', new_list)
    n = len(new_list)
    sorted_output = [0] * n
    print('Initial sorted output: ', sorted_output)

    # initialise count-array (hashed table with separate chaining - list of list)
    count_array = [None] * base  
    for i in range(len(count_array)):
        count_array[i] = []
    print('Initial count-array: ', count_array)

    # update count-array with frequency
    for i in range(n):
        item = new_list[i]
        index = (item // base ** col) % base
        count_array[index].append(item)
    print('Raw count-array: ', count_array)

    # 'pop' out each element in count_array and orderly insert into sorted list
    index = 0
    for i in range(len(count_array)):
        inner_chain = count_array[i]
        print('Processing inner_chain ', inner_chain)
        for j in range(len(inner_chain)):
            sorted_output[index] = inner_chain[j]
            index += 1
        print('Sorted output: ', sorted_output)

    print('FINAL SORTED OUTPUT FROM HELPER: ', sorted_output)
    # return the modified sorted input list 
    return sorted_output 
    
def determine_number_of_cols(x, z):
    '''
    Precondition: 
    - x must be a number of base 10
    - x must be greater than 0 
    - z is the base and must be greater than 1
    '''
    log10_x = math.log(x)
    log10_z = math.log(z)
    number_of_cols = math.floor((log10_x / log10_z)) + 1
    return number_of_cols

def radix_sort(new_list, base = 10):

    # find the maximum item from input list 
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item
    print('Max item in input list: ', max_item)

    number_of_cols = determine_number_of_cols(max_item, base)
    for i in range(number_of_cols):
        print('===== Processing column ', i, ' of base ', base, '=====')
        new_list = helper_count_sort(new_list, i, base)
        
    return new_list 

#%% driver 
list_test_radix = [4329, 5169, 4321, 3369, 2121, 2099]
print('Unsorted list: ', list_test_radix)
list_test_radix = radix_sort(list_test_radix, 5)
print('Radix sorted list: ', list_test_radix)

#%% driver
list_test_radix = [200, 151, 291, 981, 369, 421, 671]
print('Unsorted list: ', list_test_radix)
list_test_radix = radix_sort(list_test_radix, 10)
print('Sorted list: ', list_test_radix)

def helper_count_sort_alpha(new_list, col, base = 26):
    n = len(new_list)
    alpha_ord_array = [0] * n 

    for i in range(n):
        word = new_list[i]
        print(word)
        if (len(word) > col):
            alpha = word[len(word) - col - 1]
            print(alpha)
            alpha_ord = ord(alpha) - 97
            alpha_ord_array[i] = alpha_ord 
        else:
            alpha_ord_array[i] = -1
            
    print('Alpha ord array: ', alpha_ord_array)

    n = len(alpha_ord_array)
    sorted_output = [''] * n
    print('Initial sorted output: ', sorted_output)

    # initialise count-array (hashed table with separate chaining - list of list)
    count_array = [None] * base  
    for i in range(len(count_array)):
        count_array[i] = []
    print('Initial count-array: ', count_array)

    # update count-array with frequency
    for i in range(n):
        item = new_list[i]
        index = alpha_ord_array[i]
        count_array[index].append(item)
    print('Raw count-array: ', count_array)

    # 'pop' out each element in count_array and orderly insert into sorted list
    index = 0
    for i in range(len(count_array)):
        inner_chain = count_array[i]
        print('Processing inner_chain ', inner_chain)
        for j in range(len(inner_chain)):
            sorted_output[index] = inner_chain[j]
            index += 1
        print('Sorted output: ', sorted_output)

    print('FINAL SORTED OUTPUT FROM HELPER: ', sorted_output)
    # return the modified sorted input list 
    return sorted_output 

def radix_sort_alpha_noob(new_list):
    '''
    Time complexity: 
    - adding and removing paddings creates a lot of work and increases complexity
    - 
    '''
    return new_list

def radix_sort_alpha_intermediate(new_list):
    '''
    Time complexity: 
    - improvement by avoiding padding
    - abuse the use of length of each words
    '''
    n = len(new_list)

    # count length of all words in input list
    words_length_array = [0] * n 
    for i in range(n):
        word = new_list[i]
        word_length = len(word)
        words_length_array[i] = word_length
    print('Word length array: ', words_length_array)

    for i in range()



           

    return new_list

def radix_sort_alpha_pro(new_list):
    '''
    Time complexity: O(T), where T is the total length of all words in new_list
    '''
    return new_list

#%% driver 
list_test_radix = ['gudetame', 'cat', 'taro', 'tags', 'gitgud', 'food']
print('Test helper_sort_test_alpha', helper_count_sort_alpha(list_test_radix, 0))
print('Unsorted list: ', list_test_radix)
list_test_radix = radix_sort_alpha_noob(list_test_radix, )
print('Radix sorted list: ', list_test_radix)
print(ord("a")) # 97