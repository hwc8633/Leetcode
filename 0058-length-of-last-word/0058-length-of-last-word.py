class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rlist = s.split()
        rword = rlist[len(rlist)-1]
        rsize = len(rword)
        
        return rsize