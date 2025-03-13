my_str = 'nithin:1233'

values = my_str.split(':')
string_part = values[0] # copy or reference
sum = 0
for char in values[1]:
    sum = sum + int(char) ** 2

if sum % 2 == 0:
	new_str = string_part[-1] + string_part[:-1]
else:
	new_str = string_part[2:] + string_part[:2]

print(new_str)