#!/usr/bin/env python3


class LinkedListNode:


    def __init__(self, data):
        self.next:LinkedListNode|None = None
        self.prev:LinkedListNode|None = None
        self.data = data

    '''
    def __str__(self) -> str:
        return f"{self.data = } ^^^ type: {type(self.data)}"


    def __repr__(self) -> str:
        return f"{self.data = } *** type: {type(self.data)}"
    '''


class LinkedList:
    def __init__(self, head:LinkedListNode|None):
        self.head:LinkedListNode|None = head
        self.tail:LinkedListNode|None = head

        if head is not None:
            self.node_count:int = 1
        else:
            self.node_count:int = 0


    def __str__(self) -> str:
        return f"{self.node_count = }"


    def get(self, index:int) -> LinkedListNode:
        if index < 0:
            raise IndexError(f"Index needs to be >= 0")

        if index > self.node_count:
            raise IndexError(f"Attempting to get an element at index[{index}] > node_count[{self.node_count}]")

        if self.head is None:
            raise IndexError(f"linklist is empty!")

        counter:int = 0
        node:LinkedListNode|None = self.head

        while counter < index:
            node = node.next
            if node is None:
                break

            counter += 1

        if node is None:
            raise IndexError(f"Attempting to get an element at index[{index}] > node_count[{self.node_count}]")

        return node


    def get_reverse(self, index:int) -> LinkedListNode:
        if index < 0:
            raise IndexError(f"Index needs to be >= 0")

        if index > self.node_count:
            raise IndexError(f"Attempting to get an element at index[{self.node_count - index - 1}] > node_count[{self.node_count}]")

        if self.tail is None:
            raise IndexError(f"linklist is empty")

        counter:int = 0
        node:LinkedListNode|None = self.tail

        while counter < index:
            node = node.prev
            if node is None:
                break

            counter += 1

        if node is None:
            raise IndexError(f"Attempting to get an element at index[{self.node_count - index - 1}] > node_count[{self.node_count}]")

        return node


    def add_value_head(self, new_value) -> None:
        new_node:LinkedListNode|None = LinkedListNode(new_value)
        self.add_node_head(new_node)


    def add_node_head(self, new_node:LinkedListNode|None) -> None:
        if new_node is None:
            return

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            next_node = self.head
            new_node.next = next_node
            next_node.prev = new_node
            self.head = new_node

        self.node_count += 1


    def add_value_tail(self, new_value) -> None:
        new_node:LinkedListNode|None = LinkedListNode(new_value)
        self.add_node_tail(new_node)


    def add_node_tail(self, new_node:LinkedListNode|None) -> None:
        if new_node is None:
            return

        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            prev_node = self.tail
            prev_node.next = new_node
            new_node.prev = prev_node
            self.tail = new_node

        self.node_count += 1


    def insert_value(self, new_value, index:int) -> None:
        new_node:LinkedListNode|None = LinkedListNode(new_value)
        self.insert_node(new_node, index)


    def insert_node(self, new_node:LinkedListNode|None, index:int) -> None:
        if new_node is None:
            return

        node_at_index:LinkedListNode|None = self.get(index)
        if node_at_index is None:
            raise IndexError(f"Unable to get element at index [{index}]")

        prev_node:LinkedListNode|None = node_at_index.prev

        if prev_node is not None:
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = node_at_index
            node_at_index.prev = new_node
        else:
            self.head = new_node
            new_node.next = node_at_index
            node_at_index.prev = new_node

        self.node_count += 1


    def insert_value_reverse(self, new_value, index:int) -> None:
        new_node:LinkedListNode|None = LinkedListNode(new_value)
        self.insert_node_reverse(new_node, index)


    def insert_node_reverse(self, new_node:LinkedListNode|None, index:int) -> None:
        if new_node is None:
            return

        node_at_index:LinkedListNode|None = self.get_reverse(index)
        if node_at_index is None:
            raise IndexError(f"Unable to get element at reverse index [{index}]")

        next_node:LinkedListNode|None = node_at_index.next
        if next_node is not None:
            node_at_index.next = new_node
            new_node.prev = node_at_index
            new_node.next = next_node
            next_node.prev = new_node
        else:
            self.tail = new_node
            new_node.prev = node_at_index
            node_at_index.next = new_node


    def remove_head(self) -> None:
        if self.head is None:
            raise IndexError(f"Attempting to remove first element from an empty linkedlist")

        next_node:LinkedListNode|None = self.head.next

        if next_node is None:
            self.head = None
        else:
            next_node.prev = None
            self.head = next_node

        self.node_count -= 1


    def remove_tail(self) -> None:
        if self.tail is None:
            raise IndexError(f"Attempting to remove last element from an emtpy linkedlist")

        prev_node:LinkedListNode|None = self.tail.prev

        if prev_node is None:
            self.tail = None
        else:
            prev_node.next = None
            self.tail = prev_node

        self.node_count -= 1


    def remove_node(self, node:LinkedListNode) -> None:
        if node is None:
            raise TypeError(f"Unable to remove element of type None")

        next_node:LinkedListNode|None = node.next
        prev_node:LinkedListNode|None = node.prev

        if next_node is None and prev_node is None:
            self.head = None
            self.tail = None
        elif next_node is None and prev_node is not None:
            self.tail = prev_node
            prev_node.next = None
        elif next_node is not None and prev_node is None:
                self.head = next_node
                next_node.prev = None
        elif next_node is not None and prev_node is not None:
            next_node.prev = prev_node
            prev_node.next = next_node

        self.node_count -= 1


    def remove_node_at(self, index:int) -> None:
        node_at_index:LinkedListNode = self.get(index)
        self.remove_node(node_at_index)


    def remove_node_at_reverse(self, index:int) -> None:
        node_at_index:LinkedListNode = self.get_reverse(index)
        self.remove_node(node_at_index)


    def print_all_elements(self) -> None:
        stack:list[str] = []

        node = self.head
        counter:int = 0
        while node is not None:
            stack.append(f"{counter}: {str(node.data)}")
            node = node.next
            counter += 1

        print(f"{"\n".join(stack)}\n--------------")


    def length(self) -> int:
        return self.node_count


