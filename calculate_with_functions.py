"""
Functions that has a number name can only take two values:
- None
- An operator and another number

So, we check if we passed a value or not.
If not, then it should simply return the number that it is assigned to.
This is doned by a flag to see if it changed or not. Default parameter.
Else, it will return its number, the operator and another number.

Functions that has an operator name only takes a number. 
It will return a tuple of operator and the number passed.

"""

def zero(is_outer = False): 
    val = 0 if not is_outer else eval("{} {} {}".format(0,is_outer[0],is_outer[1]))
    return val

def one(is_outer = False):
    val = 1 if not is_outer else eval("{} {} {}".format(1,is_outer[0],is_outer[1]))
    return val

def two(is_outer = False):  
    val = 2 if not is_outer else eval("{} {} {}".format(2,is_outer[0],is_outer[1]))
    return val

def three(is_outer = False):  
    val = 3 if not is_outer else eval("{} {} {}".format(3,is_outer[0],is_outer[1]))
    return val

def four(is_outer = False):  
    val = 4 if not is_outer else eval("{} {} {}".format(4,is_outer[0],is_outer[1]))
    return val

def five(is_outer = False): 
    val = 5 if not is_outer else eval("{} {} {}".format(5,is_outer[0],is_outer[1]))
    return val

def six(is_outer = False):  
    val = 6 if not is_outer else eval("{} {} {}".format(6,is_outer[0],is_outer[1]))
    return val

def seven(is_outer = False):  
    val = 7 if not is_outer else eval("{} {} {}".format(7,is_outer[0],is_outer[1]))
    return val

def eight(is_outer = False): 
    val = 8 if not is_outer else eval("{} {} {}".format(8,is_outer[0],is_outer[1]))
    return val

def nine(is_outer = False):  
    val = 9 if not is_outer else eval("{} {} {}".format(9,is_outer[0],is_outer[1]))
    return val

def plus(num):  return ("+", num)
def minus(num):  return ("-", num)
def times(num): return ("*", num)
def divided_by(num):  return ("//", num)