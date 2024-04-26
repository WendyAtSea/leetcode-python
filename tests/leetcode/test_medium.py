from typing import Literal
import pytest

from leetcode.medium import SolutionMedium

@pytest.fixture
def medium_class_obj():
    return SolutionMedium()

# 80. Remove Duplicates from Sorted Array II
@pytest.mark.parametrize("nums, expected_k, expected_nums", [
    ([1,1,1,2,2,3], 5, [1,1,2,2,3]),
    ([0,0,1,1,1,1,2,3,3], 7, [0,0,1,1,2,3,3])
])
def test_removeDuplicates(medium_class_obj: SolutionMedium, nums: list[int], expected_k: int, expected_nums: list[int]):
    assert medium_class_obj.removeDuplicates(nums), expected_k
    assert nums[:expected_k] == expected_nums

# 189. Rotate Array
@pytest.mark.parametrize("nums, k, expected_nums", [
    ([1,2], 1, [2,1]),
    ([-1,-100,3,99], 2, [3,99,-1,-100]),
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    ([1,2], 3, [2,1]),
    ([1,2], 4, [1,2])
])
def test_rotate(medium_class_obj: SolutionMedium, nums: list[int], k: int, expected_nums: list[int]):
    medium_class_obj.rotate(nums, k)
    assert nums == expected_nums

# 122. Best Time to Buy and Sell Stock II
@pytest.mark.parametrize("prices, expected_profit", [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0)
])
def test_maxProfit(medium_class_obj: SolutionMedium, prices: list[int], expected_profit: int):
    assert medium_class_obj.maxProfit(prices) == expected_profit

# 12. Integer to Roman
@pytest.mark.parametrize("num, expected_result", [
    (3, "III"),
    (4, "IV"),
    (9, 'IX'),
    (40, 'XL'),
    (90, 'XC'),
    (400, 'CD'),
    (601, 'DCI'),
    (622, 'DCXXII'),
    (900, 'CM'),
    (58, "LVIII"),
    (60, 'LX'),
    (62, 'LXII'),
    (1994, "MCMXCIV"),
    (3999, "MMMCMXCIX")
])
def test_intToRaman(medium_class_obj: SolutionMedium, num: int, expected_result: str):
    assert medium_class_obj.intToRoman(num) == expected_result

# 151. Reverse Words in a String
@pytest.mark.parametrize("s, expected_result", [
    ("the sky is blue", "blue is sky the"),
    ('  hello world  ', 'world hello'),
    ('a good   example', 'example good a'),
    ('abc', 'abc')
])
def test_reverseWords(medium_class_obj: SolutionMedium, s: str, expected_result: str):
    assert medium_class_obj.reverseWords(s) == expected_result

# 6. Zigzag Conversion
@pytest.mark.parametrize("s, numRows, expected_result", [
    ('AB', 1, 'AB'),
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A")
])
def test_convert(medium_class_obj: SolutionMedium, s: str, numRows: int, expected_result: str):
    assert medium_class_obj.convert(s, numRows) == expected_result

# 274. H-Index
@pytest.mark.parametrize("citations, expected_result", [
    ([3,0,6,1,5], 3),
    ([1,3,1], 1),
    ([100], 1),
    ([2,0,3], 2),
    ([1, 200], 1),
    ([2,1,100], 2)
])
def test_convert(medium_class_obj: SolutionMedium, citations: list[int], expected_result: str):
    assert medium_class_obj.hIndex(citations) == expected_result
    

# 238. Product of Array Except Self
@pytest.mark.parametrize("nums, expected_result", [
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0])
])
def test_productExceptSelf(medium_class_obj: SolutionMedium, nums: list[int], expected_result: list[int]):
    assert medium_class_obj.productExceptSelf(nums) == expected_result

# 134. Gas Station
@pytest.mark.parametrize("gas, cost, expected_result", [
    ([1,2,3,4,5], [3,4,5,1,2], 3),
    ([2,3,4], [3,4,3], -1)
])
def test_canCompleteCircuit(medium_class_obj: SolutionMedium, gas: list[int], cost: list[int], expected_result: list[int]):
    assert medium_class_obj.canCompleteCircuit(gas, cost) == expected_result
    
# 15. 3Sum
@pytest.mark.parametrize("nums, expected_result", [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([-2,0,1,1,2], [[-2,0,2],[-2,1,1]]),
    ([0,1,1], []),
    ([0,0,0,0,0], [[0,0,0]])
])
def test_threeSum(medium_class_obj: SolutionMedium, nums: list[int], expected_result: list[list[int]]):
    assert medium_class_obj.threeSum(nums) == expected_result

# 16. 3Sum Closest
@pytest.mark.parametrize("nums, target, expected_result", [
    ([1,1,1,0], 100, 3),
])
def test_threeSumCloset(medium_class_obj: SolutionMedium, nums: list[int], target: int, expected_result: int):
    assert medium_class_obj.threeSumClosest(nums, target) == expected_result

