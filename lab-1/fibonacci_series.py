def fibonacci(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
    

n = 10
for i in range(1, n+1):
    print(fibonacci(i), end=", ")


"""
Time Complexity: O(2^n)
Space Complexity: O(n)
"""