def bouncingBall(h, bounce, window):
    """
    This function takes a parameter height (h),
    bounce factor (bounce), and a target height
    (window) and returns how many times a ball 
    will be seen from the window if it is dropped
    from height (h).
    
    This problem requires Physics understanding.
    Given h, bounce and window, you can calculate
    how many times, n, the ball will bounce if
    prev_height is greater than current_height 
    multiplied by the bounce factor.
    
    Each time it bounces greater than windows height, 
    it will be seen twice (rise and fall). Initially,
    it is 1 since it was dropped from above the windows 
    height by the boy.
    """
    
    if h>0 and (bounce>0 and bounce<1) and window<h:
        
        num_times = 1
        prev_height = h
        
        while True:
            if prev_height*bounce > window:
                num_times += 2
                prev_height = prev_height * bounce
            else:
                break
                
        return num_times
    
    return -1
