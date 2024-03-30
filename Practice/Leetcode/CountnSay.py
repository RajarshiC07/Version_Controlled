from collections import Counter
class Solution:
    def countAndSay(self, n: int) -> str:
        count = 0
        result = '1'
        while count < n:
            if count > 0:
                l = {result[0]:0}
                res = ''
                for i in range(len(result)):
                    if result[i] in l.keys():
                        l[result[i]] = l[result[i]]+1
                    else:
                        res = res + str(l[result[i-1]]) + result[i-1]
                        l[result[i]] = 1
                        l.pop(result[i-1])
                res = res + str(l[result[i]]) + result[i]
                result = res
            count += 1
        return result


obj1 = Solution()
print(obj1.countAndSay(5))

# n = '21'
# res = ''
# l = {n[0]:0}
# count = 0
# for i in range(len(n)):
#     if n[i] in l.keys():
#         # print(n[i])
#         l[n[i]] = l[n[i]]+1
#     else:
#         # print(n[i-1], l[n[i-1]])
#         res = res + str(l[n[i-1]]) + n[i-1]
#         l[n[i]] = 1
#         l.pop(n[i-1])
        
# print(l)
# res = res + str(l[n[i]]) + n[i]
# print(res)


