1# reverse of a number

# n=int(input("enter the number:"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# print("reverse",rev)

2#amstrong number

# num=int(input("enter the number:"))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum=sum+digit*digit*digit
#     temp=temp//10
#
# if sum==num:
#     print(num,"is amstrong")
# else:
#     print(num,"not amstrong")


# print the first 10 numbers

# print("the first 10 numbers:")
# for i in range(1,11):
#     print(i)

#odd numbers
# n=2
# i=0
# for i in range(0,11):
#     if i%2!=0:
#         print(i)


#global variable
# x = "awesome"
#
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#
# myfunc()

# print("Python is " + x)

# import random
# print(random.randrange(0,3))

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# a=("hello")
# print(a[2])
# for x in "banana":
#   print(x)

# txt = "The best things in life are free!"
# print(txt.upper())

# a = "Hello"
# b = "World"
# c = a + "   " + b
# print(c)


a=["apple","banana","orange"]
b=["cherry","blackberry"]
a.extend(b)
print(a)