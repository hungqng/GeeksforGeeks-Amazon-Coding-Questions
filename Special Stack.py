# Special Stack 
# https://practice.geeksforgeeks.org/problems/special-stack/1
# Design a data-structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() 
# and an additional operation getMin() which should return minimum element from the SpecialStack. 
# Your task is to complete all the functions, using stack data-Structure.

# Your Task:
# Since this is a function problem, you don't need to take inputs. You just have to complete 5 functions, push() which takes the stack and an integer x as input and pushes it into the stack; pop() which takes the stack as input and pops out the topmost element from the stack; isEmpty() which takes the stack as input and returns true/false depending upon whether the stack is empty or not; isFull() which takes the stack and the size of the stack as input and returns true/false depending upon whether the stack is full or not (depending upon the
# given size); getMin() which takes the stack as input and returns the minimum element of the stack. 
# Note: The output of the code will be the value returned by getMin() function.

# Expected Time Complexity: O(N) for getMin, O(1) for remaining all 4 functions.
# Expected Auxiliary Space: O(1) for all the 5 functions.

# Constraints:
# 1 ≤ N ≤ 104

class stack:
 
  def __init__(self):
 
    self.array = []
    self.top = -1
    self.max = 100 
 
  # Stack's member method to check
  # if the stack is empty
  def isEmpty(self):
 
    if self.top == -1:
      return True
    else:
      return False 
 
  # Stack's member method to check
  # if the stack is full 
  def isFull(self): 
     
    if self.top == self.max - 1:
      return True
    else:
      return False  
 
  # Stack's member method to
  # insert an element to it  
 
  def push(self, data):
 
    if self.isFull():
      print('Stack OverFlow')
      return
    else:
      self.top += 1
      self.array.append(data)    
 
  # Stack's member method to
  # remove an element from it
  def pop(self):
 
    if self.isEmpty():
      print('Stack UnderFlow')
      return
    else:
      self.top -= 1
      return self.array.pop()