'''
Title - Maman 13
Author - Ori Nave
Date - 01/01/25
Description - This file will include functions that will implement the answers to all 4 questions of Maman 13.
'''



def common(lst1, lst2):
    '''
    Description:
    The function will get 2 lists and will return a list with the common elements of those lists.
    The time complexity of the function is O(n) - linear time complexity.

    Parameters:
    lst1 - A list of integers that sorted in ascending order.
    lst2 - A list of integers that sorted in ascending order.

    Variables:
    result - A list that will store all the common elements of lst1 and lst2.
    i - An index that serves as iterator to lst1.
    j - An index that serves as iterator to lst2.

    Output:
    The function will return a list of the common elements of lst1 and lst2.
    '''
    result = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            i += 1
        elif lst1[i] > lst2[j]:
            j += 1
        else: # lst[i] == lst[j]
            result.append(lst1[i])
            i += 1
            j += 1

    if result == []:
        return None
    else:
        return result


def find_median(lst, m):
    '''
    Description:
    The function will get a list of non-negative integers and an integer m that presents the highest number in lst
    and will return the median of the lst.
    The time complexity of the function is O(n+m) - linear time complexity.

    Parameters:
    lst - A list of non-negative integers.
    m - The highest number in lst.

    Variables:
    m_lst - A list in length of m+1(to make the indices from 0 to m).
    sorted_lst = The sorted form of lst.
    sum - used to sum up all the indices values include itself in m_lst.
    median - The median of lst.

    Output:
    The function will return the median of the lst.
    '''
    m_lst = (m+1)*[0]
    sorted_lst = len(lst)*[0]
    for i in range(len(lst)):
        m_lst[lst[i]] += 1

    sum = 0
    for i in range(len(m_lst)):
        sum += m_lst[i]
        m_lst[i] = sum

    for i in range(len(lst)-1, -1, -1):
        value = lst[i]
        value_index = m_lst[value] - 1
        sorted_lst[value_index] = value
        m_lst[lst[i]] -= 1

    median = sorted_lst[len(sorted_lst)//2]
    return median


def max_pos_seq(lst):
    '''
    Functions Used:
    max_pos_seq_helper(lst, i, sum, max).

    Description:
    The function will get a list of integers(not including 0) and will return the length of the maximum sequence of positive integers.

    Parameters:
    lst - A list of integers(not including 0).

    Output:
    The function will return the length of the maximum sequence of positive integers.
    '''
    return max_pos_seq_helper(lst, 0, 0, 0)


def max_pos_seq_helper(lst, i, sum, max):
    '''
    Description:
    The function will get a list of integers(not including 0), a starting index, a sum, and a maximum
    and will return the length of the maximum sequence of positive integers.

    Parameters:
    lst - A list of integers(not including 0).
    i - An index that serves as iterator to lst.
    sum - An integer that keeps track of the current length of lst.
    max - An integer that keeps track of the maximum length of lst.

    Output:
    The function will return the length of the maximum sequence of positive integers.
    '''
    if i == len(lst):
        if sum > max:
            max = sum
        return max

    if lst[i] > 0:
        return max_pos_seq_helper(lst, i+1, sum+1, max)
    else:
        if sum > max:
            max = sum
        return max_pos_seq_helper(lst, i+1, 0, max)


def is_palindrome(lst):
    '''
    Functions Used:
    1) is_palindrome_lst(lst, i, j).
    2) is_palindrome_elements(lst, count, i, k, m)

    Description:
    The function will get a list of strings and will check if both of the next terms are met:
    1) The list is a palindrome.
    2) Every string in the list is a palindrome.
    The function will return True if both of the terms are met, False otherwise.

    Parameters:
    lst - A list of strings.

    Output:
    The function will return True if both of the terms are met, False otherwise.
    '''
    if lst == []:
        return True
    return is_palindrome_lst(lst,0,len(lst)-1) and is_palindrome_elements(lst, 0, 0, 0, len(lst[0])-1)


def is_palindrome_lst(lst, i, j):
    '''
    Description:
    The function will get a list and 2 indices and will return True if the list is a palindrome, False otherwise.

    Parameters:
    lst - A list of strings.
    i - An index that traverse right ->.
    j - An index that traverse left <-.

    Output:
    The function will return True if the list is a palindrome, False otherwise.
    '''
    if i >= j:
        return True
    if lst[i] != lst[j]:
        return False
    return is_palindrome_lst(lst, i+1, j-1)


def is_palindrome_elements(lst, count, i, k, m):
    '''
    Description:
    The function will get a list and 3 indices and will return True if every string in the list is palindrome, False otherwise.

    Parameters:
    lst - A list of strings.
    i - An index that serves as iterator to lst.
    k - An index that traverse right ->.
    m - An index that traverse left <-.

    Output:
    The function will return True if every string in the list is palindrome, False otherwise.
    '''
    if k >= m:
        count += 1
        if count == len(lst):
            return True
        return is_palindrome_elements(lst, count, i + 1, 0, len(lst[i + 1]) - 1)

    if lst[i][k] != lst[i][m]:
        return False

    return is_palindrome_elements(lst, count, i, k + 1, m - 1)