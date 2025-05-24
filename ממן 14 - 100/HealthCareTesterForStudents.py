from HealthCare import *

def main_tester():

    print(f"********** Test HealthCare - Started **********")

    print(f"\n\n1. Testing Constructor / get_name() and __str__:")
    name = "Jerusalem"
    hc = HealthCare(name)

    if hc.get_name() == name:
        print(f"PASSED: get_name() of the new branch is: {hc.get_name()}")
    else:
        print(f"FAILED: get_name() of the new branch named: {name} returned by the student: {hc.get_name()}")

    no_babies_str = "There are no babies in this Health Care branch."
    if str(hc) != no_babies_str:
        print(f"FAILED: after creating a branch with no babies the __str__ method should print {no_babies_str} while student method prints:\n{str(hc)}")
    else:
        print(f"\nPASSED: Health Care with no babies yet:\n{str(hc)}")

    print(f"\n\n2. Testing add()")

    baby1 = Baby("Alice", "Smith", "123456789", 15, 6, 2021, 3000)
    baby1.set_current_weight(Weight(3,400))

    baby2 = Baby("Bob", "Brown", "987654321", 10, 6, 2021, 3500)
    baby2.set_current_weight(Weight(3, 900))

    hc.add_baby(baby1)
    print(f"\nHealth Care after adding 1 baby is:\n{hc}")

    hc.add_baby(baby2)
    print(f"\nHealth Care after adding the second baby is:\n{hc}")

    print(f"\n3. Testing num_of_babies():")
    if hc.num_of_babies() == 2:
        print(f"PASSED: num_of_babies() of the Jerusalem branch is: {hc.num_of_babies()}")
    else:
        print(f"FAILED: num_of_babies() of the Jerusalem branch is 2 while student method returned: {hc.num_of_babies()}")

    print(f"\n4. Testing how_many_above_weight():")

    baby3 = Baby("Charlie", "Davis", "456789123", 15, 6, 2021, 4200)
    baby3.set_current_weight(Weight(4, 400))
    hc.add_baby(baby3)

    print(f"Testing how_many_above_weight() for Jerusalem branch after adding a new baby.\n"
          f"Total 3 babies in this branch with the following Weights: 3.4, 3.9, 4.4 then after sending 3.8 as a parameter...\n")

    how_many_above = hc.how_many_above_weight(Weight(3, 800))
    if how_many_above == 2:
        print(f"PASSED: how_many_above_weight(Weight(3,800)) of the Jerusalem branch is: {how_many_above}")
    else:
        print(f"FAILED: how_many_above_weight(Weight(3,800)) of the Jerusalem branch is 2 while student method returned: {how_many_above}")

    print(f"\n5. Testing average_weight():")

    average = hc.average_weight()
    if average == Weight(3,900):
        print(f"PASSED: average_weight() of the Jerusalem branch is: {average}")
    else:
        print(f"FAILED: average_weight() of the Jerusalem branch is 3.9 while student method returned: {average}")


    print(f"\n6. Testing most_heaviest_baby():")

    print(f"Testing most_heaviest_baby() for Jerusalem branch.\n"
          f"Total 3 babies in this branch with the following Weights: 3.4, 3.9, 4.4 then after sending 3.8 as a parameter...\n")

    heavy_baby = hc.most_heaviest_baby()
    if heavy_baby.get_current_weight() == Weight(4,400):
        print(f"PASSED: most_heaviest_baby() of the Jerusalem branch is:\n{heavy_baby}")
    else:
        print(f"FAILED: most_heaviest_baby() of the Jerusalem branch should be the baby that his current Weight is 4.4 while student method returned:\n{heavy_baby}")

    print(f"\n7. Testing babies_above_weight():")
    print(f"Testing babies_above_weight() for Jerusalem branch.\n"
          f"Total 3 babies in this branch with the following Weights: 3.4, 3.9, 4.4 then after sending 3.8 as a parameter...\n")

    heavy_babies = hc.babies_above_weight(Weight(3,800))
    print(f"babies_above_weight(3,800) of the Jerusalem branch returned the list below:\n")
    for baby in heavy_babies:
        print(baby)
    print(f"please check there are 2 babies with weights: 3.9 and 4.4")

    print(f"\n********** Test HealthCare - Finished **********\n")

if __name__ == "__main__":
    main_tester()