class Solution:
    def findContentChildren(self, g, s) -> int:
        s = sorted(s)
        g = sorted(g)
        i = j = count = 0
        while i < len(g) and j<len(s):     
            if s[j]>=g[i]:             
                count+=1
                i+=1
            j+=1
        return count