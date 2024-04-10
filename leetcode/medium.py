from typing import List

'''
Practice following questions
55. Jump Game
2417. Closest Fair Integer
'''

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
    
    # 12. Integer to Roman
    #   constraints: 1 <= num <= 3999
    # Runtime: O(1)
    # Space: O(1)
    # More challenges:
    #   [H] 273. Integer to English Words
    def intToRoman(self, num: int) -> str:
        result = ''
        n_to_roman = [
            (1000, 'M'),
            (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
            (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        result = []
        for n, roman in n_to_roman:
            if n > num: continue
            d, num = divmod(num, n)
            result.append(roman * d)
        return ''.join(result)
    

    # 151. Reverse Words in a String
    # Runtime: O(n)
    # Space: O(n)
    # More challenges:
    #   [M] 186. Reverse Words in a String II
    def reverseWords(self, s: str) -> str:
        result = []
        end_index = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i].isspace():
                if end_index != -1:
                    result.append(s[i+1:end_index+1])
                end_index = -1
            elif end_index == -1:
                end_index = i
        if end_index != -1:
            result.append(s[:end_index+1])
        return ' '.join(result)

    # 6. Zigzag Conversion
    # Runtime: O(numRows * len(s))
    # Space: O(len(s))
    # More challenges:
    #   [E] 1624. Largest Substring Between Two Equal Characters
    #   [M] 842. Split Array into Fibonacci Sequence
    #   [H] 828. Count Unique Characters of All Substrings of a Given String
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        rows = []
        for _ in range(numRows): rows.append([])
        row_index = 0
        for i in range(len(s)):
            if row_index == 0:
                step_index = 1
            elif row_index == numRows - 1:
                step_index = -1
            rows[row_index].append(s[i])
            row_index += step_index
        result = []
        for i in range(numRows): result.append(''.join(rows[i]))
        return ''.join(result)
            

    # 274. H-Index
    # Runtime: O(nLog(n)) sorted
    # Space: O(1)
    # More challenges:
    #   [M] 275. H-Index II
    def hIndex(self, citations: List[int]) -> int:
        # The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
        h_index = 0
        sorted_citations = sorted(citations)
        n = len(citations)
        for i in range(n):
            val = sorted_citations[i]
            if val == 0: continue
            if val >= n - i:
                h_index = max(h_index, n - i)
            elif val > h_index:
                h_index = val
        return h_index
    
    # 238. Product of Array Except Self
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    #   [H] 42. Trapping Rain Water
    #   [H] 265. Paint House II
    #   [H] 2163. Minimum Difference in Sums After Removal of Elements
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []

        result = [0] * len(nums) 

        # product of left to right
        result[0] = 1 
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        # product of right to left
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= r
            r *= nums[i]
        
        return result

    # 134. Gas Station
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    #   [M] 2202. Maximize the Topmost Element After K Moves
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        cur_gain = 0
        result = 0
        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            cur_gain += gas[i] - cost[i]
            if cur_gain < 0:
                cur_gain = 0
                result = i + 1
        return result if total_gain >= 0 else -1




if __name__ == '__main__':
    obj = SolutionMedium()
    print(obj.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))