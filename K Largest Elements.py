# K largest elements
# Given an array of N positive integers, print k largest elements from the array. 

#User function Template for python3

class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        # code here
        li.sort() #1,5,12,23,787
        result = []
        for i in range(n - k, n):
            result.append(li[i])
        return result[::-1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n=li[0]
    k=li[1]
    li = [int(x) for x in input().strip().split()]
    ob=Solution()
    k_largest_list = ob.kLargest(li,n,k)
    
    for element in k_largest_list:
        print(element, end = ' ')
    print('')
# } Driver Code Ends