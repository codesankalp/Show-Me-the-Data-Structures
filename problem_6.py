# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:36:49 2020

@author: sankalp
"""

class Node:
    def __init__(self, value):
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


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    ls = []
    a = llist_1.head
    for i in range(llist_1.size()): 
        ls.append(a.value)
        a = a.next
    b = llist_2.head
    for i in range(llist_2.size()): 
        ls.append(b.value)
        b = (b.next)
    return list(set(ls))

def intersection(llist_1, llist_2):
    # Your Solution Here
    ls = []
    nls = []
    a = llist_1.head
    for i in range(llist_1.size()): 
        ls.append(a.value)
        a = a.next
    b = llist_2.head
    for i in range(llist_2.size()):
        if b.value in ls:
            nls.append(b)
        b = (b.next)
    return list(set(nls))


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
print()

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))