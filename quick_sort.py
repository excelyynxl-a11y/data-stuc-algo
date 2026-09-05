def naive_quick_sort(new_list):
    left_list = []
    right_list = []



    return new_list 

#%% driver
list_a = [4, 8, 6, 2, 1, 7, 3, 5]
list_b = [1, 4, 3, 4, 1]
list_c = [8, 6, 4, 3, 2, 3]
list_d = []
print('Unsorted list: ', list_c)
# print('Naive partioning helper output: ', naive_partioning_helper(list_c))
print('Sorted list: ', naive_quick_sort(list_c))

def hoare_quick_sort(new_list, low = None, high = None):

    n = len(new_list)

    if low is None: 
        low = 0

    if high is None:
        high = n - 1

    # terminate once low equals or exceed high
    if low >= high:
        return new_list

    # find new pivot_index after swapping via hoare_partioning
    pivot_index = hoare_partioning_helper(new_list, low, high)

    # quicksort the LEFT SIDE
    hoare_quick_sort(new_list, low, pivot_index - 1)

    # quicksort the RIGHT SIDE
    hoare_quick_sort(new_list, pivot_index + 1, high)
    
    return new_list 

def hoare_partioning_helper(new_list, low, high):
    '''
    Partition ONLY the section -- new_list[low....high], not the entire new_list itself
    '''
    n = len(new_list)

    # first element as default pivot
    pivot_index = low 
    pivot = new_list[pivot_index]
    print('Pivot: ', pivot)

    # l_bad is next element after pivot
    l_bad = low + 1
    print('Initial l_bad element: ', new_list[l_bad])

    # r_bad is last element of section
    r_bad = high
    print('Initial r_bad element: ', new_list[r_bad])

    while True:
        # keep pushing l_bad to right side until it finds an element > pivot
        while l_bad <= r_bad and new_list[l_bad] <= pivot:
            l_bad += 1 
            print('l_bad = ', l_bad)

        # keep pushing r_bad to left until it finds an element <= pivot
        while r_bad >= l_bad and new_list[r_bad] > pivot:
            r_bad -= 1 
            print('l_bad = ', l_bad)

        # exit while-loop one l_bad and r_bad cross each other
        if l_bad > r_bad:
            break 
        else:
            # swap l_bad and r_bad
            new_list[l_bad], new_list[r_bad] = new_list[r_bad], new_list[l_bad]

            # increment l_bad and r_bad
            l_bad += 1 
            r_bad -= 1

        print(new_list)

    # final swap r_bad and pivot_index to place pivot in the correct position
    # all element to LEFT SIDE of pivot are <= pivot, all element to RIGHT SIDE of pivot are > pivot
    new_list[pivot_index], new_list[r_bad] = new_list[r_bad], new_list[pivot_index]

    # return r_bad as the new pivot
    return r_bad

#%% driver 
list_a = [4, 8, 6, 2, 1, 7, 3, 5]
list_b = [1, 4, 3, 4, 1]
list_c = [8, 6, 4, 3, 2, 3]
list_d = []
print('Unsorted list: ', list_c)
# print('Hoare partioning helper output: ', hoare_partioning_helper(list_c))
print('Sorted list: ', hoare_quick_sort(list_c))

def lumuto_quick_sort(new_list):

    return new_list

#%% driver 
list_a = [4, 8, 6, 2, 1, 7, 3, 5]
list_b = [1, 4, 3, 4, 1]
list_c = [8, 6, 4, 3, 2, 3]
list_d = []
print('Unsorted list: ', list_c)
# print('Lumuto partioning helper output: ', hoare_partioning_helper(list_c))
print('Sorted list: ', lumuto_quick_sort(list_c))
