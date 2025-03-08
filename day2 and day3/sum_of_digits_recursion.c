#include "sum_of_digits.h"

int findSumOfDigits(int number)
{
    if (number == 0)
        return 0;
    return (number % 10) + findSumOfDigits(number / 10);
}