#TODO kunal assignment easy and medium

# def print_tri(a,n):
#     if len(a) == 0:
#         return
#     l = []
#     for i in range(n-1):
#         ele = a[i] + a[i+1]
#         l.append(ele)
#     print(a)
#     print_tri(l,n-1)
#     # print(a)
#
#
# l = [1,2,3,4]
# print_tri(l,4)


# def print_tri(a, n, twoD):
#     if n == 1:
#         twoD.append(a)
#         return
#     l = []
#     for i in range(n-1):
#         ele = a[i] + a[i+1]
#         l.append(ele)
#     # print(a)
#     print_tri(l, n - 1, twoD)
#     twoD.append(a)
#
#
# def print2d(a,n):
#     twoD = []
#     print_tri(a,n,twoD)
#     return twoD
#
#
# l = [1,2,3,4,5]
# print(print2d(l,5))


# def maxi(a,n):
#     if n == 1:
#         return a[0]
#     return max((a[n-1]),maxi(a,n-1))

# def maxi(a,i=0):
#     if i == len(a)-1:
#         return a[i]
#
#     small = maxi(a,i+1)
#     if small > a[i]:
#         return small
#     return a[i]
#
#
# a = [1,2,3,4,7]
# print(maxi(a))

# def max_min(a,i,n): #todo both at once , Best method , do dryrun!!!
#     if i == n: #if 1 element
#         return a[0],a[0] #max,min
#
#     maxi, mini = max_min(a,i+1,n)
#     maxele = max(a[i],maxi)
#     minele = min(a[i],mini)
#     return maxele,minele
#
# def returnMaxMin(a):
#     i = 0
#     n = len(a)
#     maxi, mini = max_min(a,i,n)
#     return maxi, mini
#
#
# arr = [21,9,8,4,11,10,7]
# print(returnMaxMin(arr))


# def search(nums,target):
#     si = 0
#     ei = len(nums) - 1
#     return helper(nums,target,si,ei)
#
# def helper(nums,target,si,ei):
#     if si > ei:
#         return -1
#     mid = (si+ei)//2
#     if nums[mid] > target:
#         return helper(nums,target,si,mid-1)
#     elif nums[mid] < target:
#         return helper(nums,target,mid+1,ei)
#     else:
#         return mid
#
# a = [-1,0,3,5,9,12]
# print(search(a,2))


# def checkSorted(a,ind,n):
#     if ind == n-1:
#         return True
#     if a[ind] > a[ind+1]:
#         return False
#     return checkSorted(a,ind+1,n)
#
#
# a = [1,2,3,4,1]
# print(checkSorted(a,0,5))




# def length_str(s):
#     if len(s) == 0:
#         return 0
#     return 1 + length_str(s[1:])
#
# s = 'abcd'
# print(length_str(s))


# def fn(p,q,r,s): #geekanocci series
#     if s == p or s==q or s == r:
#         return s
#     a =  fn(p,q,r,s-1)
#     b = fn(p,q,r,s-2)
#     c = fn(p,q,r,s-3)
#     return a+b+c


# n = int(input())
# while n:
#     a,b,c,d = input().split()
#     print(fn(int(a),int(b),int(c),int(d)))
#     n = n - 1



# class Solution:
#     # function sort the stack such that top element is max
#     def sorted(self, s):
#         if s:
#             top = s.pop()
#             self.sorted(s)
#             self.inserted(s,top)
#
#     def inserted(self,s,x):
#         if not s or x > s[-1]:
#             s.append(x)
#         else:
#             temp = s.pop()
#             self.inserted(s, x)
#             s.append(temp)
#
#
# def rec(a,sv=0):
#     count = 0
#     n = len(a)
#     for i in range(n):
#             count += rec(a,i)
#     return count
#
#
# a = [1,2,9,12,14]
# print(rec(a))


#CN
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
