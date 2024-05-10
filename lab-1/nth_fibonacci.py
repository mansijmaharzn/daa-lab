def fibonacci(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
    

n = 10
print(f"{n}th fibonacci number: {fibonacci(n)}")


"""
Time Complexity:
O(2^n)
"""