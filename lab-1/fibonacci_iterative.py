def generate_fibonacci(n):
    first, second = 1, 1
    
    if n >= 1:
        print(f"First {n} series: {first}", end="")
    
    if n >= 2:
        print(f", {second}", end="")

    for i in range(3, n+1):
        next = first + second
        print(f", {next}", end="")
        first = second
        second = next
    
    print()


num = 10
generate_fibonacci(num)


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
