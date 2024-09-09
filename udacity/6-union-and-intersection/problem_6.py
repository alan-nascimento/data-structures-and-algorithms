from typing import Set


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value: int):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    unique_values: Set[int] = set()

    current = llist_1.head
    while current:
        unique_values.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        unique_values.add(current.value)
        current = current.next

    union_list = LinkedList()
    for value in unique_values:
        union_list.append(value)

    return union_list


def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    set1: Set[int] = set()
    set2: Set[int] = set()

    current = llist_1.head
    while current:
        set1.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        set2.add(current.value)
        current = current.next

    intersection_set = set1.intersection(set2)

    intersection_list = LinkedList()
    for value in intersection_set:
        intersection_list.append(value)

    return intersection_list


## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Test Case 1")
print("Union of linked lists:")
result_union = union(linked_list_1, linked_list_2)
print(result_union)
assert (
    str(result_union) == "32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> "
)
print("Intersection of linked lists:")
result_intersection = intersection(linked_list_1, linked_list_2)
print(result_intersection)
assert str(result_intersection) == "4 -> 21 -> 6 -> "

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("\nTest Case 2")
print("Union of linked lists:")
result_union = union(linked_list_3, linked_list_4)
print(result_union)
assert (
    str(result_union)
    == "65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> "
)
print("Intersection of linked lists:")
result_intersection = intersection(linked_list_3, linked_list_4)
print(result_intersection)
assert str(result_intersection) == ""

## Test Case 3: Edge case with empty lists
print("\nTest Case 3")
empty_list_1 = LinkedList()
empty_list_2 = LinkedList()

print("Union of empty linked lists:")
result_union = union(empty_list_1, empty_list_2)
print(result_union)
assert str(result_union) == ""
print("Intersection of empty linked lists:")
result_intersection = intersection(empty_list_1, empty_list_2)
print(result_intersection)
assert str(result_intersection) == ""

## Test Case 4: Edge case with one empty list
linked_list_5 = LinkedList()
empty_list_3 = LinkedList()

element_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]

for i in element_3:
    linked_list_5.append(i)

print("\nTest Case 4")
print("Union of a non-empty linked list and an empty linked list:")
result_union = union(linked_list_5, empty_list_3)
print(result_union)
assert str(result_union) == "65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 23 -> "
print("Intersection of a non-empty linked list and an empty linked list:")
result_intersection = intersection(linked_list_5, empty_list_3)
print(result_intersection)
assert str(result_intersection) == ""

## Test Case 5: Large values
large_linked_list_1 = LinkedList()
large_linked_list_2 = LinkedList()

element_4 = list(range(1, 10000, 2))
element_5 = list(range(2, 10000, 2))

for i in element_4:
    large_linked_list_1.append(i)

for i in element_5:
    large_linked_list_2.append(i)

print("\nTest Case 5")
print("Union of large linked lists:")
result_union = union(large_linked_list_1, large_linked_list_2)
print(result_union)
assert result_union.size() == 9999
print("Intersection of large linked lists:")
result_intersection = intersection(large_linked_list_1, large_linked_list_2)
print(result_intersection)
assert result_intersection.size() == 0

print("All test cases passed successfully!")
