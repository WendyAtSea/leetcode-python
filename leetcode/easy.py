from typing import List

class SolutionEasy:
    ##### ARRAY / STRING ######
    # 88. Merge Sorted Array
    # Runtime: O(m+n)
    # Space: O(1)
    # More challenges:
    #   [M] 986. Interval List Intersections
    #   [M] 2516. Take K of Each Character From Left and Right
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1  # index of nums1
        p2 = n - 1  # index of nums2
        for i in range(m+n-1, -1, -1):
            if p2 < 0: break

            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1

    # 27. Remove Element
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    #   [M] 40. Combination Sum II
    #   [H] 3013. Divide an Array Into Subarrays With Minimum Cost II
    #   [E] 2176. Count Equal and Divisible Pairs in an Array
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        while i < k:
            if nums[i] == val:
                k -= 1
                nums[i] = nums[k]
            else:
                i += 1
        return k

    # 26. Remove Duplicates from Sorted Array
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    #   [E] 2460. Apply Operations to an Array
    #   [M] 2615. Sum of Distances
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
    # 169. Majority Element 
    # Using Boyer-Moore Voting Algorithm
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    #   [M} 229. Majority Element II
    #   [E] 1150. Check If a Number Is Majority Element in a Sorted Array
    #   [E] 2404. Most Frequent Even Element
    def majorityElement(self, nums: List[int]) -> int:
        # TODO
        result = 0