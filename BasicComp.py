1.# WAP to calculate square of number
# n= int(input ("Enter a number:"))
# s=n*n;
# print(s);


2.# WAP to calculate Simple Interest
# principal = float(input("Enter an amount:"))
# rate = int(input("Enter a rate:"))
# time = float(input("Enter a time:"))
# SI = (principal*rate*time)/100
# print(SI);

3.# WAP to swap two numbers with and without third variable
# a= int(input("Enter a:"))
# b= int(input("Enter b:"))
# c=a
# a=b
# b=c
# print(a)
# print(b)


4.# WAP to take input for salary if the salary is greater than 32000 then calculate 10% bonus ohterwise 8% bonus. Also calculate total salary 
# salary = float(input("Enter salary:"))
# if(salary>32000):
#     bonus=salary*10/100
# else:
#     bonus=salary*8/100
# print(bonus);    


5.# WAP to find largest number among given 3 numbers
# a = float(input("Enter a:"))
# b = float(input("Enter b:"))
# c = float(input("Enter c:"))
# if(a>=b and a>=c):
#     print(a,"greatest number")
# elif(b>=a and b>=c):
#     print(b,"greatest number")
# else:
#     print(c,"greatest number")        


6.# WAP to take input and check the no. is even, odd and zero
# a=int(input("Enter a:"))
# if(a==0):
#     print("Zero")
# elif(a%2==0):
#     print("Even")
# else:
#     print("Odd")    


7.# WAP to print numbers 1 to 10
# for i in range(1,11):
#     print(i)


8.# WAP to take two numbers and sum between them
# n1=int(input("Enter a number n1:"))
# n2=int(input("Enter a number n2:"))
# sum=0
# for i in range(n1,n2+1):
#     sum+=i
# print(sum)  

9.# WAP to count all the even numbers b/w any given two no.
# n1=int(input("Enter a number n1:"))
# n2=int(input("Enter a number n2:"))
# count=0
# for i in range(n1,n2+1):
#     if(i%2==0):
#         count+=1
# print(count)        


10.# WAP to calculate the factorial of a given no.
# n= int(input("enter a no."))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("the factorial is",fact)


11.# WAP to print table of any given number
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)


12.# WAP to check whether the no. is prime or not 
# num = int(input("Enter a number: "))
# if num < 2:
#     print("Not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")


13.# WAP to take a number and count even digits of that no.
# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     digit = num % 10
#     if digit % 2 == 0:
#         count += 1
#     num = num // 10
# print("Number of even digits =", count)


14.# WAP to check whether the no. is armstrong or not
# num = int(input("Enter a number: "))
# temp = num
# s = 0
# while temp > 0:
#     r = temp % 10
#     s += r ** 3
#     temp //= 10
# if s == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


15.# WAP to check the fabonacci series
# n = int(input("Enter a no.:"))
# a=0
# b=1
# print(a,b,end=" ")
# for i in range (2,n):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c


16.# WAP to count the numbers in fabonacci series
# n = int(input("Enter the number of terms: "))
# a = 0
# b = 1
# count = 0
# print("Fibonacci Series:")
# while count < n:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     count += 1


17.# WAP to check the palindrome no.
# num = int(input("Enter a number: "))
# temp = num
# rev = 0
# while temp > 0:
#     r = temp % 10
#     rev = rev * 10 + r
#     temp //= 10
# if num == rev:
#     print("Palindrome number")
# else:
#     print("Not a palindrome")


18.# WAP of pattern
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()    


19.# WAP of the star pattern
# for i in range(1,7):
#     for j in range(i,7):
#         print("*",end=" " )
#     print()    


20.# WAP for number pattern
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


21.# WAP of star pattern 
# for i in range(1, 6):
#     for j in range(1,i+1):
#         print("*",end= " ")
#     print()
# for i in range(1,5):
#     for j in range(i,5):
#         print("*",end= " ")
#     print()


