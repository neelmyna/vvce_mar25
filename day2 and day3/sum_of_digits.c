#include "sum_of_digits.h"

int findSumOfDigits(int number)
{
    int sumOfDigits = 0, remainderDigit = 0;
    while (number != 0)
    {
        remainderDigit = number % 10;
        sumOfDigits = sumOfDigits + remainderDigit;
        number = number / 10;
    }
    return sumOfDigits;
}