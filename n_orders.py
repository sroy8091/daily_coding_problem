"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller 
    than or equal to N.

You should be as efficient with time and space as possible.
"""


class Log(object):
    def __init__(self, n):
        self._log = []
        self.n = n
        self.current = 0

    def record(self, order_id):
        if len(self._log) >= self.n:
            self._log[self.current] = order_id
        else:
            self._log.append(order_id)
        self.current = (self.current + 1) % self.n

    def get_last(self, i):
        return self._log[self.current-i]



def main():
    l = Log(3)
    for i in range(5):
        l.record(i)
    print(l.get_last(1), l._log)

if __name__=="__main__":
    main()