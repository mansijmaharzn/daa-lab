def factorial(n):
    first = 0 
    second = 1
    
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


factorial(20)


"""
Time Complexity:
O(n)
"""
