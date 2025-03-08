#include "sum_of_digits.h"
#include <stdio.h>

int main()
{
    int inputNumber = 0;
    puts("Enter a number to find sum of its digits");
    scanf("%d", &inputNumber);
    int sumOfDigits = findSumOfDigits(inputNumber);
    printf("Sum of the digits of %d is %d", inputNumber, sumOfDigits);
}
