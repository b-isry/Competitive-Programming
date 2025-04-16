# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head
        i = 0
        while curr and i < index - 1:
            curr = curr.next
            i += 1

        if not curr:
            return  # index out of bounds

        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            return

        curr = self.head
        i = 0
        while curr and curr.next:
            if i == index - 1:
                curr.next = curr.next.next
                return
            curr = curr.next
            i += 1
