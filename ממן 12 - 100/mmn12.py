'''
Title - Maman 12
Author - Ori Nave
Date - 12/12/24
Description - This file will include functions that will implement the answers to all 4 questions of Maman 12.
'''


def biggest_sum(lst):
    '''
    Description:
    The function will get a list and will return the biggest sum of numbers inside the list that are between two zeros.

    Parameters:
    lst - List.

    Variables:
    current_sum - The current sum between two zeros.
    max_sum - The biggest sum between two zeros.
    zero_flag - Will be False if we didn't encounter any zero, True otherwise.

    Output:
    If the input is invalid - The function will raise TypeError message.
    If the input is valid - The function will return the biggest sum of numbers inside the list that are between two zeros.
    '''
    for element in lst:
        if type(element) != int or element < 0:
                raise TypeError("All the elements in lst must be an integers that are bigger or equal to 0")

    current_sum = 0
    max_sum = 0
    zero_flag = False

    for element in lst:
        if element == 0 and zero_flag == False:
            zero_flag = True
            continue
        elif element == 0 and zero_flag == True:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
            continue

        if zero_flag == True:
            current_sum += element

    return max_sum


def biggest_sum_row(mat):
    '''
    Functions used:
    biggest_sum.

    Description:
    The function will get a 2D list and will return the index of the row with the biggest sum.

    Parameters:
    mat - 2D list

    Variables:
    row_index - The index of the list with the biggest sum.
    max_sum - The biggest list sum.
    row_sum - The current row sum.

    Output:
    If the input is invalid - The function will raise TypeError message.
    If the input is valid - The function will return the index of the row with the biggest sum.
    '''
    row_index = 0
    max_sum = 0
    row_sum = 0
    try:
        for i in range(len(mat)):
            row_sum = biggest_sum(mat[i])
            if max_sum < max(max_sum, row_sum):
                max_sum = row_sum
                row_index = i
        return row_index
    except:
        return -1


def shift_k_right(lst, k):
    '''
    Description:
    The function get a list and an integer and will right shift the list by that integer.

    Parameters:
    lst - List.
    k - Integer.

    Variables:
    lst_copy - At first it's a copy of lst, Later on it's the shifted list.

    Output:
    If the input is invalid - The function will raise IndexError message.
    If the input is valid - The function will return the shifted list.
    '''
    if k < 0 or k >= len(lst):
        raise IndexError("k must be non negative and less from the length of lst")

    lst_copy = lst.copy()

    for i in range(len(lst)):
        lst_copy[(i+k)%len(lst_copy)] = lst[i]

    return lst_copy


def shift_right_size(a, b):
    '''
    Functions used:
    shift_k_right.

    Description:
    The function will get 2 lists and will return the size of right shifts that have to be done in order to make b=a.

    Parameters:
    a - List.
    b - List.

    Variables:
    shifted_b = The current shifted list of b.

    Output:
    If it's not possible the b=a - The function will return None.
    If it's possible that b=a - The function will return the size of right shifts that have to be done in order to make b=a.
    '''
    if len(a) != len(b):
        return None

    if len(a) == 0 and len(b) == 0:
        return 0

    for i in range(len(b)):
        shifted_b = shift_k_right(b, i)
        if shifted_b == a:
            return i

    return None


def is_perfect(lst):
    '''
    Description:
    The function will get a list and will return if the list is perfect or not by "scan by cells values" method.
    "scan by values" method is a scanning method which starts at index 0(i=0) and the next index that will be scan is list[i].
    Terms for perfect list:
    1) All the list's cells are scanned.
    2) The scan ends(The value 0 is encountered).

    Parameters:
    lst - List.

    Variables:
    visited - A list that contains which cells of lst are visited.
    steps - A counter that holds the value of how many moves we've done so far.
    i - Index.
    found_zero - A boolean that acts as a flag, if zero found in lst - True, Otherwise - False.

    Output:
    If the list is invalid - The function will raise IndexError message.
    If the list is perfect - True
    If the list isn't perfect - False.
    '''
    if len(lst) == 0 or (len(lst) == 1 and lst[0] == 0):
        return True
    for element in lst:
        if type(element) != int or element < 0:
            raise IndexError("All the elements in lst must be non negative integers")

    visited = len(lst)*[False]
    steps = 0
    i = 0
    found_zero = False

    while True:
        if lst[i] == 0:
            found_zero = True
            visited[i] = True
            break

        if steps >= len(lst):
            break

        elif lst[i] != 0:
            visited[i] = True
            i = lst[i]
            steps += 1


    for cell in visited:
        if cell == False:
            return False

    if found_zero == False:
        return False

    return True


def mirror_list(mat):
    '''
    Description:
    This function will get a 2D list that all of it's elements are strings in length of 1,
    we will check whether it's a "mirror list"(a list that all of its elements in opposite spots are identical)

    Parameters:
    mat - a 2D list.

    Variables:
    rows - rows length
    columns - columns length

    Output:
    If the input is invalid - TypeError or ValueError message.
    If it's a mirror list - True
    If it's not a mirror list - False.
    '''
    if len(mat) == 0:
        return True

    rows = len(mat)
    columns = len(mat[0])

    for i in range(rows):
        for j in range(columns):
            if type(mat[i][j]) != str:
                raise TypeError("All the elements in mat must be strings")
            if len(mat[i][j]) != 1:
                raise ValueError("All the elements in mat must be in length of 1")

    for i in range(rows):
        for j in range(columns):
            if mat[i][j] != mat[rows-i-1][j]: #Checks rows
                return False
            if mat[i][j] != mat[i][columns - j - 1]: #Checks columns
                return False

    return True