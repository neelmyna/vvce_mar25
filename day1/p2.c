
#include <stdio.h>

int main()
{
    int num1 = 0;
    long int num2 = 0;
    long long int num3 = 0;
    double d = 0.0;
    float f = 0.0f;
    printf("%d  %d  %d  %d  %d \n", sizeof(num1), sizeof(num2), sizeof(num3), sizeof(d), sizeof(f));
    printf("%d  %d  %d  %d  %d", sizeof(int), sizeof(long int), sizeof(long long int), sizeof(double), sizeof(float));
    return 0;
}
