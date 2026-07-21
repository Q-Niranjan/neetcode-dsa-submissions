# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        linkarray = []
        temp = head
        while temp:
            linkarray.append(temp.val)
            temp = temp.next

        l = 1
        r = len(linkarray)-1

        while l<r:
            head.next = ListNode(linkarray[r],None)
            head = head.next
            r -= 1

            head.next = ListNode(linkarray[l],None)
            head = head.next
            l +=1
        
        if l == r:
            head.next = ListNode(linkarray[l])

            


        


        
        
        