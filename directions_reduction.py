def dirReduc(arr):
    
    all_patterns = ["NORTH SOUTH", "SOUTH NORTH", "EAST WEST", "WEST EAST"]
    arr_string = " ".join(arr)

    while True:
        found = False
        for pattern in all_patterns:
            if pattern in arr_string:
                arr_string = " ".join(arr_string.replace(pattern, "").split())
                found = True
        if not found:
            break


    return arr_string.split()
                

print(dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]))