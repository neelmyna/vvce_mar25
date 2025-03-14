def find_area_rectangle(lengt = 11, breadth = 15):
    return length * breadth

length = int(input('Enter length of the Rectangle: '))
breadth = int(input('Enter breadth of the Rectangle: '))

area = find_area_rectangle(length, breadth)
print(f'Area of the Rectangle = {area}')

area = find_area_rectangle(length)
print(f'Area of the Rectangle = {area}')

area = find_area_rectangle()
print(f'Area of the Rectangle = {area}')

#area = find_area_rectangle(breadth = 12, length = 18)
#print(f'Area of the Rectangle = {area}')