22.# WAP of pattern
# for i in range(1, 6):
#      for j in range(1,6):
#           if i==1 or i==5:
#                print("*",end= " ")
#           elif j==1 or j==5:
#                print("*",end= " ")    
#           else:
#                print(" ",end= " ")     
#      print()         


23.# Reverse of a number (using while loop)
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     r = num % 10
#     rev = rev * 10 + r
#     num //= 10
# print("Reversed number =", rev)


24.# sum of n natural numbers
# n=int(input("enter a number:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("sum of first",n,"natural numbers:",sum) 


25.# WAP to find the sum of digits of given number
# sum=0
# n=int(input("Enter a no.:"))
# while(n>0):
#     digits=n%10
#     sum+=digits
#     n//=10
# print(sum)    


26.#WAP to check whether it is leap year or not
# year = int(input("Enter a year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("It is a leap year")
# else:
#     print("It is not a leap year")


27.#WAP to check cube and square and product of digits of a given no.
# n = int(input("Enter a number: "))
# square = n ** 2
# cube = n ** 3
# product = 1
# if n == 0:
#     product = 0
# else:
#     while n > 0:
#         digit = n % 10
#         product = product * digit
#         n = n // 10
# print("Square =", square)
# print("Cube =", cube)
# print("Product of digits =", product)


28.#Sum of even digits and product of odd digits of given no.
# num = int(input("Enter a number: "))
# sum_even = 0
# product_odd = 1
# while num > 0:
#     digit = num % 10
#     if digit % 2 == 0:
#         sum_even = sum_even + digit
#     else:
#         product_odd = product_odd * digit
#     num = num // 10
# print("Sum of even digits =", sum_even)
# print("Product of odd digits =", product_odd)


29.#Count total number of factors of given no.
# num = int(input("Enter a number: "))
# count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         count = count + 1
# print("Total number of factors =", count)


30.# WAP to print all the prime numbers between 1 to 100
# for num in range(2, 101):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         print(num, end=" ")


31.# WAP to print armstrong numbers between 100 to 999        
# for num in range(100,1000):
#     temp = num
#     sum = 0
#     while temp > 0:
#         digit = temp% 10
#         sum = sum + digit ** 3
#         temp = temp // 10
#     if sum == num:
#         print(num,end=" ")


32.# WAP to print perfect numbers 1 to 100
# for num in range(1, 101):
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum = sum + i
#     if sum == num:
#         print(num, end=" ")


33.# WAP to print happy numbers
# for num in range(1, 101):
#     n = num
#     while n != 1 and n != 4:
#         sum = 0
#         while n > 0:
#             digit = n % 10
#             sum = sum + digit ** 2
#             n = n // 10
#         n = sum
#     if n == 1:
#         print(num, end=" ")


34.# WAP to print the star pattern
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(" ",end=" ")
#     for j in range(1,i):
#         print("*",end=" ")
#     print()        


35.#WAP to print marksheet
# name = input("Enter student name: ")
# s1 = int(input("Enter marks of Subject 1: "))
# s2 = int(input("Enter marks of Subject 2: "))
# s3 = int(input("Enter marks of Subject 3: "))
# s4 = int(input("Enter marks of Subject 4: "))
# s5 = int(input("Enter marks of Subject 5: "))
# total = s1 + s2 + s3 + s4 + s5
# percentage = total / 5
# print("\n----- MARKSHEET -----")
# print("Name:", name)
# print("Subject 1:", s1)
# print("Subject 2:", s2)
# print("Subject 3:", s3)
# print("Subject 4:", s4)
# print("Subject 5:", s5)
# print("Total Marks:", total)
# print("Percentage:", percentage, "%")
# if (percentage >= 90):
#     print("Grade: A+")
# elif (percentage >= 80):
#     print("Grade: A")
# elif (percentage >= 70):
#     print("Grade: B")
# elif (percentage >= 60):
#     print("Grade: C")
# elif (percentage >= 50):
#     print("Grade: D")
# else:
#     print("Grade: F")


36.# WAP that takes the number of electricity units consumed and calculates the bill:
# First 100 units Rs.5 per unit 
# Next 100 units Rs.7 per unit  
# Above 200 units Rs.10 per unit
# Use a for loop to process bills for 5 customers.   

