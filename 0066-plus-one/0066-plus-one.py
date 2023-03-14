class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        no = ''
        for x in digits:
            no = no + str(x)
        
        no = int(no) + 1

        rlist = []

        for y in list(str(no)):
            rlist.append(int(y))

        return rlist
