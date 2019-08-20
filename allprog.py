'''
1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
'''


# text ="Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star, \n\tHow I wonder what you are"
# print(text)


'''
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
'''

# rad=int(input("Enter the radius:"))
# pi=22/7
# area=(pi)*(rad)*(rad)
# area=round(area,3)
# print(area)
#

'''
5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
'''

# first=list(input("Enter the first name:"))
# last =list(input("Enter the last name:"))
# rev_fi=''.join(reversed(first))
# rev_la=''.join(reversed(last))
# full=(rev_fi +' '+ rev_la)
# print(full)

'''
7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java 
Output : java
'''
# txt=input("Enter the input :")
# exten=txt.split('.')
# print(exten[-1])

'''
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5 
Expected Result : 615
'''
# def compute(n):
#     cal=(n)
#     cal1=int('%s%s'%(n,n))
#     cal2=int('%s%s%s'%(n,n,n))
#     print(cal+cal1+cal2)
# compute(int(input("Enter the number to compute :")))
#

'''
16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
'''

# num=int(input("Enter a num:"))
# c=17
# if num<=17:
#     diff=c-num
#     print(diff)
# else:
#     diff=c-num
#     final=abs(diff*diff)
#     print(final)

'''
17. Write a Python program to test whether a number is within 100 of 1000 or 2000. 
'''
# num=input("Enter a num:")
# for i in range(100,2001,100):
#     if num==str(i):
#         print("Given number found:",i)
#         break
# else:
#     print("Given number not found on range:",num)
#

'''
Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum
'''
# num1=int(input("Enter a num1:"))
# num2=int(input("Enter a num2:"))
# num3=int(input("Enter a num3:"))
# sum=(num1+num2+num3)
# if num1==num2==num3:
#     print(sum**3)
# else:
#     print(sum)

'''
Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged
'''
# text=input("Provide a string:")
# first_two=text[:2]
# if first_two=='IS' or first_two=='Is' or first_two=='iS' or first_two=='is':
#     print(text)
# else:
#     add = 'Is' + text
#     print(add)
#

'''
22. Write a Python program to count the number 4 in a given list.
'''
# lst=[1,2,3,4,5,4,2,4,4]
# lst1=[]
# for i in lst:
#     if i==4:
#         lst1.append(i)
#     else:
#         pass
# print(len(lst1))

'''
23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
'''

# txt=input("Enter the text:")
# copy=int(input("Enter the no of copies you want of string:"))
# if len(txt)<=2:
#     print(txt*copy)
# elif len(txt)>2:
#     first_two=txt[:2]
#     print(first_two*copy)

'''
24. Write a Python program to test whether a passed letter is a vowel or not. 
'''
# txt=input("Enter the letter:")
# lower=txt.lower()
# if lower in 'aeiou':
#     print("vowel found")
# else:
#     print("Consonent found")

'''
27. Write a Python program to concatenate all elements in a list into a string and return it.
'''
# lst=[2,3,4,5]
# data=""
# for i in lst:
#     data=data+str(i)
# print(data)

'''
28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
'''
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
#
# for i in numbers:
#     if i%2==0:
#         print(i,'',end='')
#     if i==237:
#         break

'''
Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

Expected Output 
{'Black', 'White'}

'''

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
#
#
# print(color_list_1.difference(color_list_2))

'''
31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. 
'''

# num1=int(input("Enter a num1:"))
# num2=int(input("Enter a num2:"))
# lst1=[]
# lst2=[]
# for i in range(1,num1+1):
#     if num1%i==0:
#         lst1.append(i)
# for i in range(1,num2+1):
#     if num2%i==0:
#         lst2.append(i)
# new_lst=set(lst1).intersection(set(lst2))
# print("The GCD for the given numbers is :",max(new_lst))

'''
LCM
'''
# num1=int(input("Enter a num1:"))
# num2=int(input("Enter a num2:"))
# lst1=[]
# lst2=[]
# for i in range(1,num1+1):
#     if num1%i==0:
#         lst1.append(i)
# for i in range(1,num2+1):
#     if num2%i==0:
#         lst2.append(i)
# new_lst=set(lst1).intersection(set(lst2))
# gcd=max(new_lst)
# multiple =num1*num2
# lcm=(multiple/gcd)
# print(lcm)

'''
1. Write a Python function to find the Max of three numbers.
'''

# def greater(x,y,z):
#     if x>y and x>z:
#         return ("x is grater")
#     elif y>x and y>z:
#         return ("y is grater")
#     elif z>x and z>y:
#         return ("z is grater")
#     else:
#         return ("Given numbers are in equal of value")
# print(greater(2,2,2))
# print(greater(2,3,4))
# print(greater(4,3,2))
# print(greater(2,4,3))

