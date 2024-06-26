def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)
    

num = 5
print(f"Factorial of {num} is {factorial(num)}")


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""