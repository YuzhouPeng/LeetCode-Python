class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people==None or len(people)==0 or len(people[0])==0:
            return []

        def comparenumber(pp):
            return -pp[0],pp[1]

        people.sort(key = comparenumber)
        for i in range(len(people)):
            if (people[i][1]==i):
                continue
            tmp = people[i]
            people.pop(i)
            people.insert(tmp[1],tmp)
        return people