# for customer in range(1, 6):
#     units = int(input("Enter the units consumed: "))
#     if units <= 100:
#         bill = units * 5
#     elif units <= 200:
#         bill = (100 * 5) + ((units - 100) * 7)
#     else:
#         bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
#     print("Customer", customer, "Bill = Rs.", bill)
#     print()


# 37. Process 5 customers using a for loop.
# Discount rules:
# Purchase Amount      Discount
# Rs.10,000 or more         20%
# Rs.5,000 or Rs.9,999      10%
# Rs.2,000 or Rs.4,999      5%
# Below Rs.2,000            No discount
# Calculate and display :
# Original amount
# Discount
# Final amount

# highest_discount = 0
# highest_customer = 0
# for customer in range(1, 6):
#     amount = float(input("Enter purchase amount: "))
#     if amount >= 10000:
#         discount = amount * 20 / 100
#     elif amount >= 5000:
#         discount = amount * 10 / 100
#     elif amount >= 2000:
#         discount = amount * 5 / 100
#     else:
#         discount = 0
#     final_amount = amount - discount
#     print("\nCustomer", customer)
#     print("Original Amount =", amount)
#     print("Discount =", discount)
#     print("Final Amount =", final_amount)
#     # Check highest discount
#     if discount > highest_discount:
#         highest_discount = discount
#         highest_customer = customer
# print("\nHighest Discount =", highest_discount)
# print("Customer", highest_customer, "got the highest discount")


#38. Given a list of integers , calculate the sum of all elements
# list1= [1,2,3,4,5]
# sum=0
# for i in list1 :
#     sum=sum+i
# print("the sum is :",sum)


#39. Find the largest element in a list without using max()
# numbers = [10, 25, 7, 45, 32, 18]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print("Largest element:", largest)


#40. WAP count how many even and odd numbers are present in a list 
# numbers = [10, 15, 22, 33, 40, 51, 64, 77]
# even = 0
# odd = 0
# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even numbers:", even)
# print("Odd numbers:", odd)


#41. Check whether a given number exists in a list
# numbers = [10, 20, 30, 40, 50]
# num = int(input("Enter a number: "))
# if num in numbers:
#     print("Number exists in the list")
# else:
#     print("Number does not exist in the list")


#42. WAP reverse of numbers without using rev() method
# numbers = [10, 20, 30, 40, 50]
# reverse = []
# for i in range(len(numbers) - 1, -1, -1):
#     reverse.append(numbers[i])
# print("Original list:", numbers)
# print("Reversed list:", reverse)


#43. Find the second-largest distinct element without using sort()
# l = [10,20,30,40,50,]
# large = 0
# second = 0
# for i in l:
#     if i > large:
#         large = i 
# for i in l:
#     if large > i:
#         second = i
# print(second)                


#44. Remove duplicate elements from a list while maintaining the original order 
# list1= [1,2,2,3,4]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)


#45. Find the elements that are present in both the lists.
# list1= [1,2,3,4,5,6]
# list2=[1,2,3,8,9]
# for x in list1:
#     for y in list2:
#         if x==y:
#             print("the common element is:",x)


#46. Count how many times each element occurs in a list
# numbers = [1, 2, 2, 3, 1, 4, 2, 3]
# count = {}
# for num in numbers:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1
# print(count)


#47. Transaction code
# withdrawl = [500 , 2000 , 15000 , 8000 , 25000 , 1000]
# bal = 50000
# for i in withdrawl:
#     if i>0:
#         if i%100==0:
#             if i<=20000:
#                 print("Transaction Successfull")
#                 bal = bal-i
#             else:
#                 print("Appropriate error")
#         else:
#                 print("Appropriate error")
#     else:
#                     print("Appropriate error")
# print("Remaining Balance in: ",bal)     


