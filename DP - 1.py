import math
import sys
sys.setrecursionlimit(10000)

# def fibRec(n):
#     if n == 0 or n == 1:
#         return n
#     return fibRec(n-1) + fibRec(n-2)

# print(fibRec(7))


# def fibMemo(n,dp):
#     if n == 0 or n == 1:
#         return n
#     if dp[n-1] == -1:
#         ans1 = fibMemo(n-1,dp)
#         dp[n-1] = ans1
#     else:
#         ans1 = dp[n-1]
#
#     if dp[n-2] == -1:
#         ans2 = fibMemo(n-2,dp)
#         dp[n-2] = ans2
#     else:
#         ans2 = dp[n-2]
#     ans = ans1 + ans2
#     return ans

# n = 7
# dp = [-1 for i in range(n+1)]
# print(fibMemo(n,dp))


# def fibIteravtive(n):
#     dp = [-1 for _ in range(n+1)]
#     dp[0] = 0
#     dp[1] = 1
#     i = 2
#     while i <= n:
#         dp[i] = dp[i-1] + dp[i-2]
#         i += 1
#     return dp[n]
#
# print(fibIteravtive(5))



# import sys
# def minStepsTo1(n, dp):
#     if  n == 1:
#         return 0
#
#     ans1 = sys.maxsize
#     if n % 3 == 0:
#         if dp[n//3] == -1:
#             ans1 = minStepsTo1(n//3, dp)
#             dp[n//3] = ans1
#         else:
#             ans1 = dp[n//3]
#
#     ans2 = sys.maxsize
#     if n % 2 == 0:
#         if dp[n//2] == -1:
#             ans2 = minStepsTo1(n//2, dp)
#             dp[n//2] = ans2
#         else:
#             ans2 = dp[n//2]
#     if dp[n-1] == -1:
#         ans3 = minStepsTo1(n-1,dp)
#         dp[n-1] = ans3
#     else:
#         ans3 = dp[n-1]
#
#     return 1 + min(ans1,ans2,ans3)
#
#
# n = int(input())
# dp = [-1 for _ in range(n)]
# print(minStepsTo1(n,dp))


# def iterMinStepsTo1(n):
#     dp = [-1 for _ in range(n+1)]
#     dp[0] = 0
#     dp[1] = 0
#     i = 2
#     while i <= n:
#         ans1,ans2,ans3 = sys.maxsize,sys.maxsize,sys.maxsize
#         if dp[i] == -1:
#             ans1 = dp[i-1]
#         if i % 2 == 0:
#             x = i//2
#             if dp[i//2] == -1:
#                 ans2 = 1 + dp[x//2]
#             else:
#                 ans2 = dp[i//2]
#
#         if i % 3 == 0:
#             y = i//3
#             if dp[i//3] == -1:
#                 ans2 = 1 + dp[y//3]
#             else:
#                 ans3 = dp[i//3]
#
#         ans = 1+min(ans1,ans2,ans3)
#         dp[i] = ans
#         i += 1
#     return dp[n]
#
#
# print(iterMinStepsTo1(5))



# import math
# def minSquares(n):
#     if n == 0:
#         return 0
#     root = int(math.sqrt(n))
#     ans = sys.maxsize
#     for i in  range(1,root+1):
#         curans = 1 + minSquares(n-(i**2))
#         ans = min(ans,curans)
#     return ans

# print(minSquares(41))


# def minSquares(n,dp):
#     if n == 0:
#         return 0
#     root = int(math.sqrt(n))
#     ans = sys.maxsize
#     for i in  range(1,root+1):
#         checkValue = n-(i**2)
#         if dp[checkValue] == -1:
#             curAns = 1 + minSquares(checkValue,dp)
#             dp[checkValue] = curAns
#         else:
#             curAns = dp[checkValue]
#         ans = min(ans,curAns)
#     return ans
#
#
# n = int(input())
# dp = [-1 for _ in range(n)]
# print(minSquares(n,dp))



# def minSquaresTon(n,dp): #Time complexity is O(n.sqrt(n))
#     if n == 0:
#         return 0
#
#     root = int(math.sqrt(n))
#     ans = sys.maxsize
#     for i in range(1,root+1):
#         checkValue = n-(i**2)
#         if dp[checkValue] == -1:
#             cur_ans = 1 + minSquaresTon(checkValue,dp)
#             dp[checkValue] = cur_ans
#         else:
#             cur_ans = dp[checkValue]
#         ans = min(ans,cur_ans)
#     return ans


