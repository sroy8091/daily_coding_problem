"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the 
largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5
"""


def largest_sum(arr):
    inc = arr[1]
    exc = arr[0]

    for i in range(2, len(arr)):
        new_exc = max(inc, exc)

        inc = exc + arr[i]
        exc = new_exc
    return max(inc, exc)


def main():
    arr = [2, 4, 6, 2, 5]
    assert largest_sum(arr) == 13
    arr = [5, 5, -10, 100, 10, -5]
    assert largest_sum(arr) == 105

if __name__=="__main__":
    main()
