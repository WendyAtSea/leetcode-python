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
    
    # 28. Find the Index of the First Occurrence in a String
    # Rabin-Karp algorithm (Double Hash)
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    # [H] 214. Shortest Palindrome
    # [H] 459. Repeated Substring Pattern   
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        if n < m: return -1

        # constants
        # RADIX_1 as the radix of the first hashing mechanism. It should be at least 262626.
        RADIX_1 = 26 
        # MOD_1 as the modulus for the first hashing mechanism. It should be a large prime number.
        MOD_1 = 10**9+33
        # MAX_WEIGHT_1 as the maximum weightage for the first hashing mechanism. 
        # It will be RADIX_1 m^{m}. This value is used in the O(1)O(1)O(1) formula. Hence, it's better to store it.
        MAX_WEIGHT_1 = 1
        # RADIX_2 as the radix of the second hashing mechanism. It should be at least 262626, and different from RADIX_1.
        RADIX_2 = 27
        # MOD_2 as the modulus for the second hashing mechanism. It should be a large prime number, and different from MOD_1.
        MOD_2 = 2**31-1
        # MAX_WEIGHT_2 as the maximum weightage for the second hashing mechanism. 
        # It will be RADIX_2 m^{m}. This value is used in the O(1)O(1)O(1) formula. Hence, it's better to store it.
        MAX_WEIGHT_2 = 1

        for _ in range(m):
            MAX_WEIGHT_1 = (MAX_WEIGHT_1 * RADIX_1) % MOD_1
            MAX_WEIGHT_2 = (MAX_WEIGHT_2 * RADIX_2) % MOD_2

        # Define the hash_pair() function which takes a string as input and returns the hash value pair of the string.
        # Compute the hash value of the first hashing mechanism using RADIX_1, and MOD_1.
        # Compute the hash value of the second hashing mechanism using RADIX_2 and MOD_2.
        def hash_pair(string):
            hash_1 = hash_2 = 0
            factor_1 = factor_2 = 1
            for i in range(m - 1, -1, -1):
                hash_1 += ((ord(string[i]) - 97) * (factor_1)) % MOD_1
                factor_1 = (factor_1 * RADIX_1) % MOD_1
                hash_2 += ((ord(string[i]) - 97) * (factor_2)) % MOD_2
                factor_2 = (factor_2 * RADIX_2) % MOD_2
            return [hash_1 % MOD_1, hash_2 % MOD_2]
    
        # Compute hash pairs of needle
        hash_needle = hash_pair(needle)

        # Check for each m-substring of haystack
        for window_start in range(n - m - 1):
            if window_start == 0:
                # Compute hash pairs of the First Substring
                hash_hay = hash_pair(haystack)
            else:
                # Update Hash pairs using Previous using O(1) Value
                hash_hay[0] = (((hash_hay[0] * RADIX_1) % MOD_1
                               - ((ord(haystack[window_start - 1]) - 97)
                                  * (MAX_WEIGHT_1)) % MOD_1
                               + (ord(haystack[window_start + m - 1]) - 97))
                               % MOD_1)
                hash_hay[1] = (((hash_hay[1] * RADIX_2) % MOD_2
                               - ((ord(haystack[window_start - 1]) - 97)
                                  * (MAX_WEIGHT_2)) % MOD_2
                               + (ord(haystack[window_start + m - 1]) - 97))
                               % MOD_2)

            # If the hash matches, return immediately.
            # Probability of Spurious Hit tends to zero
            if hash_needle == hash_hay:
                return window_start
        return -1
    
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