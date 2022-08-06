class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            center_index = (left + right)//2
            if nums[center_index]==target:
               return center_index
            if target < nums[center_index]:
                right = center_index -1
            if target > nums[center_index]:
                left = center_index +1 
        return -1