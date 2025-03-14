def my_function(my_numbers):
    my_numbers[0] = 1000
    my_numbers[-1] = 10000

print('Enter space seperated numbers of your choice')
numbers = [int(element) for element in input().split()]
print(numbers)
my_function(numbers) # call by refrence
print(numbers)

# values = input().split()
# print(values)
# print(type(values))