#48. Bank code
# age = [25, 35, 42, 19, 52]
# salary = [30000, 55000, 75000, 25000, 90000]
# credit_score = [720, 650, 780, 750, 600]
# for i in range(5):
#     if age[i] < 21:
#         print("Customer", i + 1)
#         print("Not Eligible")
#         print("Reason: Age is below 21")
#     elif salary[i] < 30000:
#         print("Customer", i + 1)
#         print("Not Eligible")
#         print("Reason: Salary is below 30000")
#     elif credit_score[i] < 700:
#         print("Customer", i + 1)
#         print("Not Eligible")
#         print("Reason: Credit Score is below 700")
#     else:
#         print("Customer", i + 1)
#         print("Eligible")
#     print()               


#49. WAP to count the vowels 
# n="Shriya"
# count=0
# for i in n:
#     if i in "aeiou":
#         print(i, "is a vowel")
#         count+=1
#     else:
#         print(i, "is a consonant")
# print("Total vowels:", count)


#50. WAP to count Peak numbers in any given array
# arr = [1, 3, 2, 5, 4, 7, 6]
# count = 0
# for i in range(len(arr)):
#     if i == 0:
#         if arr[i] > arr[i + 1]:
#             count += 1
#     elif i == len(arr) - 1:
#         if arr[i] > arr[i - 1]:
#             count += 1
#     else:
#         if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
#             count += 1
# print("Number of peak elements:", count) 


#51. E-Commerce - Best Product Pair
# prices = [1200, 2500, 1800, 3200, 1500]
# budget = 4300
# for i in range(len(prices)):
#     for j in range(i + 1, len(prices)):
#         if prices[i] + prices[j] == budget:
#             print([i, j])


#52. Product of array except self
# n = [1,2,3,4]
# ans = []
# for i in range(0,4):
#     product=1
#     for j in range(0,4):
#         if j==i:
#             continue
#         product=product*n[j]
#     ans.append(product)    
# print(ans)        
    

#53. Given an integer array nums, return all the triplets
# num = [-1,0,1,2,-1,-4]
# arr = []
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         for k in range(j+1,len(num)):
#             if num[i]+num[j]+num[k]==0:
#                 arr.append([num[i],num[j],num[k]])
# print(arr)


#54.  reverse of the string
# s="hello world"
# rev=s[::-1]
# print (rev)


#55. palindrome check using string
# s= input ("enter a name:")
# if s ==s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")  


#56. first non - repeating characters
# n=input("Enter a name: ") 
# for i in n:
#   if n.count(i)==1:
#     print("first non - repeating character: ",i)
#     break
# else:  
#     print("No non - repeating character")


#57. Check anagram
# n1 = input("Enter first name: ")
# n2 = input("Enter second name: ") 
# if sorted(n1)==sorted(n2):
#       print("anagram") 
# else:
#       print("not an anagram") 


#58. Creating a dictionary
# EMPTY DICTIONARY
# d = {}
# print(d)

#USING A DICTIONARY LITERAL
# student = {
#     'id': 101,
#     'name': 'Amit',
#     'marks': 85
# }
# print(student)

#USING dict() CONSTRUCTOR
# d = dict(name='Amit', age=21)
# print(d)

#FROM PAIRS
# d = dict([('A', 10), ('B', 20)])
# print(d)


#59. Accessing values
# Suppose if we have
# student = {
#     'id': 101,
#     'name': 'Amit',
#     'marks': 85
# }

#DIRECT ACCESS
# print(student['name'])

#IF THE KEY DOESN'T EXIST
# print(student['email'])

#SAFE LOOKUP -  GET
# print(student.get('name'))

#IF THE KEY DOESN'T EXIST OF GET
# print(student.get('email'))

#GIVE YOUR OWN DEFAULT VALUE
# print(student.get('email', 'Not Found'))


#60. Frequency of array using dictionary function
# arr = [1, 2, 2, 3, 1, 4, 2, 3]
# freq = {}
# for i in arr:
#     if i in freq:
#         freq[i] = freq[i] + 1
#     else:
#         freq[i] = 1
# print(freq)


