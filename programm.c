#include <stdio.h>

void findSum(int m, int n) {
    int sumDiv = 0, sumNotDiv = 0;

    for(int i = 1; i <= n; i++) {
        if(i % m == 0) {
            sumDiv += i;
        } else {
            sumNotDiv += i;
        }
    }

    printf("Sum of numbers divisible by %d = %d\n", m, sumDiv);
    printf("Sum of numbers not divisible by %d = %d\n", m, sumNotDiv);
}

int main() {
    int m, n;

    printf("Enter value of m: ");
    scanf("%d", &m);

    printf("Enter value of n: ");
    scanf("%d", &n);

    findSum(m, n);

    return 0;
}
