from typing import List


class SolutionMedium:
    #### ARRAY / STRING #######
    # 80. Remove Duplicates from Sorted Array II
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    #   [E] 2154. Keep Multiplying Found Values by Two
    #   [H] 2926. Maximum Balanced Subsequence Sum
    #   [E] 246. Strobogrammatic Number
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        i = 0      # index for keeped items
        count = 1  # counter of current number
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
            else:
                count = 1

            if count <= 2:
                i += 1
                nums[i] = nums[j]

        return i + 1

    # 189. Rotate Array
    # Runtime: O(n)
    # Space: O(n)
    # More Challenges:
    #   [M] 186. Reverse Words in a String II
    #   [M] 2607. Make K-Subarray Sums Equal
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or len(nums) <= 1: return
        temp = [0] * len(nums)
        for i in range(len(nums)):
            temp[(i + k) % len(nums)] = nums[i]
        nums[:] = temp
        

    # 189. Rotate Array
    # Runtime: O(n)
    # Space: O(1)
    def rotate_space_saver(self, nums: List[int], k: int) -> None:
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        
        if k == 0 or len(nums) <= 0: return
        k = k % len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)

    # 122. Best Time to Buy and Sell Stock II
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    #   [H] 123. Best Time to Buy and Sell Stock III
    #   [H] 188. Best Time to Buy and Sell Stock IV
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_min = prices[0]
        for p in prices[1:]:
            if p > cur_min:
                profit += p - cur_min
            cur_min = p
        return profit