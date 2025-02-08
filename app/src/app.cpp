#include "fib.h"
#include <stdio.h>

int main(void) {
    int n = 10;
    int result = fibonacci(n);
    printf("fibonacci(%d) = %d\n", n, result);
    return 0;
}