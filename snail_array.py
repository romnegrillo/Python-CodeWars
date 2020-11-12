def snail(arr):

    for i in arr:
        print(i)

    snail_array = []
    n = len(arr)

    if n%2 == 0:
        
        for i in range(0,n//2):

            snail_array.extend(arr[i][i:n-i])
 
            snail_array.extend(arr[n-1-i][n-1-i:-n+i:-1])
        
    else:
        pass

    return snail_array
            





print(snail([[1,2],[3,4]]))
print(snail([[1,2,3],[4,5,6],[7,8,9]]))
print(snail([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
print(snail([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))
print(snail([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]))




