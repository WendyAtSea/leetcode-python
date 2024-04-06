from typing import Literal
import pytest

from leetcode.easy import SolutionEasy

@pytest.fixture
def easy_class_obj():
    return SolutionEasy()

# 88. Merge Sorted Array
@pytest.mark.parametrize("nums1, m, nums2, n, expected_result", [
    ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
    ([1,2,3,0,0,0], 3, [4,5,6], 3, [1,2,3,4,5,6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1])
])
def test_merge(easy_class_obj: SolutionEasy, nums1: list[int], m: Literal[3] | Literal[1] | Literal[0], nums2: list[int], n: Literal[3] | Literal[0] | Literal[1], expected_result: list[int]):
    easy_class_obj.merge(nums1, m, nums2, n) 
    assert nums1 == expected_result

# 27. Remove Element
@pytest.mark.parametrize("nums, val, expected_k, expected_nums", [
    ([0,1,2,2,3,0,4,2], 2, 5, [0,1,4,0,3]),
    ([1,2,2], 2, 1, [1]),
    ([2,2,2], 2, 0, [])
])
def test_removeElement(easy_class_obj: SolutionEasy, nums: list[int], val: int, expected_k: int, expected_nums: list[int]):
    assert easy_class_obj.removeElement(nums, val) == expected_k
    assert nums[0:expected_k] == expected_nums

# 26. Remove Duplicates from Sorted Array
@pytest.mark.parametrize("nums, expected_k, expected_nums", [
    ([], 0, []),
    ([1], 1, [1]),
    ([1,1,2], 2, [1,2]),
    ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4])
])
def test_removeDuplicates(easy_class_obj, nums, expected_k, expected_nums):
    assert easy_class_obj.removeDuplicates(nums) == expected_k
    assert nums[0:expected_k] == expected_nums