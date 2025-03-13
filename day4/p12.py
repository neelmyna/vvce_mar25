input_str = input('Enter the input string: ') # the input string may consist of letters, digits and symbols as well.

digits = [] # Take a list to capture only digits from the input string
#digits = list()

for char in input_str: # iterate every character in the given string
    if char.isdigit(): # check if the char is a digit
        digits.append(char) # if yes, copy it to list

digits = list(set(digits)) # convert the list to set to remove the duplicates and convert it back to a list to process the data easily
digits.sort(reverse=True) # sort the strings(digits) in the list in decreasing order

digits_str = ''.join(digits) # convert the list to string
biggest_number = int(digits_str) # convert the string to int number
print(f'The resultant number is {biggest_number}')