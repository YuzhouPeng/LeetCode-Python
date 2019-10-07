class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        asc = list(seats)
        des = list(seats[::-1])
        count = 0
        disa = []
        disb = []

        for i in range(len(seats)):
            if asc[i] == 1:
                count = 0
                disa.append(0)
            if asc[i] == 0:
                count += 1
                disa.append(count)

        count = 0
        for i in range(len(seats)):
            if des[i] == 1:
                count = 0
                disb.append(0)

            if des[i] == 0:
                count += 1
                disb.append(count)

        disb = (disb[::-1])
        # print(disa)
        # print(disb)
        flaga = 1
        flagb = 1

        for i in range(len(seats)):
            if disa[i] != i:
                flaga = 0
            if disb[i] != len(seats) - i - 1:
                flagb = 0
        if flaga == 1 and flagb != 1:
            return len(seats) - 1
        elif flaga != 1 and flagb == 1:
            return len(seats) - 1
        maxvalue = 0
        results = []
        for i in range(1, len(seats) - 1):
            results.append(min(disa[i], disb[i]))
        results.append(max(disa[0], disb[0]))
        results.append(max(disa[len(seats) - 1], disb[len(seats) - 1]))

        maxvalue = max(results)
        return maxvalue

