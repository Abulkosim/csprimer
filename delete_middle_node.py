class Solution(object):
    def deleteMiddle(self, head):
        temp_cur, cur = head, head
        length, idx, prev = 0, 0, None

        while temp_cur:
            temp_cur = temp_cur.next
            length += 1

        if length < 2:
            return None

        while cur:
            if idx == int(length / 2) and prev:
                next_temp = cur.next
                cur.next = None
                prev.next = next_temp

                return head

            prev = cur
            cur = cur.next
            idx += 1

            def deleteMiddle(self, head):
                if not head or not head.next:
                    return None

                slow = fast = head
                prev = None

                while fast and fast.next:
                    fast = fast.next.next
                    prev = slow
                    slow = slow.next

                prev.next = slow.next

                return head
