# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones.
# If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible.
# Write a Python program to find the number of stones in each pile.
try:
    def pileOfStone(n):
        pileLits=[n]
        for i in range(1,n):
            n=n+2
            pileLits.append(n)
        return pileLits
    n = int(input("Enter the number of pile: "))
    print(pileOfStone(n))
except:
    print("You have enter invalid input")

