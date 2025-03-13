my_name = input('Enter the main string: ')
sub_string = input('Enter the sub string: ')

print(my_name) # nithin
print(my_name.upper()) # NITHIN
try:
    print(my_name.index(sub_string)) # 2
    print('next stmt')
except TypeError:
    print('May be you did not enter a string value')
except ValueError:
    print(f'The sub-string {sub_string} not found in {my_name}')

print(my_name.capitalize()) # Nithin
print(my_name.find('tt')) # 2

# print(f'The sub-string \'tt\' not found in {my_name}')