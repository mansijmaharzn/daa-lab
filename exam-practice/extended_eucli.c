#include<stdio.h>


// Function to perform the extended Euclidean algorithm
int extendedGCD(int a, int b, int *x, int *y) {
    // Base case: if b is 0, gcd is a, and the coefficients are x=1, y=0
    if (b == 0) {
        *x = 1;
        *y = 0;
        return a;
    }

    // Recursively call the function
    int x1, y1;  // To store results of recursive call
    int gcd = extendedGCD(b, a % b, &x1, &y1);

    // Update x and y using the results of the recursive call
    *x = y1;
    *y = x1 - (a / b) * y1;

    return gcd;
}


int main() {
    int a, b;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);

    int x, y;
    int gcd = extendedGCD(a, b, &x, &y);

    printf("GCD of %d and %d is %d\n", a, b, gcd);
    printf("Coefficients x and y are: x = %d, y = %d\n", x, y);

    // Check the result using Bézout's identity
    printf("Verification: %d * %d + %d * %d = %d\n", a, x, b, y, a * x + b * y);

    return 0;
}