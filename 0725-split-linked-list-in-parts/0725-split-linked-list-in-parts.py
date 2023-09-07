# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list_length=0
        cur=head
        ans=[]
        
        while cur:
            list_length+=1
            cur=cur.next
        
        part_in_num=list_length//k
        part_mod=list_length%k
        
        cur=head
        for i in range(k):
            temp=cur
            for j in range(part_in_num+(i<part_mod)-1):
                if cur:
                    cur=cur.next
            if cur:
                cur.next,cur=None,cur.next
            ans.append(temp)
        return ans
        