def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a%b)


def gcd_interative(a, b):
    while b !=0:
        r = a % b
        a = b
        b = r
    
    return a


print(gcd(90, 24))
print(gcd_interative(90, 24))