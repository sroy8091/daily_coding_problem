"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that 
contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct 
characters is "bcb"
"""


def longest_substr(s, k):
    i = 0
    j = 1
    d = {}
    d[s[i]] = 1
    length_of_d = 1
    max_sub = 0
    while i<j and j < len(s):
        if d.get(s[j]):
            d[s[j]] += 1
        else:
            d[s[j]] = 1
            length_of_d += 1
        if length_of_d == k:
            max_sub = max(max_sub, (j-i)+1)
            j += 1
        elif length_of_d > k:
            while length_of_d != k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    length_of_d -= 1
                i += 1
        else:
            j += 1
    return max_sub

def main():
    print(longest_substr("abcba", 2))

if __name__=="__main__":
    main()