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

# 189. Rotate Array
@pytest.mark.parametrize("nums, k, expected_nums", [
    ([1,2], 1, [2,1]),
    ([-1,-100,3,99], 2, [3,99,-1,-100]),
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    ([1,2], 3, [2,1]),
    ([1,2], 4, [1,2])
])
def test_rotate_space_saver(medium_class_obj: SolutionMedium, nums: list[int], k: int, expected_nums: list[int]):
    medium_class_obj.rotate_space_saver(nums, k)
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
    