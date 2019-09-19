"""

"""


def sort_binary(arr):
    p = len(arr) - 1
    i = -1

    for j in range(p):
        if arr[j] != arr[p]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[p] = arr[p], arr[i+1]
    return arr


def main():
    arr = [0, 0, 1, 0, 1, 1, 1, 0]
    print(sort_binary(arr))

if __name__=="__main__":
    main()
