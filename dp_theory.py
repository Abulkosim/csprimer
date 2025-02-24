'''
Dynamic programming: 

1. optimal substructure -> if an optimal solution to the entire problem can be constructed from optimal solutions to its subproblems.
2. overlapping subproblems -> if the recursive breakdown of the task solves the same subproblem multiple times. 

examples: 
1. knapsack problem, shortest path, etc. 
2. fibonacci numbers, longest common subsequence, etc. 

Implementation styles: 
1. top-down (memoization)
2. bottom-up (tabulation)

'''

def fib_memo(n, memo=None):
	if memo is None: 
		memo = {}

	if n in memo: 
		return memo[n]

	if n <= 1: 
		memo[n] = n
		return n

	result = fib_memo(n-1, memo) + fib_memo(n-2, memo)

	memo[n] = result
	return result


print(fib_memo(10))

'''
Longest common subsequence: 
'''

def lcs_memo(X, Y, i=None, j=None, memo=None):
    """
    Returns the length of the LCS of X and Y using top-down memoization.
    i, j represent the current indices we are considering in X, Y respectively.
    """
    if memo is None:
        memo = {}
    if i is None:
        i = len(X)
    if j is None:
        j = len(Y)

    # If already in memo, return it
    if (i, j) in memo:
        return memo[(i, j)]

    # Base case: if one string is empty
    if i == 0 or j == 0:
        memo[(i, j)] = 0
        return 0

    # If the last characters match
    if X[i-1] == Y[j-1]:
        memo[(i, j)] = 1 + lcs_memo(X, Y, i-1, j-1, memo)
    else:
        # If they don't match
        memo[(i, j)] = max(
            lcs_memo(X, Y, i-1, j, memo),
            lcs_memo(X, Y, i, j-1, memo)
        )

    return memo[(i, j)]


# Example usage:
X = "ABCDGH"
Y = "AEDFHR"
print(lcs_memo(X, Y))  # 3 (LCS is "ADH")
 
 
 
