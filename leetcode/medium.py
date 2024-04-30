from collections import Counter
from typing import List, Set

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
    # Space: O(1)
    # More challenges:
    #   [M] 186. Reverse Words in a String II
    #   [M] 2607. Make K-Subarray Sums Equal
    def rotate(self, nums: List[int], k: int) -> None:
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

    # 15. 3Sum
    # Runtime: O(nLog(n) + n*n)
    # Space: O(n)
    # More challenges:
    #   [E] 653. Two Sum IV - Input is a BST
    #   [M] 16. 3Sum Closest
    #   [M] 18. 4Sum
    #   [E] 2367. Number of Arithmetic Triplets
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
    
        def twoSums(cur_index: int):
            left, right = cur_index + 1, len(sorted_nums) - 1
            while left < right:
                val = sorted_nums[cur_index] + sorted_nums[left] + sorted_nums[right]
                if val == 0:
                    result.append([sorted_nums[cur_index], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicated values
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                elif val < 0:
                    left += 1
                else:
                    right -= 1
       
        for i in range(len(sorted_nums)):
            if sorted_nums[i] > 0: break
            if i == 0 or sorted_nums[i] != sorted_nums[i-1]:
                twoSums(i)
        return result

    # 16. 3Sum Closest
    # Runtime: O(n*n + nLog(n))
    # Space: O(n)
    # More challenges
    #  [H] 548. Split Array with Equal Sum
    #  [M] 1861. Rotating the Box
    #  [M] 1498. Number of Subsequences That Satisfy the Given Sum Condition
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        result = sum(sorted_nums[:3])
        min_diff = abs(target - result)
        for i in range(len(sorted_nums)):
            left, right = i + 1, len(sorted_nums) - 1
            while left < right:
                val = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if abs(target - val) < min_diff:
                    result = val
                    min_diff = abs(target - val)
                
                if min_diff == 0:
                    return result
                elif val > target:
                    right -= 1
                else:
                    left += 1
        return result
    
    # 259. 3Sum Smaller
    # Runtime: O(n*n + nLog(n))
    # Space: O(Log(n))
    # More challenges:
    #   [M] 611. Valid Triangle Number
    #   [M] 2592. Maximize Greatness of an Array
    #   [M] 2971. Find Polygon With the Largest Perimeter

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return 0

        sorted_nums = sorted(nums)
        result = 0
        for i in range(len(sorted_nums)): 
            left, right = i + 1, len(sorted_nums) - 1
            while left < right:
                val = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if val < target:
                    result += right - left # all the combinations in between
                    left += 1
                else:
                    right -= 1
        return result

    # 209. Minimum Size Subarray Sum
    # Runtime: O(n) 2*n each node is visited at most twice
    # Space: O(1)
    # More challenges:
    #   [M] 325. Maximum Size Subarray Sum Equals k
    #   [M] 718. Maximum Length of Repeated Subarray
    #   [M] 1658. Minimum Operations to Reduce X to Zero
    def minSubArrayLenTwoPointers(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1 # initialize 
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0

    # 3. Longest Substring Without Repeating Characters
    # Runtime: O(n)
    # Space: O(m) m is the unique number of chars
    # More challenges:
    #   [M] 159. Longest Substring with At Most Two Distinct Characters
    #   [M] 340. Longest Substring with At Most K Distinct Characters
    #   [H] 992. Subarrays with K Different Integers
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        seen = {}  # store char and its latest index
        for right in range(len(s)):
            key = s[right]
            if key in seen:
                left = max(seen[key], left)

            result = max(result, right - left + 1)
            seen[key] = right + 1  # start index without curent char
        return result
    
    # 567. Permutation in String
    # Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
    # or false otherwise. In other words, return true if one of s1's permutations 
    # is the substring of s2.
    # Constraints: s1 and s2 consist of lowercase English letters.
    # Note: could use a = [0] * 26 [ord(s1[i]) - ord('a')] to keep track of chars
    # Runtime: O(len(s2) + 26 * (len(s2) - len(s1)))
    # Space: O(1)
    # More challenges:
    #   [M] 438. Find All Anagrams in a String
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0 or len(s2) == 0 or len(s1) > len(s2): return False

        if len(s1) > len(s2): return False

        s1Map = Counter(s1)
        s2Map = Counter(s2[:len(s1)])

        def isEqual(s1Map: Counter, s2Map: Counter): 
            if len(s1Map) != len(s2Map): return False
            for key, val in s1Map.items():
                if s2Map.get(key, 0) != val:
                    return False
            return True

        for i in range(len(s2) - len(s1)):
            if isEqual(s1Map, s2Map): return True

            key = s2[i]
            if s2Map[key] == 1:
                del s2Map[key]
            else:   
                s2Map[key] = s2Map[key] - 1
            
            key = s2[i + len(s1)]
            s2Map[key] = s2Map.get(key, 0) + 1

        return isEqual(s1Map, s2Map)


    # 291. Word Pattern II
    # Runtime: O(len(pattern) * len(s))
    # Space: 
    # More challenges:
    #   [M] 1676. Lowest Common Ancestor of a Binary Tree IV
    #   [M] 2397. Maximum Rows Covered by Columns
    #   [H] 2953. Count Complete Substrings
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def isMatch(pIndex: int, sIndex: int, psMap: dict, seen: set) -> bool:
            # reach the end of the pattern
            if pIndex == len(pattern):
                return sIndex == len(s)
            
            if len(pattern) - pIndex > len(s) - sIndex: 
                # not enough letters to match the pattern
                return False
            
            # found the pattern
            if pattern[pIndex] in psMap:
                word = psMap[pattern[pIndex]]
                if len(word) > len(s) - sIndex or word != s[sIndex:sIndex + len(word)]:
                    return False
                else:
                    return isMatch(pIndex + 1, sIndex + len(word), psMap, seen)
            
            # the pattern is new and try each substring
            for i in range(1, len(s) - sIndex + 1):
                cur = s[sIndex:sIndex + i]
                if cur in seen: 
                    continue

                # save current pattern and substring
                psMap[pattern[pIndex]] = cur
                seen.add(cur)
                if isMatch(pIndex + 1, sIndex + i, psMap, seen):
                    return True
                
                # remove the current pattern and substring and retry
                psMap.pop(pattern[pIndex])
                seen.remove(cur)

            return False

        psMap = {}
        seen = set()
        return isMatch(0, 0, psMap, seen)

    # 128. Longest Consecutive Sequence
    # Runtime: O(n)
    # Space: O(n)
    # More challenges:
    #   [M] 298. Binary Tree Longest Consecutive Sequence
    #   [M] 2177. Find Three Consecutive Integers That Sum to a Given Number
    #   [M] 2274. Maximum Consecutive Floors Without Special Floors
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        numSet = set(nums) 
        seen = set()
        result = 1
        for n in nums:
            if n - 1 in numSet or n in seen: 
                # find the smallest number in the sequence
                continue

            seen.add(n)
            # count up from the smallest to the largest
            cur = 1
            while n + 1 in numSet:
                cur += 1
                n += 1
            result = max(result, cur)
        
        return result

    # 2177. Find Three Consecutive Integers That Sum to a Given Number
    # Runtime: O(log(n))
    # Space: O(1)
    # More challenges:
    #   [M] 2240. Number of Ways to Buy Pens and Pencils
    def sumOfThree(self, num: int) -> List[int]:
        # num = (n - 1) + n + (n + 1) = 3 * n
        # n = num // 3
        # m = num % 3
        # if m == 0: return [n - 1, n, n + 1]
        # if m % 3 != 0: return []
        left = 0
        right = num - 1
        while left <= right:
            mid = left + (left + right) // 2
            total = mid * 3
            if total == num:
                return [mid - 1, mid, mid + 1]
            elif total > num:
                right -= 1
            else:
                left += 1
        return []

    # 2655. Find Maximal Uncovered Ranges
    # Runtime: m = ranges.length O(mLog(m)) + O(m)
    # Space: 
    # More challenges:
    #   [E] 1893. Check if All the Integers in a Range Are Covered
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        if len(ranges) == 0:
            return [[0, n]]

        # sort the ranges by the lowest boundary
        sorted_ranges = sorted(ranges, key = lambda item: item[0])
        
        lo, hi = sorted_ranges[0]
        result = []
        if lo > 0:
            result.append([0, lo - 1])
        
        for i in range(1, len(sorted_ranges)):
            cur_lo, cur_hi = sorted_ranges[i]

            # Case 1: current range is inside of (lo, hi)
            if cur_lo >= lo and cur_hi <= hi:
                continue

            # Case 2: current range is > (lo, hi)
            elif cur_lo > hi:
                if hi + 1 == cur_lo:
                    # they are connected
                    hi = cur_hi
                else:
                    # no overlap
                    result.append([hi + 1, cur_lo - 1])
                    lo, hi = cur_lo, cur_hi

            # Case 3: current range is overlap with (lo, hi)
            else: 
                hi = cur_hi

        if hi+1 < n:
            result.append([hi + 1, n - 1])
        return result

    # 57. Insert Interval
    # Runtime: O(intervals.length)
    # Space: O(n)
    # More challenges:
    #   [H] 715. Range Module
    #   [H] 2276. Count Integers in Intervals
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        if len(intervals) == 0: 
            result.append(newInterval)
            return result
        
        i = 0
        newStart, newEnd = newInterval
        while i < len(intervals):
            start, end = intervals[i]

            # (start, end) > new interval
            if newEnd < start:
                break

            i += 1

            # (start, end) < new interval
            if newStart > end:
                result.append([start, end])
                continue

            # (start, end) is fully overlapped 
            if start >= newStart and end <= newEnd:
                continue

            # (start, end) is partially overlapped
            if start <= newStart:
                newStart = start
            if end >= newEnd:
                newEnd = end

        # insert the new interval
        result.append([newStart, newEnd])

        # (start, end) > new interval
        while i < len(intervals): 
            result.append(intervals[i])
            i += 1

        return result

    # 150. Evaluate Reverse Polish Notation
    # Runtime: O(n) n = tokens.length
    # Space: O(n)
    # More challenges:
    #   [H] 282. Expression Add Operators
    def evalRPN(self, tokens: List[str]) -> int:
        def cal(tokens: List[str]) -> int:
            val = tokens.pop()
            if val == '+':
                right = cal(tokens) 
                left = cal(tokens)
                return left + right
            elif val == '-':
                right = cal(tokens) 
                left = cal(tokens)
                return left - right
            elif val == '*':
                right = cal(tokens) 
                left = cal(tokens)
                return left * right
            elif val == '/':
                right = cal(tokens)
                left = cal(tokens)
                # The division between two integers always truncates toward zero.
                return int(left / right)
            else:
                return int(val)
        
        return cal(tokens)

    # # 442. Find All Duplicates in an array
    # You must write an algorithm that runs in O(n) time and uses only constant extra space.
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    #   2615. Sum of Distances
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            i = abs(n) - 1
            if nums[i] < 0:
                result.append(i + 1)
            nums[i] *= -1
        return result

    # 245. Shortest Word Distance III
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    #   [E] 243. Shortes Word Distance
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        result = len(wordsDict) + 1
        prevIndex = -1
        for i in range(len(wordsDict)):
            curWord = wordsDict[i]
            if curWord != word1 and curWord != word2: continue

            if prevIndex != -1 and (curWord != wordsDict[prevIndex] or word1 == word2):
                result = min(result, i - prevIndex)
            
            prevIndex = i

        return result

    # 2411. Smallest Subarrays With Maximum Bitwise OR
    # Runtime:
    # Space:
    # More challenges:
    #
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # TODO
        pass





if __name__ == '__main__':
    obj = SolutionMedium()
    print(obj.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))
    #print(obj.evalRPN(["4","-2","/","2","-3","-","-"]))
    #print(obj.insert([[1,2],[5,7]], [3,4]))  # [[1,7]]
    #print(obj.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    #print(obj.threeSum([-2,0,1,1,2]))
    #print(obj.threeSumSmaller([-1,1,-1,-1], -1))
    #print(obj.minSubArrayLenTwoPointers(7, [2,3,1,2,4,3]))
    #print(obj.lengthOfLongestSubstring("abcbaefg"))
    #print(obj.checkInclusion("ab", "aob")) #abcdxabcde", "abcdeabcdx"))
    #print(obj.wordPatternMatch("p", "s")) #"aaaa", "asdasdasdasd"))
    #print(obj.longestConsecutive([1, 100,4,200,1,3,2]))
    #print(obj.sumOfThree(33))
    #print(obj.findMaximalUncoveredRanges(10, [[3,5],[7,8]]))