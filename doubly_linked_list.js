class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class Deque {
  constructor() {
    this.size = 0
    this.head = null
    this.tail = null
  } 

  pushRight(val) {
    const newNode = new Node(val)
    this.size++ 

    if (!this.head) {
      this.head = newNode
      this.tail = newNode
    } else {
      newNode.prev = this.tail
      this.tail.next = newNode
      this.tail = newNode
    }
  }

  pushLeft(val) {
    const newNode = new Node(val)
    this.size++

    if (!this.head) {
      this.head = newNode
      this.tail = newNode
    } else {
      newNode.next = this.head
      this.head.prev = newNode
      this.head = newNode
    }
  }

  popRight() {
    if (!this.head) {
      throw Error("Should not be empty")
    }
    if (this.head === this.tail) {
      this.head = null
      this.tail = null
    } else {
      const val = this.tail.val
      this.size--

      this.tail = this.tail.prev
      this.tail.next = null

      return val
    }
  }

  popLeft() {
    if (!this.head) {
      throw Error("Should not be empty")
    }
    if (this.head === this.tail) {
      this.head = null
      this.tial = null
    } else {
      const val = this.head.val
      this.size--

      this.head = this.head.next
      this.head.prev = null

      return val
    }
  }
}

const deque = new Deque()

// Test pushRight
deque.pushRight(1)
deque.pushRight(2)
deque.pushRight(3)
console.assert(deque.size === 3, "pushRight: size should be 3")
console.assert(deque.tail.val === 3, "pushRight: tail value should be 3")
console.assert(deque.head.val === 1, "pushRight: head value should be 1")

// Test popRight 
const rightVal = deque.popRight()
console.assert(rightVal === 3, "popRight: should return 3")
console.assert(deque.size === 2, "popRight: size should be 2")
console.assert(deque.tail.val === 2, "popRight: new tail should be 2")

// Test pushLeft
deque.pushLeft(0)
console.assert(deque.size === 3, "pushLeft: size should be 3") 
console.assert(deque.head.val === 0, "pushLeft: head value should be 0")

// Test popLeft
const leftVal = deque.popLeft()
console.assert(leftVal === 0, "popLeft: should return 0")
console.assert(deque.size === 2, "popLeft: size should be 2")
console.assert(deque.head.val === 1, "popLeft: new head should be 1")

console.log("\x1b[32m%s\x1b[0m", "All tests passed!")
