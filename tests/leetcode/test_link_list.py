from typing import List, Optional
import pytest

from leetcode.link_list import ListNode, Solution

@pytest.fixture
def solution():
    return Solution()


# 2. Add Two Numbers
@pytest.mark.parametrize("nums1, nums2, expected_result", [
    ([2,4,3], [5,6,4], [7,0,8]),
    ([0], [0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])
])
def test_merge(solution: Solution, nums1: List[int], nums2: List[int], expected_result: List[int]):
    l1 = ListNode.arrayToList(nums1)
    l2 = ListNode.arrayToList(nums2)
    l = solution.addTwoNumbers(l1, l2) 
    assert ListNode.toArray(l) == expected_result

# 141. Linked List Cycle
@pytest.mark.parametrize("nums1, pos, expected_result", [
    ([3,2,0,-4], 1, True),
    ([1,2], 0, True),
    ([1], -1, False)
])
def test_hasCycle(solution: Solution, nums1: List[int], pos: int, expected_result: List[int]):
    head = ListNode.toListWithCycle(nums1, pos)
    assert solution.hasCycle(head) == expected_result

# 25. Reverse Nodes in K-Group
@pytest.mark.parametrize("nums, k, expected_result", [
    ([1,2,3,4,5], 3, [3,2,1,4,5]),
    ([1,2,3,4,5], 2, [2,1,4,3,5])
])
def test_reverseKGroup(solution: Solution, nums: Optional[List[int]], k: int, expected_result: Optional[List[int]]):
    head = ListNode.arrayToList(nums)
    head = solution.reverseKGroup(head, k) 
    assert ListNode.toArray(head) == expected_result