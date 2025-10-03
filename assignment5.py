print("=== Challenge 1: Collatz Conjecture ===")
n = int(input("Enter starting number: "))
counter = 0
print("Sequence:", n, end=" ")
while n != 1:
    if (n % 2) == 0:
        n/=2
        counter +=1
        print(int(n), end=" ")
    else:
        n = (n*3)+1
        counter +=1
        print(int(n), end=" ")
print()
print("\nSteps: ", counter)