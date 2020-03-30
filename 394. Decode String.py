class Solution:
    def decodeString(self, s):
        if not s or len(s)==0:
            return s
        result,position = self.dfs(0,s,0,"")
        return result
    def dfs(self,position,s,prev_num,prev_str):
        while position <len(s):
            while s[position].isdigit():
                prev_num = prev_num*10+int(s[position])
                position+=1
            if s[position]=="[":
                returned_str,position_end = self.dfs(position+1,s,prev_num=0,prev_str="")
                prev_str = prev_str+returned_str*prev_num
                position = position_end
                prev_num=0
            elif s[position]=="]":
                return prev_str,position
            else:
                prev_str+=s[position]
            position+=1
        return prev_str,position