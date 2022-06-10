import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        
##    def __repr__(self):
##        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def reverse(head):           
    prev_node = None
    next_node = head
    
    while next_node:
        if prev_node == None:
            llist.tail = head
            
        copy_prev_node = prev_node
        copy_next_next_node = next_node.next
        
        prev_node = next_node
        next_node.next = copy_prev_node
        next_node = copy_next_next_node
    
    head = prev_node
    return head
    
def printLinkedList(head):
    if head:
        print(head.data)
        printLinkedList(head.next)

if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        printLinkedList(llist.head)
