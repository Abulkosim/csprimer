class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        
        while current: 
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
            
        return prev
    