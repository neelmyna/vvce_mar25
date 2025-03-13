# program to print Math table of a number

input_number = int(input('Enter a number to print its Math table: '))

for i in range(1, 21):
    #print(f'{input_number} * {i} = {input_number * i}')
    print('%d * %02d = %03d'%(input_number, i, input_number * i))