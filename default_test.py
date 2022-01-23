def test_default_solution(result, expected):
    print("Running default test")
    print("-------------------------")
    if result == expected:
        print(f"OK. Result expected was {result}")
        print("-------------------------")
        return True
    else:
        print(f"Test Failed. Expression evaluates to: {result}. Expected: {expected}")
        return False