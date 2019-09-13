"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3
"""

def swap_positions(list, pos1, pos2): 
    get = list[pos1], list[pos2] 
    list[pos2], list[pos1] = get 
       
    return list

def segregate(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            swap_positions(arr, i ,j)
            j += 1
    return j

def find_missing(arr):
    j = segregate(arr)
    for i in range(j, len(arr)):
        if arr[i] - 1 < len(arr)-1 and arr[arr[i]-1] > 0:
            arr[arr[i]-1] = -arr[arr[i]-1]
    
    for i in range(len(arr)):
        if arr[i] > 0:
            return i + 1

    


def main():
    arr = [3, 4, -1, 1]
    print(find_missing(arr))

if __name__=="__main__":
    main()