#61. Stack code
# sub=[]
# while True:
#     print(" 1.push \n 2.pop \n 3.peek \n 4.display \n 5.exit")
#     ch=int(input("Enter your choice : "))
#     if ch==1:
#         x=int(input("Enter number of elements to push : "))
#         for i in range(x):
#             n=int(input("Enter a number : "))
#             sub.append(n)
#     elif ch==2:
#         if len(sub)==0:
#             print("Stack is empty")
#         else:
#             print("Popped element is :", sub.pop())
#     elif ch==3:
#         if len(sub)==0:
#             print("Stack is empty")
#         else:
#             print("Top element is :", sub[-1])
#     elif ch==4:
#         print("Stack elements are :", sub)
#     elif ch==5:
#         break
#     else:
#         print("Invalid choice")


#62. stack using list in fuction
# def push():
#     x=int(input("Enter number of elements to push : "))
#     for i in range(x):
#         n=int(input("Enter a number : "))
#         sub.append(n)
#     def pop():
#         if len(sub)==0:
#             print("Stack is empty")
#         else:
#             print("Popped element is :", sub.pop())                                     
#     def peek():
#         if len(sub)==0:
#             print("Stack is empty")
#         else:
#             print("Top element is :", sub[-1])
#     def display():
#         print("Stack elements are :", sub)
#     def main():
#         while True:
#             print(" 1.push \n 2.pop \n 3.peek \n 4.display \n 5.exit")
#             ch=int(input("Enter your choice : "))
#             if ch==1:
#                 push()
#             elif ch==2:
#                 pop()
#             elif ch==3:
#                 peek()
#             elif ch==4:
#                 display()
#             elif ch==5:
#                 break
#             else:
#                 print("Invalid choice")
                
                
#63. queue using list
# q=[]
# while True:
#     print(" 1.enqueue \n 2.dequeue \n 3.peek \n 4.display \n 5.exit")
#     ch=int(input("Enter your choice : "))
#     if ch==1:
#         x=int(input("Enter number of elements to enqueue : "))
#         for i in range(x):
#             n=int(input("Enter a number : "))
#             q.append(n)
#     elif ch==2:
#         if len(q)==0:
#             print("Queue is empty")
#         else:
#             print("Dequeued element is :", q.pop(0))
#     elif ch==3:
#         if len(q)==0:
#             print("Queue is empty")
#         else:
#             print("Front element is :", q[0])
#     elif ch==4:
#         print("Queue elements are :", end=" ")
#         for i in range(len(q)):
#             print(q[i], end=" ")
#         print()
#     elif ch==5:
#         break
#     else:
#         print("Invalid choice")


#64. enqueue and dequeue using function
# q=[0]*3
# f=-1
# r=-1
# def enqueue():
#     global f,r
#     if r==len(q)-1:
#         print("Queue is overflow")
#     else:
#         n=int(input("Enter a number : "))
#         if f==-1:
#             f=0
#         r+=1
#         q[r]=n

# def dequeue():
#     global f,r
#     if f==-1 or f>r:
#         print("Queue is underflow")
#     else:
#         print("Dequeued element is :", q[f])
#         f+=1

# print("1.enqueue \n 2.dequeue \n 3.peek \n 4.display \n 5.exit")
# ch=int(input("Enter your choice : "))
# while ch!=5:
#     if ch==1:
#         enqueue()
#     elif ch==2:
#         dequeue()
#     elif ch==3:
#         if f==-1 or f>r:
#             print("Queue is empty")
#         else:
#             print("Front element is :", q[f])
#     elif ch==4:
#         if f==-1 or f>r:
#             print("Queue is empty")
#         else:
#             print("Queue elements are :", end=" ")
#             for i in range(f,r+1):
#                 print(q[i], end=" ")
#             print()
#     else:
#         print("Invalid choice")


#65. Make an array program 
# from array import array
# i = []
# arr = array[1, 2, 3, 4, 5]
# print(arr)


#66. Array functions
# from array import array
# arr = array('i',[1,2,3,4,5])
# for i in range(len(arr)):
#     print(arr[i])  #Iterating through the array

