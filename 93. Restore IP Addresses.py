def doStore(k,tempaddress,addresses,s):
    if k==4 or len(s)==0:
        if k==4 and len(s)==0:
            addresses.append(''.join(tempaddress))
        return
    for i in range(len(s)):
        if i<=2:
            if i!=0 and s[0]== '0':
                break
            part = s[:i+1]
            if int(part)<=255:
                if len(tempaddress)!=0:
                    part = '.'+part
                tempaddress+=part
                doStore(k+1,tempaddress,addresses,s[i+1:])
                del tempaddress[len(tempaddress)-len(part):len(tempaddress)]
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        addresses = []
        tempaddress = []
        doStore(0,tempaddress,addresses,s)
        return addresses

if __name__ == '__main__':
    sol = Solution
    print(sol.restoreIpAddresses(sol,"25525511135"))
