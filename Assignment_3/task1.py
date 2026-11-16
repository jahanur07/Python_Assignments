#using loop

# def factorial(n):
#   fact = 1
#   for i in range(1,n+1):
#     fact *= i
#   return fact

# n = int(input("Enter a number :"))
# fact = factorial(n)
# print(f"factorial of {n} is : {fact}")

#using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial of", num, "is:", result)

