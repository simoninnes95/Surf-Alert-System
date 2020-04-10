import scrape_conditions

def check_conditions(input_list, minimum, maximum):

    matrix = []

    for item in input_list:
        if minimum <= item <= maximum:
            matrix.append(1)
        else:
            matrix.append(0)

    return matrix

def all_swellconditions_check(array1, array2, array3):

    swell_variable_check = []

    for index in range(len(array1)):
        if array1[index] == 1 and array2[index] == 1 and array3[index] ==1:
            swell_variable_check.append(1)
        else:
            swell_variable_check.append(0)

    return swell_variable_check
