function fibTab(n) {
  if (n <= 1) return n;

  let arr = [];
  arr[0] = 0;
  arr[1] = 1;

  for (let i = 2; i < n + 1; i++) {
    arr[i] = arr[i - 1] + arr[i - 2]
  }

  return arr[n]
}

console.log(fibTab(10))
