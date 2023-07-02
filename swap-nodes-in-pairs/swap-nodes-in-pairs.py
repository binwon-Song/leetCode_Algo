# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head.next:
#             return head
#         head.val,head.next.val=head.next.val,head.val
#         print(head)
#         if head.next.next:
#             self.swapPairs(head.next.next)
        
#         return head
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: 노드가 없거나 마지막 노드인 경우
        if not head or not head.next:
            return head
        
        # 두 노드의 값 교환
        head.val, head.next.val = head.next.val, head.val
        
        # 재귀적으로 다음 두 노드 호출
        self.swapPairs(head.next.next)
        print(head)
        return head
