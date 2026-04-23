class Solution(object):
    def rotate_brute(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        for i in range(k):
            temp = nums[N -1]
            for j in range(N-1, -1, -1):
                nums[j] = nums[j-1]
            nums[0] = temp
        return nums 
    
    def rotate_optimal(self, nums, k):
        N = len(nums)
        k = k % N
        seq1 = nums[::-1]
        result = seq1[0:k][::-1] + seq1[k:N][::-1]
        nums[:] = result
    
    def rotate(self, nums, k):
        N = len(nums)
        k = k % N
        def reverse(l,r):
            while l < r:
                nums[l] , nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums
        nums = reverse(0, N-1)
        nums = reverse(0, k-1)
        nums = reverse(k, N-1)
        return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    obj = Solution()
    result = obj.rotate(nums=nums,k = k)
    print(result)