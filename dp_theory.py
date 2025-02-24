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
