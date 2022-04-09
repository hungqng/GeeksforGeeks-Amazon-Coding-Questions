# Given a string S. The task is to print all permutations of a given string in lexicographically sorted order.

#User function Template for python3

class Solution:
    def find_permutation(self, S):
        # Code here
        # permutation_list = []
        # if len(S) == 1:
        #     return [S]
        # else:
        #     for char in S:
        #         [permutation_list.append(char + a) for a in self.find_permutation(S.replace(char, "", 1))]
        # return permutation_list

        if len(S) == 1:
            return [S]
        permutations = self.find_permutation(S[1:])
        character = S[0]
        result = []
        for p in permutations:
            for i in range(len(p) + 1):
                result.append(p[:i] + character + p[i:])
        return result

        # if len(S) == 1:
        #     return S

        # recursive_perms = []
        # for c in S:
        #     for perm in self.find_permutation(S.replace(c,'',1)):
        #         recursive_perms.append(c+perm)

        # return set(recursive_perms)
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends