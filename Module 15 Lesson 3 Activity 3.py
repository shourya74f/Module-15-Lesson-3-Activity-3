g=input("At n=1000, O(n^2) takes how many steps? ")
input("Watch O(n) andO(n^2) grow, Press Enter to continue...")
for n in [10, 100, 1000]:
    input("n=" + str(n) + " Press Enter to continue...")
    print("O(n) takes", n, "steps and O(n^2) takes", n*n, "steps.")
