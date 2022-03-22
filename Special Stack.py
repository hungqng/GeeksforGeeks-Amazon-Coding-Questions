# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    # Code here
    arr.append(ele)
# Function should pop an element from stack
def pop(arr):
    # Code here
    if arr.isEmpty():
        return "The stack is empty."
    else:
        return arr.pop()
# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    if len(arr) == n:
        return True
    else:
        return False
# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    if arr == []:
        return True
    else:
        return False
# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    arr.sort()
    return arr[0]
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        while(not isEmpty(stack)):
            pop(stack)
            
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
# contributed by: Harshit Sidhwa

# } Driver Code Ends