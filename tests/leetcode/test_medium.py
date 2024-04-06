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