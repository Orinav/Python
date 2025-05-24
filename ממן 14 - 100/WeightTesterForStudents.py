from Weight import*

def main_tester():

    print(f"********** Test Weight - Started **********")
    print(f"\n1. Testing Constructor and __Str__:")
    w1 = Weight(3, 10)
    print(f"\tWeight(3,10) result in  Weight w1: {w1} while should it be 3.01")
    w2 = Weight(4, 3)
    print(f"\tWeight(4,3) result in Weight w2: {w2} while it should be 4.003")

    print(f"\n2. Testing accessors :")
    print (f"\tkilos of w1 (3.01 so should be 3): {w1.get_kilos()}")
    print(f"\tgrams of w1 (3.01 so should be 10): {w1.get_grams()}")

    print(f"\n3. Testing equals method:")
    if w1 == w2:
        print(f"\tERROR: Weight w1 is equal to Weight w2 while the Weights are not equal 3.01 != 4.003...")
    else:
        print(f"\tPASSED: Weight w1 (3.01) is NOT equal to Weight w2 (4.003)")

    print(f"\n4. Testing lighter method:")
    if w1 < w2:
        print(f"\tPASSED: Weight1 (3.01) is lighter than Weight w2 (4.003)")
    else:
        print(f"\tERROR: Weight1 is NOT lighter than Weight w2 while it should be since 3.01 < 4.003")

    print(f"\n5. Testing heavier method:")
    if w2 > w1:
        print(f"\tPASSED: Weight w2 (4.003) is heavier than Weight w1 (3.01)")
    else:
        print(f"\tERROR: Weight w2 is Not heavier than Weight w1 while it should be since 4.003 > 3.01...")

    print(f"\n6. Testing add method:")
    print(f"\tWeight w1 is 3.01")
    w1.add(500)
    print(f"\tAdding 500 grams to Weight w1 result is the following Weight: {w1} while it should be 3.51")

    print(f"\n********** Test Weight - Finished **********\n")


if __name__ == "__main__":
    main_tester()