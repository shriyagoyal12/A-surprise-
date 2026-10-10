# 1. Print a table of any given number

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 2. Print even numbers from 1 to 100

for i in range(1, 101):
    if i % 2 == 0:
        print(i)


# 3. Print odd numbers from 1 to 100

for i in range(1, 101):
    if i % 2 != 0:
        print(i)


# 4. Print numbers between 1 and 100 divisible by 3 and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# 5. Calculate area and circumference of circle using function

def circle(radius):
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius

    print("Area =", area)
    print("Circumference =", circumference)

r = float(input("Enter radius: "))
circle(r)


# 6. Calculate area of rectangle using function

def rectangle(width, height):
    area = width * height
    print("Area of rectangle =", area)

w = float(input("Enter width: "))
h = float(input("Enter height: "))

rectangle(w, h)


# 7. Find sum of digits of a given number

num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits =", total)


# 8. Find sum of square of digits of a given number

num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total = total + (digit * digit)
    num = num // 10

print("Sum of square of digits =", total)


# 9. Find sum of cube of digits of a given number

num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total = total + (digit * digit * digit)
    num = num // 10

print("Sum of cube of digits =", total)


# 10. Check whether a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


# 11. Find the greatest number among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number =", a)
elif b >= a and b >= c:
    print("Greatest number =", b)
else:
    print("Greatest number =", c)


# 12. Check whether a number is prime or not

num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")


# 13. Calculate sum of n natural numbers

n = int(input("Enter value of n: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum of natural numbers =", total)


# 14. Find factorial of a given number

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)


# 15. Print Fibonacci series of a given number

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

print()


# 16. Reverse a given number

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse number =", reverse)


# 17. Check whether a number is positive or negative

num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")


# 18. Check whether a number is palindrome or not

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# 19. Check whether a number is Armstrong or not

num = int(input("Enter a number: "))
original = num
total = 0

while num > 0:
    digit = num % 10
    total = total + (digit * digit * digit)
    num = num // 10

if original == total:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# 20. Check whether a year is leap year or not

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# 21. Find product of digits of a given number

num = int(input("Enter a number: "))
product = 1

while num > 0:
    digit = num % 10
    product = product * digit
    num = num // 10

print("Product of digits =", product)


# 22. Find sum of even digits and product of odd digits
num = int(input("Enter a number: "))
even_sum = 0
odd_product = 1

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even_sum = even_sum + digit
    else:
        odd_product = odd_product * digit

    num = num // 10

print("Sum of even digits =", even_sum)
print("Product of odd digits =", odd_product)


# 23. Count total number of factors of a given number

num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

print("Total number of factors =", count)


# 24. Print 20 different pattern programs

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


for i in range(1, 6):
    for j in range(i):
        print(6 - i, end=" ")
    print()


for i in range(1, 6):
    for j in range(5):
        print("*", end=" ")
    print()


for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()


for i in range(1, 6):
    for j in range(5):
        print(i, end=" ")
    print()


for i in range(1, 6):
    for space in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()


for i in range(5, 0, -1):
    for space in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()


for i in range(1, 6):
    for space in range(5 - i):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j % 2, end=" ")
    print()


for i in range(1, 6):
    for j in range(i):
        print(i % 2, end=" ")
    print()


for i in range(1, 6):
    for j in range(i):
        print(chr(64 + i), end=" ")
    print()


for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(i):
        print(chr(70 - i), end=" ")
    print()


number = 1
for i in range(1, 5):
    for j in range(i):
        print(number, end=" ")
        number = number + 1
    print()


for i in range(1, 6):
    for space in range(5 - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()


for i in range(5, 0, -1):
    for space in range(5 - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()