# Add two numbers represented by linked lists
# https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1
# Given two numbers represented by two linked lists of size N and M. The task is to return a sum list.

# The sum list is a linked list representation of the addition of two input numbers from the last.


#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        head = None
        temp = None
        c = 0
        while first or second:
            if not first:
                a= 0
            else:
                a = first.data
            if not second:
                b=0
            else:
                b = second.data
            n = a +b + c
            c = 1 if n>9 else 0
            node = Node(n%10)
            if not head:
                head = node
                temp = node
            else:
                head.next = node
                head = node
            first = first.next if first else None
            second = second.next if second else None
        if c:
            node = ListNode(1)
            head.next = node
        return temp
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends