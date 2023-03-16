class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        rlist = list(s)
        sum_no = 0
        tmp = ''
        
        for x in rlist:
            if tmp and roman[tmp] < roman[x]:
                sum_no += roman[x] - roman[tmp] * 2
                tmp = x
                continue
            sum_no += roman[x]
            tmp = x
            
        return sum_no
        