# 16. 3Sum Smaller
@pytest.mark.parametrize("nums, target, expected_result", [
    ([-2,0,1,3], 2, 2), # [-2,0,1], [-2, 0, 3]
    ([], 0, 0),
    ([0], 0, 0),
    ([3,1,0,-2], 4, 3),
    ([-1, 1, -1, -1], -1, 1)
])
def test_threeSumSmaller(medium_class_obj: SolutionMedium, nums: list[int], target: int, expected_result: int):
    assert medium_class_obj.threeSumSmaller(nums, target) == expected_result

# 209. Minimum Size Subarray Sum
@pytest.mark.parametrize("target, nums, expected_result", [
    (7, [2,3,1,2,4,3], 2),
    (4, [1,4,1], 1),
    (11, [1,1,1], 0)
])
def test_minSubArrayLenTwoPointers(medium_class_obj: SolutionMedium, target: int, nums: list[int], expected_result: int):
    assert medium_class_obj.minSubArrayLenTwoPointers(target, nums) == expected_result 

# 3. Longest Substring Without Repeating Characters
@pytest.mark.parametrize("s, expected_result", [
    ("abcabcbb", 3),
    ("aaaa", 1),
    ("abcbaefg", 6)
])
def test_lengthOfLongestSubstring(medium_class_obj: SolutionMedium, s: str, expected_result: int):
    assert medium_class_obj.lengthOfLongestSubstring(s) == expected_result

# 567. Permutation in String
@pytest.mark.parametrize("s1, s2, expected_result", [
    ("ab", "eidbaooo", True),
    ('ab', 'eidboaoo', False),
    ('adc', 'dcda', True),
    ('abcdxabcde', 'abcdeabcdx', True)
])
def test_checkInclusion(medium_class_obj: SolutionMedium, s1: str, s2: str, expected_result: bool):
    assert medium_class_obj.checkInclusion(s1,s2) == expected_result

# 291. Word Pattern II
@pytest.mark.parametrize("pattern, s, expected_result", [
    ("abab", "redblueredblue", True),
    ("aaaa", "asdasdasdasd", True),
    ("aabb", "xyzabcxzyabc", False),
    ("p", "a", True)
])
def test_wordPatternMatch(medium_class_obj: SolutionMedium, pattern: str, s: str, expected_result: bool):
    assert medium_class_obj.wordPatternMatch(pattern, s) == expected_result

# 128. Longest Consecutive Sequence
@pytest.mark.parametrize("nums, expected_result", [
    ([100,4,200,1,3,2], 4),
    ([0,3,7,2,5,8,4,6,0,1], 9)
])
def test_longestConsecutive(medium_class_obj: SolutionMedium, nums: list[int], expected_result: int):
    assert medium_class_obj.longestConsecutive(nums) == expected_result

# 2177. Find Three Consecutive Integers That Sum to a Given Number
@pytest.mark.parametrize("num, expected_result", [
    (33, [10,11,12]),
    (4, [])
])
def test_sumOfThree(medium_class_obj: SolutionMedium, num: int, expected_result: list[int]):
    assert medium_class_obj.sumOfThree(num) == expected_result

# 2655. Find Maximal Uncovered Ranges
@pytest.mark.parametrize("n, ranges, expected_result", [
    (10, [[3,5],[7,8]], [[0,2],[6,6],[9,9]]),
    (3, [[0,2]], []),
    (7, [[2,4],[0,3]], [[5,6]]),
    (11, [(0,1), (2,5), (3,4), (0,8), (7, 10)], [])
])
def test_findMaximalUncoveredRanges(medium_class_obj: SolutionMedium, n: int, ranges: list[list[int]], expected_result: list[list[int]]):
    assert medium_class_obj.findMaximalUncoveredRanges(n, ranges) == expected_result

# 57. Insert Interval
@pytest.mark.parametrize("intervals, newInterval, expected_result", [
    ([[1,5]], [0,0], [[0,0], [1,5]]),
    ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
    ([[1,2],[5,7]], [3,4], [[1,2],[3,4],[5,7]]),
    ([[1,3],[5,7]], [3,4], [[1,4],[5,7]]),
    ([[1,3],[5,7]], [3,6], [[1,7]]),
    ([[1,2],[5,6]], [3,4], [[1,2],[3,4],[5,6]])
])
def test_insert(medium_class_obj: SolutionMedium, intervals: list[list[int]], newInterval: list[int], expected_result: list[list[int]]):
    assert medium_class_obj.insert(intervals, newInterval) == expected_result

# 150. Evaluate Reverse Polish Notation
@pytest.mark.parametrize("tokens, expected_result", [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
    (["4","-2","/","2","-3","-","-"], -7)
])
def test_evalRPN(medium_class_obj: SolutionMedium, tokens: list[str], expected_result: int):
    assert medium_class_obj.evalRPN(tokens) == expected_result

# 442. Find All Duplicates in an array
@pytest.mark.parametrize("nums, expected_result", [
    ([4,3,2,7,8,2,3,1], [2,3]),
    ([1], []),
    ([1,1], [1])
])
def test_findDuplicates(medium_class_obj: SolutionMedium, nums: list[int], expected_result: list[int]):
    assert medium_class_obj.findDuplicates(nums) == expected_result