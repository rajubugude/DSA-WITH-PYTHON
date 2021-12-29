# def geomentric_sum(k):
#     if k == 0:
#         return 1
#     s = 1/pow(2,k)
#     small = s + geomentric_sum(k-1)
#     return small
#
#
# s = (geomentric_sum(3))
# print('{:.5f}' .format(s))



# def check_palindrome(a,si,ei):
#     if si >= ei:
#         return True
#     if a[si] != a[ei]:
#         return False
#     return check_palindrome(a,si+1,ei-1)
#
#
# s = 'asdfdsa'
# print(check_palindrome(s,0,len(s)-1))



# def sum_strings(s):
#     if len(s) == 1:
#         return s[0]
#     return s[0]+sum_strings(s[len(s)-1])
#
#
# print(sum_strings('51345462'))



# def multiplication(m,n):
#     if n == 1:
#         return m
#     return m + multiplication(m,n-1)
#
#
# print(multiplication(7,5))



#todo STAIRCASE (using recursion)

# def staircase(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     one = staircase(n-1)
#     two = staircase(n-2)
#     three = staircase(n-3)
#     return one+two+three
#
#
# print(staircase(4))


# n = int(input())
# if n == 1 or n == 2:
#     print(n)
# if n == 3:
#     print(4)
# a=1
# b=2
# c=4
# i = 3
# while (i < n):
#     d = a+b+c
#     a = b
#     b = c
#     c = d
#     i = i + 1
# print(c)


# n = int(input())
# if n == 1 or n == 2:
#     print(n)
# a=1
# b=1
# c=2
# i=2
# for i in range(3,n):
#     d=a+b+c
#     a=b
#     b=c
#     c=d
# print(c)

# def power(x, y):
#     if y == 0:
#         return 1
#     temp = power(x, int(y / 2))#%10000000007
#     # print(temp)
#     if y % 2 == 0:
#         return temp * temp
#     else:
#         if y > 0:
#             return x * temp * temp
#         else:
#             print(temp)
#             return (temp * temp) / x
#
#
# print(power(2,-5))


# def triangle(a):
#     lst =[]
#     if len(a) == 0:
#         return
#
#     for i in range(len(a)-1):
#         lst.append(a[i]+a[i+1])
#     triangle(lst)
#     print(a)
#
#
# arr = [1,2,3,4]
# triangle(arr)

# def arraySortedOrNot(arr,n):
#     if n == 1 or n == 0:
#         return True
#     if arr[n-2] == arr[n-1]:
#         return True
#     if arr[n-2] > arr[n-1]:
#         return False
#     return arraySortedOrNot(arr,n-1)
#
#
# a=[90, 100, 200, 400, 500, 600, 700, 900]
# print(arraySortedOrNot(a,3))







