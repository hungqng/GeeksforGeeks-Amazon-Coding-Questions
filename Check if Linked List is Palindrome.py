# Check if Linked List is Palindrome
# Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.
# https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1/

#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        slow = head
 
    # Declare a stack
        stack = []
     
        ispalin = True
 
    # Push all elements of the list
    # to the stack
        while slow != None:
            stack.append(slow.data)
         
        # Move ahead
            slow = slow.next
 
    # Iterate in the list again and
    # check by popping from the stack
        while head != None:
 
        # Get the top most element
            i = stack.pop()
         
        # Check if data is not
        # same as popped element
            if head.data == i:
                ispalin = True
            else:
                ispalin = False
                break
 
        # Move ahead
            head = head.next
         
        return ispalin
#{ 
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends