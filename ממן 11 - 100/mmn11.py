'''
Title - Maman 11
Author - Ori Nave
Date - 20/11/24
Description - This file will include functions that will implement the answers to all 4 questions of Maman 11.
'''



def game(player1, player2):
    '''
    Description:
    The function will simulate the popular game "Rock, Paper, Scissors" when:
    Rock - 'R', Paper - 'P', Scissors - 'S'.

    Parameters:
    player1 - R/S/P
    player2 - R/S/P

    Output:
    The function will return:
    0 - If it's a tie.
    1 - If player1 wins.
    2 - If player2 wins.
    '''
    if player1 == 'R':
        if player2 == 'R':
            return 0
        elif player2 == 'P':
            return 2
        elif player2 == 'S':
            return 1

    elif player1 == 'P':
        if player2 == 'R':
            return 1
        elif player2 == 'P':
            return 0
        elif player2 == 'S':
            return 2

    elif player1 == 'S':
        if player2 == 'R':
            return 2
        elif player2 == 'P':
            return 1
        elif player2 == 'S':
            return 0


def tournament():
    '''
    Description:
    This function will base on game function to create a tournament,
    At first it will ask the user to enter player1 and player2 names,
    Then it will simulate 5 rounds of "Rock, Paper, Scissors" based on best of 3 rounds,
    In the end it will print who won the tournament.

    Variables:
    name1 - The name of player1.
    name2 - The name of player2.
    sum1 - The amount of wins of player1.
    sum2 - The amount of wins of player2.
    choice1 - player1 choice.
    choice2 - player2 choice.
    result - game result in each round.

    Output:
    The function will print who won the tournament.
    '''
    name1 = input("Player1, Please enter your name: ")
    name2 = input("Player2, Please enter your name: ")
    sum1 = 0
    sum2 = 0
    for iteration in range(5):
        choice1 = input(f"{name1}, Please choose R/P/S: ")
        choice2 = input(f"{name2}, Please choose R/P/S: ")
        result = game(choice1, choice2)
        if result == 1:
            sum1 += 1
        elif result == 2:
            sum2 += 1

        if sum1 == 3 or sum2 == 3:
            break

    if sum1 > sum2:
        print(f"{name1} won the tournament!")
    elif sum1 < sum2:
        print(f"{name2} won the tournament!")
    else:
        print("Tournament ended with a tie")


def sum_digits(num):
    '''
    Description:
    This function will get a number and will return the sum of its digits.

    Parameters:
    num - positive integer.

    Variables:
    sum - The sum of num digits.
    num_string - In order to iterate num we use num_string which is a string type variable of num.

    Output:
    The function will return the sum of num digits.
    '''
    sum = 0
    num_string = str(num)
    for number in num_string:
        sum += int(number)
    return sum


def close_to_ten(num):
    '''
    Description:
    This function will get a number and will return the closest multiplication by 10 to the number(from above the number).

    Parameters:
    num - positive integer.

    Variables:
    rounded_num - The closest multiplication by 10 of num(from above).

    Output:
    The function will return The closest multiplication by 10 of num(from above).
    '''
    rounded_num = num
    if (num%10 == 0):
        return rounded_num
    else:
        rounded_num += 10 - num%10
        return rounded_num


def valid_id(id_num):
    '''
    Description:
    This function will use sum_digits and close_to_ten functions,
    The function get a string that represents an Israeli identity card number and will print:
    "OK" - if the number is valid.
    "ERROR" - if the number is invalid.

    Parameters:
    id_num - A string that represents an Israeli identity card number.

    Variables:
    sum - The sum of the first 8 digits of the identity card number based on the Israeli identity card digits weight method.
    digit - The integer variation of each digit of id_num.
    position - A variable that represent the position of the current digit that we sum.
    rounded_sum - The closest multiplication by 10 of sum(from above).
    check_digit - The 9th digit of id_num.

    Output:
    The function will print:
    "OK" - if the number is valid.
    "ERROR" - if the number is invalid.
    '''
    if len(id_num) != 9 or not id_num.isdigit():
        print("ERROR")
        return

    sum = 0
    position = 1
    for character in id_num:
        if position == 9:
            break

        digit = int(character)
        if position%2 == 1:
            sum += digit
        elif position%2 == 0:
            sum += sum_digits(2*digit)
        position += 1

    rounded_sum = close_to_ten(sum)
    check_digit = int(id_num[8])

    if check_digit != rounded_sum - sum:
        print("ERROR")
    else:
        print("OK")


def is_prime(num):
    '''
    * NOTE - THIS FUNCTION IS A HELPER FUNCTION FOR QUESTION 3 *
    Description:
    This function will get a number and will return whether if its a prime number or not.

    Parameters:
    num - Natural number.

    Output:
    The function will return:
    True - If num is a prime number.
    False - If number isn't a prime number.
    '''
    for number in range(2, num):
        if num%number == 0:
            return False

    return True


def max_common_prime_divider(n1, n2):
    '''
    Description:
    This function will use is_prime function,
    The function will get 2 numbers and will return their prime greatest common divider.

    Parameters:
    n1 - Natural number.
    n2 - Natural number.

    Variables:
    prime_gcd - The prime greatest common divider of n1 and n2.

    Output:
    The function will return the prime greatest common divider of n1 and n2.
    '''
    prime_gcd = 1
    if n1 > n2:
        for num in range(2, n2+1):
            if n1%num == 0 and n2%num == 0 and is_prime(num):
                prime_gcd = num
    else:
        for num in range(2, n1 + 1):
            if n1%num == 0 and n2%num == 0 and is_prime(num):
                prime_gcd = num

    return prime_gcd


def max_prime_divider(n):
    '''
    Description:
    This function will use is_prime function,
    The function will get a number and will return its prime greatest divider.

    Parameters:
    n - Natural number.

    Variables:
    prime_gd - The prime greatest divider of n.

    Output:
    The function will return the prime greatest divider of n.
    '''
    prime_gd = 1
    for num in range(1,n+1):
        if n%num == 0 and is_prime(num):
            prime_gd = num

    return prime_gd


def is_perfect(n):
    '''
    Description:
    This function will get a number and will return whether its a perfect number or not.

    Parameters:
    n - Natural number.

    Variables:
    sum - The sum of all the numbers from 1 to (n-1) that are divided by n.

    Output:
    The function will return:
    True - If n is perfect number.
    False - If n isn't perfect number.
    '''
    sum = 0
    for num in range(1,n):
        if n%num == 0:
            sum += num

    if n == sum:
        return True
    else:
        return False


def perfect_numbers(num):
    '''
    Description:
    This function will use is_perfect function,
    The function will get a number and will print all the perfect numbers from 1 to that number.

    Variables:
    num - Integer.

    Output:
    The function will print all the perfect numbers from 1 to num.
    '''
    if num < 6:
        print("There are no perfect numbers.")
    else:
        print("Perfect numbers are: ", end="")
        for number in range(6, num+1):
            if is_perfect(number):
                print(f"{number}, ", end="")
        print("")  # Go to the next line when the function finish.