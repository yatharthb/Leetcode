# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head
        ch = head
        bl = ch
        hed = head
        tl = head
        ll = 1
        while tl.next:
            ll+=1
            tl = tl.next
        #print(ll)
        n = 0
        if k%ll == 0:
            return head
        while n < ll-(k%ll):
            n += 1
            
            if hed.next:
               hed = hed.next
               
               if n < ll-(k%ll):
                  ch = ch.next
            else:
                hed = head
                ch = head
            
        ch.next = None
        hd = hed
        #print(hed)

        while hed.next:
           hed = hed.next
        if hd != bl:
           hed.next = bl
        
        #print(hd)
        return hd