# n = 41
# dp = [-1 for _ in range(n)]
# print(minSquaresTon(41,dp))


# import sys, math  #Time complexity is O(n.sqrt(n)) and space complexity is O(n)
# def minSquaresI(n):
#     dp = [-1 for _ in range(n+1)]
#     dp[0] = 0
#
#     for i in range(1,n+1):
#         ans = sys.maxsize
#         root = int(math.sqrt(i))
#         for j in range(1, root+1):
#             currAns = 1 + dp[i - (j*j)]
#             ans = min(ans, currAns)
#         dp[i] = ans
#
#     return dp[n]
#
# print(minSquaresI(41))


# def lisSubseq(arr,i,n):
#     if i == n:
#         return 0,0 #including_max, overallMax
#
#     including_max = 1
#     for j in range(i+1,n):
#         if arr[j] >= arr[i]:
#             further_including_max = lisSubseq(arr,j,n)[0]
#             including_max = max(including_max,1+further_including_max)
#
#     excluding_max = lisSubseq(arr,i+1,n)[1]
#     overallmax = max(including_max,excluding_max)
#     return including_max,overallmax


# a = [6,3,1,2]
# ans = (lisSubseq(a,0,4))[1]
# print(ans)


# def lisMemo(arr, idx, n, dp): #here dp will store a tuple of (including_max, overallMax) for every element
#     if idx == n:
#         return 0, 0 #including_max, overallMax
#
#     including_max = 1
#     for j in range(idx + 1, n):
#         if arr[j] >= arr[idx]:
#             if dp[j] == -1:
#                 ans = lisMemo(arr,j,n,dp)
#                 dp[j] = ans
#                 further_including_max = ans[0]
#             else:
#                 further_including_max = dp[j][0]
#             including_max = max(including_max, 1 + further_including_max)
#
#     if dp[idx+1] == -1:
#         ans1 = lisMemo(arr,idx+1,n,dp)
#         dp[idx+1] = ans1
#         excluding_max = ans1[1]
#
#     else:
#         excluding_max = dp[idx+1][1]
#
#     overallMax = max(including_max,excluding_max)
#     return including_max,overallMax
#
#
# a = [6,3,1,2,0,7,9]
# dp = [-1 for _ in range(len(a)+1)]
# ans =lisMemo(a,0,7,dp)
# print(ans[1])



# def lisI(nums, n):
#     dp = [[0 for _ in range(2)] for _ in range(n+1)]
#
#     for i in range(n-1,-1,-1):
#         including_max = 1
#         for j in range(i+1,n):
#             if nums[j] > nums[i]:
#                 including_max = max(including_max,1+dp[j][0])
#         dp[i][0] = including_max
#         excluding_max = dp[i+1][1]
#         overAllMax = max(including_max,excluding_max)
#         dp[i][1] = overAllMax
#
#     return dp[0][1]
#
#
# arr = [6,3,1,2,0,7,9,10]
# print(lisI(arr,8))



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


# def stairCaseMemo(n,dp):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#
#     if dp[n-1] == -1:
#         one = stairCaseMemo(n-1,dp)
#         dp[n-1] = one
#     else:
#         one = dp[n-1]
#
#     if dp[n-2] == -1:
#         two = stairCaseMemo(n-2,dp)
#         dp[n-2] = two
#     else:
#         two = dp[n-2]
#
#     if dp[n-3] == -1:
#         three = stairCaseMemo(n-3,dp)
#         dp[n-3] = three
#     else:
#         three = dp[n-3]
#
#     return one+two+three
#
# n = 4
# dp = [-1 for _ in range(n+1)]
# print(stairCaseMemo(n,dp))


# def stairCaseI(n):
#     dp = [-1 for _ in range(n+1)]
#     dp[0] = 0
#     dp[1] = 1
#     if n >= 2:
#         dp[2] = 2
#     if n >= 3:
#         dp[3] = 4
#     if n >= 3:
#         for i in range(4,n+1):
#             dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
#     return dp[n]
#
# print(stairCaseI(5))





