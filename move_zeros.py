def move_zeros(array):
    """
    The goal of this function is to accept a list, then
    return  a list with all 0 moved in the right side while 
    maintaining the order of non-zero from left to right.

    List can contain any data type.
        
    Note that:
        - False is equal to 0 in Python but False should not be moved to right.
        - 0.0 is equal to 0 as well.
    """
    new_array = []
    num_zero = 0
    num_false = 0

    # Create a new list that only adds non-zero value 
    # and include False since 0==False since it
    # won't get included in the elif statement.
    
    # Keep track of the number of False values since
    # we are going to use to to subtract from  using
    # list.count(x) function because it also counts False.

    for item in array:
        if str(item)=="False":
            new_array.append(item)
            num_false += 1
        elif item!=0:
            new_array.append(item)

    # Count all non-zero, this will include
    # False values so we subtract it.
    num_zero=array.count(0)-num_false

    # Append the n number of zeros at list.
    for i in range(0, num_zero):
        new_array.append(0)

    return new_array


#print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print(move_zeros([False, 0]))
 