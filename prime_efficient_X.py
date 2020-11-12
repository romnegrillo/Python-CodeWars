def is_prime(num):
    
    if num <= 1:
        return False
        
    num_div=0
    
    for i in range(1,num):
        if num%i == 0:
            num_div += 1
            
        if num_div>2:
            break
            
    if num_div>2:
        return False
    
    return True

print(is_prime(1))