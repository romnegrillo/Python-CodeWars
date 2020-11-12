# This functions accepts a single integer and return a list of its factors.
def get_factors(num):
    num = abs(num)
    return [i for i in range(2,num+1) if num%i == 0]

# This function accepts a list of integer and return the prime numbers only.
def get_prime_numbers(num_list):
    
    prime_num_list = []
   
    for num in num_list:
        is_prime = True

        if num <= 1:
            continue

        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
            
        if is_prime:
            prime_num_list.append(num)

    return prime_num_list

# This function accepts list of integers then returns a sorted list of the form:
#[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]
def sum_for_list(num_list):

    # Create list that will be paired later.
    num_factor_list = []
    sum_of_num_list = []

    # For each interget, get all its factors then extend it to a list.
    for num in num_list:
         num_factor_list.extend(get_prime_numbers(get_factors(num)))
    
    #  Remove the duplicates by converting it to a set then back to list.
    num_factor_list = list(set(num_factor_list))
    num_factor_list.sort()

    # The first element in each pair is the unique factor so lets
    # iterate in their list and store each in current_num_factor.
    # For the current original number, current_num, we will check
    # if it can be factored by the current_num_factor then add it
    # to a new vatiable, sum_num_factor, if it is. Repeat the process
    # and set sum_num_factor to zero at the very start.
    for current_num_factor in num_factor_list:
        sum_num_factor = 0

        for current_num in num_list:
            if current_num % current_num_factor == 0:
                sum_num_factor += current_num
        
        sum_of_num_list.append(sum_num_factor)

    final_list = [list(i) for i in zip(num_factor_list, sum_of_num_list)]

 

    return final_list


print(sum_for_list([[2, 12], [3, 27], [5, 15]]))