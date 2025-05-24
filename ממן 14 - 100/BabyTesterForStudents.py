from Baby import *

def main_tester():
    print(f"********** Test Baby - Started **********")

    print(f"\n\n1. Testing Constructor and __str__:")
    b1 = Baby("Denis", "Johnson", "123456789", 3, 5, 2018, 3600)
    print(f"\nbaby b1 is:\n{b1}")
    b2 = Baby("Joe", "Davis", "112233445", 14, 6, 1999, 4200)
    print(f"\nbaby b2 is:\n{b2}")

    print(f"\n\n2. Testing accessors and mutators:")
    w1 = Weight(4,40)
    b1.set_current_weight(w1)
    print(f"\nafter setting current weight to (4,40) baby b1 is:\n{b1}")

    print(f"\nfirst name of b1 (should be Denis): {b1.get_first_name()}")
    print(f"last name of b1 (should be Johnson): {b1.get_last_name()}")
    print(f"id of b1 (should be 123456789): {b1.get_id()}")
    print(f"date of birth of b1 (should be 03/05/2018): {b1.get_date_of_birth()}")
    print(f"birth weight of b1 (should be 3.6): {b1.get_birth_weight()}")
    print(f"current weight of b1 (should be 4.04): {b1.get_current_weight()}")

    print(f"\n\n3. Testing equals method:")
    print(f"\nbaby b1 is:\n{b1}")
    print(f"\nbaby b2 is:\n{b2}")
    if b1 == b2:
        print(f"\nERROR: b1 is the same baby as b2 while the two babies are not equal")
    else:
        print(f"\nPASSED: b1 isn't the same baby as b2")

    print(f"\n4. Testing areTwins method:")
    if b1.are_twins(b2):
        print(f"\tFAILED: b1 and b2 are Twins")
    else:
        print(f"\tPASSED: b1 and b2 are not Twins")

    print(f"\n5. Testing heavier method b2 (4.2) > b1 (3.6):")
    if b2 > b1:
        print(f"\tPASSED: b2 is heavier compare to b1 since 4.2 > 3.6")
    else:
        print(f"\tFAILED: b1 is not heavier than b2 since 3.6 is not > 4.2")

    print(f"\n6. Testing updateCurrentWeight method - adding 440 grams to b2 (that his current Weight is 4.2):")
    b2.update_current_weight(440)
    print(f"\nbaby b2 is:\n{b2}\nshould see that Current Weight is 4.64")

    print(f"\n7. Testing older method by executing b2.older(b1) where b1 birth date 03/05/2018 is and b2 birth date is 14/06/1999:")
    if b2.older(b1):
        print(f"\tPASSED: b2 is older than b1")
    else:
        print(f"\tFailed: b1 is not older than b2")

    print(f"\n********** Test Baby - Finished **********\n")

if __name__ == "__main__":
    main_tester()