class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Deque(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push_right(self, val):
        new_node = Node(val)
        self.size += 1
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_right(self):
        if not self.tail:
            raise IndexError("Cannot pop from empty deque")
        else:
            val = self.tail.val
            self.size -= 1

            if self.head == self.tail:
                self.head = None
                self.tail = None

            else:
                self.tail = self.tail.prev
                self.tail.next = None

            return val

    def push_left(self, val):
        new_node = Node(val)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_left(self):
        if not self.head:
            raise IndexError("Cannot pop from empty deque")
        else:
            val = self.head.val
            self.size -= 1

            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

            return val
