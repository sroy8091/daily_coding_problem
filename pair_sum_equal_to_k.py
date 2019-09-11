"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def pair_sum(arr, k):
    """
    The idea is to create a hash and then check whether the current number is already present 
    if not then current-k will be added
    """
    hash = {}
    for i in arr:
        if hash.get(i):
            return True
        else:
            hash[abs(i-k)] = i
    return False

def main():
    arr = [10, 15, 3, 7]
    k = 17
    print(pair_sum(arr, k))

if __name__=="__main__":
    main()