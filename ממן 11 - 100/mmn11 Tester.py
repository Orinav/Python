def main_tester():
    print("Check game function")
    print(game("R","S"))   
    print(game("S", "R"))  
    print(game("P", "R"))  
    print(game("R", "P"))  
    print(game("S", "S"))  

    # tournament()

    print("\n\nCheck sum_digit function:")
    print(sum_digits(5))
    print(sum_digits(14))
    print(sum_digits(12345))


    print("\n\nCheck close_to_ten function:")
    print(close_to_ten(9))  
    print(close_to_ten(10)) 
    print(close_to_ten(22)) 
    print(close_to_ten(141)) 


    print("\n\nCheck valid_id function:")
    valid_id("543700421")   
    valid_id("543700422")   
    valid_id("206264541")   
    valid_id("206264551")   


    print("\n\nCheck max_common_prime_divider function:")
    print(max_common_prime_divider(14,21))  
    print(max_common_prime_divider(17,101)) 
    print(max_common_prime_divider(4,4))    
    print(max_common_prime_divider(50,25))  
    print(max_common_prime_divider(21,1))   
    print(max_common_prime_divider(21,2))  

    print("\n\nCheck max_prime_divider function:")
    print(max_prime_divider(21))    
    print(max_prime_divider(8))     
    print(max_prime_divider(5))     
    print(max_prime_divider(1981))  
    print(max_prime_divider(399))   
    print(max_prime_divider(11935)) 
    print(max_prime_divider(106))   


    print("\n\nCheck is_perfect function:")
    print(is_perfect(6))    
    print(is_perfect(20))   
    print(is_perfect(28))   
    print(is_perfect(8128)) 
    print(is_perfect(17))   

    print("\n\nCheck perfect_numbers function:")
    perfect_numbers(5)
    perfect_numbers(6)
    perfect_numbers(29)
    perfect_numbers(10000)


main_tester()