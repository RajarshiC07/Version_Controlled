class Solution:
    def removeDigit(self, number, digit):
        index = max_num = 0
        while index < len(number):
            if number[index] == digit:
                l = list(number)
                l.pop(index)
                max_num = max(int(''.join(l)), max_num)
            index+=1
        return str(max_num)