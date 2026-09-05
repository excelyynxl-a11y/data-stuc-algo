def quick_select_partioning_helper(new_list, low, high):
    print('new_list: ', new_list)
    pivot_index = low
    pivot = new_list[pivot_index]
    print('Pivot: ', pivot)
    l_bad = low + 1
    print('Initial l_bad element: ', new_list[l_bad])
    r_bad = high
    print('Initial r_bad element: ', new_list[r_bad])

    while True:
        print('l_bad = ', l_bad)
        while l_bad <= r_bad and new_list[l_bad] <= pivot:
            l_bad += 1 
            print('l_bad = ', l_bad)
        print('r_bad = ', r_bad)
        while r_bad >= l_bad and new_list[r_bad] > pivot:
            r_bad -= 1 
            print('r_bad = ', r_bad)

        if l_bad > r_bad:
            break 
        else:
            print('Swapping l_bad = ', l_bad, ' and r_bad = ', r_bad)
            new_list[l_bad], new_list[r_bad] = new_list[r_bad], new_list[l_bad]
            l_bad += 1 
            r_bad -= 1

        print(new_list)

    print('Swapping pivot_index = ', pivot_index, ' and r_bad = ', r_bad)
    new_list[pivot_index], new_list[r_bad] = new_list[r_bad], new_list[pivot_index]
    print(new_list) 

    print('r_bad returned = ', r_bad)
    return r_bad

def quick_select(new_list, k, low = 0, high = None):
    n = len(new_list)

    if high is None:
        high = n - 1

    if n <= 1 or n == len(new_list):
        return new_list
    
    pivot_index = quick_select_partioning_helper(new_list, low, high)

    if pivot_index + 1 < k:
        print('Target k = ', k)
        print('QuickSelect again on RIGHT SIDE')
        return quick_select(new_list, k, pivot_index + 1, high)
    elif pivot_index + 1 > k:
        print('Target k = ', k)
        print('QuickSelect again on LEFT SIDE')
        return quick_select(new_list, k, low, pivot_index - 1)
    else:
        print('Next pivot_index = ', pivot_index)
        print('Target k = ', k)
        print('Top k-th smallest element: ', new_list[0:k]) 

    return new_list[0:k]

#%% driver 
list_a = [5, 8, 9, 1, 3, 2, 7, 6]
list_b = [2, 8, 9, 1, 3, 5, 7, 6]
list_c = [8, 6, 4, 3, 2, 3]
list_d = []
print('Original list: ', list_a)
print('QuickSelect: ', quick_select(list_a, 0))

def find_k_closest