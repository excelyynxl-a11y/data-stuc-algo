#%% UNSTABLE counting sort for integers
def sort_counting(new_list):
    '''
    Precondition: new_list must have at least one element. All element must be numeric.
    '''
    # find the maximum from input array
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item
    print('Max item in input list: ', max_item) 
    
    # initialized count-array 
    count_array = [0] * (max_item + 1)
    print('Initial count-array: ', count_array)

    # update count-array [represent a | itemId | frequency | table]
    for item in new_list:
        count_array[item] += + 1
    print('Count-array: ', count_array)

    # update input array
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            new_list[index] = item 
            index += 1 

    # return the sorted input array
    return new_list


#%% driver
print('=== UNSTABLE COUNTING SORT ===')
list_a = [6, 3, 1, 7, 2, 8, 1, 7]
print('Unsorted list: ', list_a)
list_a = sort_counting(list_a)
print('Sorted list: ', list_a)

#%% counting sort for alphabets
def sort_counting_alpha(new_alpha_list):
    '''
    Prerequisite: new_alpha_list must be a list with at least one element. All element can be of alphabets
    '''
    # find the maximum from input list 
    max_item = ord(new_alpha_list[0]) - 97
    for item in new_alpha_list:
        item = ord(item) - 97
        if item > max_item:
            max_item = item 
    print('Max item: ', max_item)

    # initialized count-array 
    count_array = [0] * (max_item + 1)
    print('Initial count-array: ', count_array)
    
    # update count-array
    for item in new_alpha_list:
        count_array[ord(item) - 97] += 1
    print('Count-array: ', count_array)

    # update input list
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            new_alpha_list[index] = chr(item + 97) 
            index += 1
    
    # return sorted input list 
    return new_alpha_list 


#%% driver 
print('=== UNSTABLE COUNTING SORT for ALPHABETS ===')
alpha_list = ['a', 'b', 'a', 'c', 'x', 'a']
for alp in alpha_list:
    print(alp, ' converted to ord = ', ord(alp))
print('Unsorted alpha list: ', alpha_list)
alpha_list = sort_counting_alpha(alpha_list)
print('Sorted alpha list: ', alpha_list)
for alp in alpha_list:
    print(alp, ' converted to ord = ', ord(alp))


#%% STABLE counting sort
def stable_sort_counting(new_list):
    # find the maximum in input list 
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item
    print('Maximum value: ', max_item)

    # initialise count-array that mimics a hashed table with separate chaining (list of list)
    count_array = [None] * (max_item + 1)
    for i in range(len(count_array)):
        count_array[i] = []
    print('Initial count-array: ', count_array)

    # update the count-array 
    for item in new_list:
        count_array[item].append(item)
    print('Count-array: ', count_array)

    # update input list 
    index = 0 
    for i in range(len(count_array)):
        chain = count_array[i]
        for item in chain:
            new_list[index] = item 
            index += 1 

    # return sorted list 
    return new_list
        

#%% driver
print('=== STABLE COUNTING SORT ===')
list_a = [6, 3, 1, 7, 2, 8, 1, 7]
print('Unsorted list: ', list_a)
list_a = stable_sort_counting(list_a)
print('Sorted list: ', list_a)