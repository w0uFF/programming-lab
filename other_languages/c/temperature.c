/* Basic Celsius-to-Fahrenheit table for C practice. */
#include <stdio.h>

static double fahrenheit(double celsius) {
    return (celsius * 9.0 / 5.0) + 32.0;
}

int main(void) {
    for (int value = -10; value <= 40; value += 10) {
        printf("%3d C -> %6.1f F\n", value, fahrenheit((double)value));
    }
    return 0;
}
