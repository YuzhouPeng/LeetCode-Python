import collections
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = []
        counter = [0 for i in range(n+1)]
        for i in range(len(bookings)):
            left = bookings[i][0]
            right = bookings[i][1]
            counter[left-1] +=bookings[i][2]
            counter[right] -=bookings[i][2]
        for i in range(1,n):
            counter[i] +=counter[i-1]
        return counter[:-1]