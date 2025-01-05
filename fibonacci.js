function fibonacci(n) {
	if (n <= 1) return n; 
	 
	let prev2 = 0; prev1 = 1; 

	for (let i = 2; i <= n; i++) {
		[prev1, prev2] = [prev1 + prev2, prev1];
	}

	return prev1; 
}

console.log(fibonacci(10))
