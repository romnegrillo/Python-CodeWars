def iq_test(numbers):
    """
    This function accepts a string that contains a numbers
    separated by spaces and returns the one number  the 
    is different in eveness. 
    """
    
    # Convert string into list of integers.
    numbers_list_int = [int(i) for i in numbers.split()]
    
    # Get all even numbers.
    numbers_even = [i for i in numbers_list_int if i % 2 == 0]
    
    # Get all odd numbers.
    numbers_odd = [i for i in numbers_list_int if i % 2 != 0]

    # Compare the number of even and odd numbers and
    # get the index of the lower items based from original
    # list of numbers.
    target_num = 0

    if len(numbers_even) > len(numbers_odd):
        target_num = numbers_odd[0]
    else:
        target_num = numbers_even[0]

    return numbers_list_int.index(target_num)+1