def check_list(arr:list):
    error_messages = [
        "Please pass in a List",
        "Error list contains non integer values",
        "Error empty list detected pass in a list with int values instead",
    ]
    
    if type(arr) != list:
        return error_messages[0]
    
    if len(arr):
        for val in arr:
            if type(val) != int:
                return error_messages[1]
        return True
    else:
        return error_messages[2]

def print_even(arr:list):
    is_list = check_list(arr)
    
    if is_list == True:
        print(*filter(lambda val: val%2==0 and val!=0, arr))
    else:
        print(is_list)


