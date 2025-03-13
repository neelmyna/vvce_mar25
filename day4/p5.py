# Program to print the numbers from m to n (m < n) with an incriment of p

m = int(input('Enter the M value (start value): '))
n = int(input('Enter the N value (End value): '))
p = int(input('Enter the P value (Increment): '))

for i in range(m, n, p): # 10, 40, 3
    print(i, end=' ')
    i += 2
