def min_splits_formula(m, n):
    return m * n - 1

def test_min_splits_formula():
    # Test 1x1 chocolate bar
    assert min_splits_formula(1, 1) == 0
    
    # Test 2x2 chocolate bar
    assert min_splits_formula(2, 2) == 3
    
    # Test 2x3 chocolate bar
    assert min_splits_formula(2, 3) == 5
    
    # Test 3x3 chocolate bar
    assert min_splits_formula(3, 3) == 8
    
    # Test larger chocolate bars
    assert min_splits_formula(4, 5) == 19
    assert min_splits_formula(6, 8) == 47

    print("\033[92mAll test cases passed!\033[0m")

test_min_splits_formula()