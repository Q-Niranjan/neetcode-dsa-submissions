# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        tempHead = head

        while head:
            if not visited.get(head,False):
                visited[head] = True
            else:
                return True
            
            head = head.next
        
        return False
        