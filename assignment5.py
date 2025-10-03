print("=== Challenge 1: Collatz Conjecture ===")
n = int(input("Enter starting number: "))
counter = 0
print("Sequence:", n, end=" ") #print the starting number and formatting for the rest of the sequence
while n != 1: #loop until n is 1
    if (n % 2) == 0:
        n/=2
        counter +=1
        print(int(n), end=" ")
    else:
        n = (n*3)+1
        counter +=1
        print(int(n), end=" ")
print()
print("Steps:", counter)
print("")

print("=== Challenge 2: Prime Number Checker ===")
num=int(input("Enter a number: "))
print(f"Testing divisors from 2 to {num-1}...")
if num > 1: #check if number is greater than 1 in order to then check if the number is prime
    for i in range(2,num-1):
        if num % i == 0:
            print(num, "is not prime (Divisible by", i,")")
            break#add a break statement to exit the loop if a divisor is found since it would not be prime
    else:
        print(num, "is prime!")

else:
    print(num, "is not prime (Less than 2)")

print("")
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
print("   ", end="")
for i in range(1,11): #print the header row of 1 through 10 
    print(f"{i:4}", end="")
print()

for row in range(1,11): #print each row of the multiplication table 
    print(f"{row:4}", end=" ")
    for col in range(1,11):
        print(f"{row*col:4}", end=" ")
    print()