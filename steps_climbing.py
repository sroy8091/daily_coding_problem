"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number 
from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 
steps at a time.
"""


def unique_ways(n, arr):
    dp = [0] * n
    arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i]-1<n:
            dp[arr[i]-1] = 1
    for j in range(arr[0], n):
        for k in range(len(arr)):
            if j-arr[k] >= 0:
                dp[j] += dp[j-arr[k]]
    return dp[-1]


def main():
    print(unique_ways(4, [1,3,5]))

if __name__=="__main__":
    main()
