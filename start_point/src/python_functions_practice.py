def return_10():
    return 10

def add(num_1, num_2):
    total = num_1 + num_2
    return total

def subtract(num_1, num_2):
    total = num_1 - num_2
    return total

def multiply(num_1, num_2):
    total = num_1 * num_2
    return total

def divide(num_1, num_2):
    total = num_1 / num_2
    return total

def length_of_string(my_string):
    length = len(my_string)
    return length

def join_string(string_1, string_2):
    joined = string_1 + string_2
    return joined

def add_string_as_number(string_1, string_2):
    num_1 = int(string_1)
    num_2 = int(string_2)
    total = num_1 + num_2
    return total

def number_to_full_month_name(month_number):
    if month_number == 1:
        return "January"
    elif month_number == 2:
        return "February"
    elif month_number == 3:
        return "March"
    elif month_number == 4:
        return "April"
    elif month_number == 5:
        return "May"
    elif month_number == 6:
        return "June"
    elif month_number == 7:
        return "July"
    elif month_number == 8:
        return "August"
    elif month_number == 9:
        return "September"
    elif month_number == 10:
        return "October"
    elif month_number == 11:
        return "November"
    elif month_number == 12:
        return "December"
    
def number_to_short_month_name(month_number):
    if month_number == 1:
        return "Jan"
    elif month_number == 2:
        return "Feb"
    elif month_number == 3:
        return "Mar"
    elif month_number == 4:
        return "Apr"
    elif month_number == 5:
        return "May"
    elif month_number == 6:
        return "Jun"
    elif month_number == 7:
        return "Jul"
    elif month_number == 8:
        return "Aug"
    elif month_number == 9:
        return "Sept"
    elif month_number == 10:
        return "Oct"
    elif month_number == 11:
        return "Nov"
    elif month_number == 12:
        return "Dec"
    
def calc_vol(l, b, h):
    volume = l * b * h
    return volume

def reversed_string(words):
    reversed = words[::-1]
    return reversed

def temp_convert(temp_f):
    temp_c = (temp_f - 32) * 5 / 9
    temp_c = int(temp_c)
    return temp_c