'''
2. Write a Python function to sum all the numbers in a list.
'''
# def sum(lst):
#     final=0
#     for i in lst:
#         final=final+i
#     return final
# print(sum([8, 2, 3, 0, 7]))

'''
5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
'''
# def fact(num):
#     fact = 1
#     for i in range(num,0,-1):
#         fact *=i
#     return fact
# print(fact(int(input("Enter a factorial number:"))))

'''
6.Write a Python function to check whether a number is in a given range.
'''
# def check(num,num1):
#     lst=[]
#     for i in range(1,num+100):
#         lst.append(i)
#     if num1 in lst:
#         print("Number found in given range")
#     else:
#         print("Not in range")
#
# check(5,9)

'''
7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
'''
# def char(txt):
#     up=[]
#     low=[]
#     for i in txt:
#         if i.islower():
#             low.append(i)
#         elif i.isupper():
#             up.append(i)
#     print("lower count is:",len(low))
#     print("upper count is:",len(up))
# char('helloHow')

'''
8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
'''

# def uniq(lst):
#     new_lst=set(lst)
#     return list(new_lst)
#
# print(uniq([1,2,3,3,3,3,4,5]))

'''
9. Write a Python function that takes a number as a parameter and check the number is prime or not.
'''

# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             print("Given number not prime :{}".format(num))
#             break
#     else:
#         print("Given number is prime:")
#
# prime((int(input("Enter a number to check:"))))

'''
0. Write a Python program to print the even numbers from a given list.
'''
# def even(num):
#     even=[]
#     for i in num:
#         if i%2==0:
#             even.append(i)
#     print(even)
# even([1, 2, 3, 4, 5, 6, 7, 8, 9] )

'''
patterns
'''
#
# for i in range(1,6):
#     print(i*'*')

# for i in range(1,6):
#     for j in range (1,i+1):
#         print(j,end='')
#     print()


# for i in range(1,6):
#     for j in range(i):
#         print(i,end='')
#     print()
#

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()
#
# n = 1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(n, end='')
#         n=n+1
#     print()
#
# for i in range(1,6):
#     for j in range(1, i+1):
#         print('*',end='')
#     print()
#

# num=4
# for i in range(1,6):
#     print(' '*num,i*'*')
#     num=num-1

'''
12. Write a Python function that checks whether a passed string is palindrome or not.
'''
# def pali(text):
#     lst=[]
#     for i in text:
#         lst.append(i)
#     lst.reverse()
#     rev=''.join(lst)
#     if text==rev:
#         return True
#     else:
#         return False
# print(pali(text=input("Enter the word :")))


# start=int(input("Enter start no:"))
# end=int(input("Enter end no:"))
#
# for j in range(start,end+1):
#     for num in range(2,j):
#         if j%num==0:
#             #print("Non-primes:",j)
#             break
#     else:
#         print("Prime number:",j)


'''
14. Write a Python function to check whether a string is a pangram or not.
'''
'''
15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
'''

# def hypen(sent):
#     ls_sent=list(sent)
#     print(ls_sent)
#     #return sorted(ls_sent)
# (hypen(input("green-red-yellow-black-white")))

#
# li=('green-red-yellow-black-white')
#
#
# items=[n for n in input("Enter text:").split('-')]
# print(items)
# items.sort()
# print('-'.join(items))
'''
16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included). 
'''
# def sq(num):
#     li=[]
#     for i in range(1,num+1):
#         sq=i*i
#         li.append(sq)
#     return li
# print(sq(30))

'''
5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''
# lst=['abc','cc','xyz','a','aba', '1221']
# new_lst=[]
# final=[]
# for i in lst:
#     if len(i)>=2:
#         new_lst.append(i)
# for j in new_lst:
#     if j[0]==j[-1]:
#         final.append(j)
# print(final,'- count :',len(final))


'''
6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
#lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# def keyvalue(a):
#     return a[1]
# lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# print(sorted(lst,key=keyvalue))



#
# class parent():
#     def __init__(self,c_brand,price):
#         self.brand = c_brand
#         self.price = price
#
#     def display(self):
#         print(self.brand,self.price)
#
#     def update_age(self):
#         self.price = 15000
#
#     def compare(self,c2):
#         if obj1.price == c2.price:
#             return True
#         else:
#             return False
#
#
#
# obj1 = parent('HP',20000)
# obj2 = parent('ACER',15000)
#
# if obj1.compare(obj2):
#     print('price values are same')
# else:
#     print('price values are differ')
#
# obj1.update_age()
#
# if obj1.compare(obj2):
#     print('price values are same')
# else:
#     print('price values are differ')
#


