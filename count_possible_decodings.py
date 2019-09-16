"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def count_decodings(s):
    """
    The idea is to use of fibonacci solution
    """

    if len(s) == 1:
        return 1
    if len(s) == 2:
        return 2
    including_last_digit = 0
    including_last_two_digit = 0
    if int(s[-1]) > 0:
        including_last_digit = count_decodings(s[:-1])
    if int(s[-2:]) < 28:
        including_last_two_digit = count_decodings(s[:-2])
    return including_last_digit + including_last_two_digit
    


def main():
    s = "1234"
    print(count_decodings(s))

if __name__=="__main__":
    main()