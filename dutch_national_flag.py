def dutch_national_flag(new_list):
    '''
    Dutch RED_WHITE_BLUE National Flag algorithm.
    Use in QuickSort to enable 3-ways partitioning [< pivot || = pivot || > pivot]
    instead of usual 2-ways partitioning [< pivot || > pivot].
    '''
    n = len(new_list)
    blue_pointer = 0
    red_pointer = n - 1 
    white_pointer = 0

    while white_pointer <= red_pointer: 
        if new_list[white_pointer].startswith('B'):
            # swap white_pointer and blue_pointer
            new_list[white_pointer], new_list[blue_pointer] = new_list[blue_pointer], new_list[white_pointer] 
            # increment white_pointer
            white_pointer += 1
            # increment blue_pointer
            blue_pointer += 1 

        elif new_list[white_pointer].startswith('R'):
            # swap white_pointer and red_pointer
            new_list[white_pointer], new_list[red_pointer] = new_list[red_pointer], new_list[white_pointer] 
            # decrement red_pointer
            red_pointer -= 1
            
        else:
            # increment white_pointer 
            white_pointer += 1

    return new_list 



#%% driver 
new_list = ['R1', 'B1', 'W1', 'R2', 'B2', 'W2', 'R3', 'W3']
print(new_list)
new_list = dutch_national_flag(new_list)
print(new_list)