# arr.append(6)  #Adding an element to the end of the array
# print(arr)

# arr.extend([7,8,9])  #Adding multiple elements to the end of the array
# print(arr)

# arr.insert(2,4)  #Inserting an element at a specific index
# print(arr)

# arr.remove(2)  #Removing an value from the array
# print(arr)

# arr.pop(3)  #Removing an element at a specific index
# print(arr.index(4))

# arr.count(4)  #Counting the occurences of an element
# print(arr.count(1))

# arr.reverse()  #Reversing an array
# print(arr)


#67. Insertion sort
# from array import array
# num = array('i',[50, 20, 40, 10, 30])
# for i in range(1, len(num)):
#     key = num[i]
#     j = i - 1
#     while j>=0 and num[j] > key:
#         num[j+1] = num[j]
#         j-=1
#     num[j+1] = key
# print(num)        


#68. find second largest element in an array
# from array import array
# arr = array('i', [10, 20, 30, 40, 50])
# largest = arr[0]                          
# second_largest = arr[0]
# for i in range(len(arr)): 
#     if arr[i] > largest:
#         second_largest = largest
#         largest = arr[i]    
#     elif arr[i] > second_largest and arr[i] != largest:
#         second_largest = arr[i]                                                 
# print("Second largest element is:", second_largest)


#69. Move all zeroes to the end of an array
# from array import array
# arr = array('i', [0, 1, 0, 3, 12])
# non_zero_index = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr[non_zero_index] = arr[i]
#         non_zero_index += 1
# for i in range(non_zero_index, len(arr)):     
#         arr[i] = 0
# print("Array after moving zeroes to the end:", arr)


#70. find the missing number in an array
# from array import array
# arr = array('i', [1, 2, 3, 5])
# n = len(arr) + 1
# total_sum = n * (n + 1) // 2
# arr_sum = sum(arr)
# missing_number = total_sum - arr_sum
# print("The missing number is:", missing_number)


#71. WAP to count the given digit found in the number
# num = int(input("Enter a number: "))
# digit = int(input("Enter the digit to count: "))
# count = 0
# temp = num
# while temp > 0:
#     rem = temp % 10
#     if rem == digit:
#         count += 1
#     temp //= 10
# print("The digit", digit, "is found", count, "times")


#72. You are a given a positive integer A. You have to find the value of cube of A
# A = int(input("Enter a positive integer: "))
# cube = A ** 3
# print("Cube of", A, "is", cube)


#73. WAP to print square of all numbers for x to y
# x = int(input("Enter the starting number: "))
# y = int(input("Enter the ending number: "))
# for i in range(x, y + 1):
#     print("Square of", i, "is", i ** 2)


#74. In a class of n students ,each student's marks are given in a list . A student passes if their marks are greater than or equal to 35
# WAP to count the number of students who passed and failed the exam
# n = int(input("Enter the number of students: "))
# marks = []                  
# for i in range(n):
#     mark = int(input(f"Enter marks for student : "))
#     marks.append(mark)
# pass_count = 0
# fail_count = 0  
# for mark in marks:
#     if mark >= 35:
#         pass_count += 1
#     else:
#         fail_count += 1
# print("Number of students who passed:", pass_count)
# print("Number of students who failed:", fail_count)


#75. A store keeps a list of sales of n products. Each product has a sales count. The manager wants to print the highest - selling product count and the lowest - selling product count.
# n = int(input("Enter the number of products: "))
# sales = []
# for i in range(n):
#     count = int(input(f"Enter sales count for product {i + 1}: "))
#     sales.append(count)   
# highest_selling = max(sales)
# lowest_selling = min(sales)
# print("Highest selling product count:", highest_selling)
# print("Lowest selling product count:", lowest_selling)      


#77. WAP to print a string containing both single and double quotes
# string = 'He said, "Python is easy" and I said, \'Yes, it is.\''
# print(string)


#78. WAP to print a string containing the triple quotes in python 
# string = """He said, "Python is easy" and I said, 'Yes, it is.'"""
# print(string)


#79. WAP to 










       








































