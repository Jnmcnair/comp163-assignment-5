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
print("=== Challenge 2: Prime Number Checker ===")
num=int(input("Enter a number: "))
print(f"Testing divisors from 2 to {num-1}...")

for i in range(2,num):
    if (num % i) == 0:
        print(num, "is not prime (Divisible by", i,")")
        break
    else:
        print(num, "is prime!")
        break
