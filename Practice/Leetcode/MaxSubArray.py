class Solution:
    max_val = -999999
    def maxSubArray(self, nums: list[int]) -> int:
        self.max(nums, 0, (len(nums)-1))
        return self.max_val
        
    def max(self, arr, lindex, uindex):
        curr_Sum = sum(i for i in arr)
        if curr_Sum > self.max_val:
            self.max_val = curr_Sum
        if lindex == len(arr)-1 or uindex == 0:
            return
        else:
            self.max(arr[lindex+1::], lindex+1, uindex)
            self.max(arr[:uindex-1:], lindex, uindex-1)
#enter


    

obj = Solution()
print(obj.maxSubArray([1,-1,3, 5, 7]))
