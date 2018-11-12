def getordefault(hashmap,key):
    if key in hashmap:
        hashmap[key] = hashmap[key]+1
    else:
        hashmap[key] = 1

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequencyfornum = {}
        for c in s:
            getordefault(frequencyfornum,c)
        frequencybucket = [[]for j in range(len(s)+1)]
        for c in frequencyfornum:
            f = frequencyfornum[c]
            frequencybucket[f].append(c)

        stringbuilder = []
        for i in range(len(frequencybucket)-1,-1,-1):
            if frequencybucket[i] == None:
                continue
            for c in frequencybucket[i]:
                for j in range(0,i):
                    stringbuilder.append(c)


        return ''.join(stringbuilder)

