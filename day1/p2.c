#include <stdio.h>

int main()
{
    int inputNumber = 0;
    puts("Enter a number to print its Math table");
    scanf("%d", &inputNumber);
    for (int i = 1; i <= 20; i++)
    {
        printf("%d * %02d  %03d \n", inputNumber, i, inputNumber * i);
    }
}