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
def test_removeDuplicates(easy_class_obj: SolutionEasy, nums: list[int], expected_k: Literal[0] | Literal[1] | Literal[2] | Literal[5], expected_nums: list[int]):
    assert easy_class_obj.removeDuplicates(nums) == expected_k
    assert nums[0:expected_k] == expected_nums

# 28. Find the Index of the First Occurrence in a String
@pytest.mark.parametrize("haystack, needle, expected_result", [
    (['sadbutsad', 'sad', 0]),
    (['leetcode', 'leeto', -1])
])
def test_strStr(easy_class_obj: SolutionEasy, haystack: list[str | int], needle: list[str | int], expected_result: list[str | int]):
    assert easy_class_obj.strStr(haystack, needle) == expected_result

# 1893. Check if All the Integers in a Range Are Covered
@pytest.mark.parametrize("ranges, left, right, expected_result", [
    ([[37,49],[5,17],[8,32]], 29, 49, False),
    ([[1,2], [3,5]], 2, 4, True),
    ([[1,2], [4,5], [7,8]], 3, 6, False),
    ([[1,2], [5,7], [0,3], [5,9], [9, 10]], 3, 7, False),
    ([[0,2], [4,5], [8,10]], 1, 9, False),
    ([[0,2], [4,5], [8,10], [4,7]], 1, 9, False),
    ([[0,2], [3,4], [4,6], [7,8], [9,11]], 1, 9, True)
])
def test_isCovered(easy_class_obj: SolutionEasy, ranges: list[list[int]], left: int, right: int, expected_result: bool):
    assert easy_class_obj.isCovered(ranges, left, right) == expected_result
        
# 455. Assign Cookies
@pytest.mark.parametrize("g, s, expected_result", [
    ([3,2], [1,1,1], 0),
    ([1,2,3], [3], 1),
    ([1,2,3], [1,1], 1),
    ([1,1], [1,2,3], 2),
    ([1,2,3], [2,2], 2),
    ([262,437,433,102,438,346,131,160,281,34,219,373,466,275,51,118,209,32,108,57,385,514,439,73,271,442,366,515,284,425,491,466,322,34,484,231,450,355,106,279,496,312,96,461,446,422,143,98,444,461,142,234,416,45,271,344,446,364,216,16,431,370,120,463,377,106,113,406,406,481,304,41,2,174,81,220,158,104,119,95,479,323,145,205,218,482,345,324,253,368,214,379,343,375,134,145,268,56,206],
     [149,79,388,251,417,82,233,377,95,309,418,400,501,349,348,400,461,495,104,330,155,483,334,436,512,232,511,40,343,334,307,56,164,276,399,337,59,440,3,458,417,291,354,419,516,4,370,106,469,254,274,163,345,513,130,292,330,198,142,95,18,295,126,131,339,171,347,199,244,428,383,43,315,353,91,289,466,178,425,112,420,85,159,360,241,300,295,285,310,76,69,297,155,416,333,416,226,262,63,445,77,151,368,406,171,13,198,30,446,142,329,245,505,238,352,113,485,296,337,507,91,437,366,511,414,46,78,399,283,106,202,494,380,479,522,479,438,21,130,293,422,440,71,321,446,358,39,447,427,6,33,429,324,76,396,444,519,159,45,403,243,251,373,251,23,140,7,356,194,499,276,251,311,10,147,30,276,430,151,519,36,354,162,451,524,312,447,77,170,428,23,283,249,466,39,58,424,68,481,2,173,179,382,334,430,84,151,293,95,522,358,505,63,524,143,119,325,401,6,361,284,418,169,256,221,330,23,72,185,376,515,84,319,27,66,497],
     99)
])
def test_findContentChildren(easy_class_obj: SolutionEasy, 
                             g: list[int], 
                             s: list[int], 
                             expected_result: int):
    assert easy_class_obj.findContentChildren(g, s) == expected_result

# 448. Find All Numbers Disappeared in an Array
@pytest.mark.parametrize("nums, expected_result", [
    ([4,3,2,7,8,2,3,1], [5,6]),
    ([1,1], [2]),
    ([1,2], []),
    ([3,3,3,3], [1,2,4])
])
def test_findDisappearedNumbers(easy_class_obj: SolutionEasy, nums: list[int], expected_result: list[int]):
    easy_class_obj.findDisappearedNumbers(nums) == expected_result