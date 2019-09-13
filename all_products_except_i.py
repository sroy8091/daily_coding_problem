"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def product(arr):
    """
    The idea is to create two array with products till 
    """
    left = [1]
    right = [1] * len(arr)
    res = []
    p = 1
    for i in range(1, len(arr)):
        p = p*arr[i-1]
        left.append(p)
    
    p = 1
    for i in range(len(arr)-2, -1, -1):
        p = p*arr[i+1]
        right[i] = p
    
    for i, j in zip(left, right):
        res.append(i*j)
    
    return res




def main():
    arr = [10, 15, 3, 7]
    print(product(arr))

if __name__=="__main__":
    main()