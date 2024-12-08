parts = [
  (1000, 'M'),
  (900, 'CM'),
  (500, 'D'), 
  (400, 'CD'),
  (100, 'C'),
  (90, 'XC'),
  (50, 'L'),
  (40, 'XL'), 
  (10, 'X'),
  (9, 'IX'),
  (5, 'V'),
  (4, 'IV'),
  (1, 'I'),
]

def integer_to_roman(n):
  for d, r in parts:
    if d <= n:
      return r + integer_to_roman(n - d)
  return ""

# Tests for integer_to_roman function
cases = ((39, 'XXXIX'), (2421, 'MMCDXXI'))
for n, x in cases:
  assert integer_to_roman(n) == x

print("\033[92mAll test cases passed!\033[0m")
