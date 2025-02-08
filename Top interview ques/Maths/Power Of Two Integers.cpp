//Given a positive integer that fits in a 32-bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0.

#include <iostream>
#include <cmath>

using namespace std;

int isPower(int A) {
    if (A <= 1) return 1;

    for (int p = 2; p <= log2(A); p++) {
        int a = pow(A, 1.0 / p);
        if (pow(a, p) == A || pow(a + 1, p) == A) {
            return 1;
        }
    }
    return 0;
}
