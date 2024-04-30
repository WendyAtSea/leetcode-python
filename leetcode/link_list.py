# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def arrayToList(cls, nums: List[int]):
        dummy_head = cls()
        cur = dummy_head
        for n in nums:
            node = cls(n)
            cur.next = node
            cur = node
        return dummy_head.next

    @staticmethod
    def toArray(head: Optional['ListNode']) -> List[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
    
    @staticmethod
    def toListWithCycle(nums: Optional[List[int]], pos: int):
        dummy_head = ListNode()
        tail = None
        cur = dummy_head
        for i in range(len(nums)):
            node = ListNode(nums[i])
            cur.next = node
            cur = node
            if i == pos:
                tail = cur
        cur.next = tail
        return dummy_head.next





class Solution:

    # 2. Add Two Numbers
    # More challenges:
    #   [M] 43. Multiply Strings
    #   [E] 67. Add Binary
    #   [M] 371. Sum of Two Integers
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur = dummy_head
        carry_over = 0
        while l1 or l2 or carry_over > 0:
            n = carry_over
            if l1:
                n += l1.val
                l1 = l1.next
            if l2:
                n += l2.val
                l2 = l2.next
            carry_over = n // 10
            next_node = ListNode(n % 10)
            cur.next = next_node
            cur = next_node
        return dummy_head.next
    
    # 141. Linked List Cycle
    # More challenges:
    #   [M] 3078. Match Alphanumerical Pattern in Matrix I
    #   [E] 2570. Merge Two 2D Arrays by Summing Values
    #   [M] 1124. Longest Well-Performing Interval
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False

        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    # 25. Reverse Nodes in K-Group
    # Runtime: O(n)
    # Space: O(1)
    # More challenges:
    #   [M] 1721. Swapping Nodes in a Linked List
    #   [M] 2074. Reverse Nodes in Even Length Groups
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: ListNode) -> List[ListNode]:
            prev = None
            tail = head
            while head.next:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            head.next = prev
            return head, tail

        # keep two pointers that are k step apart
        dummy_head = ListNode()
        cur = dummy_head
        first = head
        second = head
        while first:
            second = first
            i = 0
            tail = None
            while i < k and first:
                i += 1
                tail = first
                first = first.next
            # first is pointing to the kth node
            if i < k:
                cur.next = second
                break
            else:
                tail.next = None
                head, tail = reverse(second)
                cur.next = head
                cur = tail
        return dummy_head.next





if __name__ == '__main__':
    solution = Solution()
    for nums, k, expected_result in [
        ([1,2,3,4,5], 2, [2,1,4,3,5]),
    ]:
        head = ListNode.arrayToList(nums)
        head = solution.reverseKGroup(head, k)
        print(ListNode.toArray(head))