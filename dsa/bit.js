function countBits(n) {
  let bitCountArr = []
	for (let i = 0; i <= n; i++) {
		bitCountArr.push(i.toString(2).split('1').length - 1)
	} 
	return bitCountArr
};

console.log(countBits(2))
