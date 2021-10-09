

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



def check_date(date:str):
    error_messages = [
        "Invalid date string ensure that the date is of this format YYYY-MM-DD",
        "Date's can only contain integers"
    ]
    
    date_split =  date.split("-")
    
    if len(date_split) != 3:
        return error_messages[0]

    if len(date_split[0]) > 4 or len(date_split[1]) > 2 or len(date_split[2]) > 2:
        return error_messages[0]
    
    try:
        for i in date_split:
            int(i)
    except TypeError:
        return error_messages[1]
    else:
        if (
            int(date_split[1]) < 1 or 
            int(date_split[1]) > 12 or
            int(date_split[2]) < 1 or
            int(date_split[2]) > 31 or
            int(date_split[0]) < 1):

            return error_messages[0]
    return date_split

def string_date(date_1:str, date_2:str):
    parseed_date_1, parseed_date_2 = check_date(date_1), check_date(date_2)


    if type(parseed_date_1) != list:
        print(parseed_date_1)
        return
    
    if type(parseed_date_2) != list:
        print(parseed_date_2)
        return

    days = [
        int(parseed_date_1[2]),
        int(parseed_date_2[2])
    ]

    print(f"The days in date {date_1} is {days[0]}")
    print(f"The days in date {date_2} is  {days[1]}")
    print(f"The difference in days between {date_1} and {date_2} is {abs(days[0] - days[1])}")



if __name__ == "__main__":
    print_even([2,3,4,6,7,8,9,0,1,10,23,12,54])
    string_date("2001-2-1", "2001-2-20")