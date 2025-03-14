import sys

def enQueue(queue):
    element = input('Enter element to be inserted: ')
    queue.append(element)

def deQueue(queue): # Mutator
    if len(queue) == 0:
        print('queue is empty')
        return
    print(f'Popped element is {queue[0]}')
    del queue[0]

def listQueue(queue): # Accessor
    if len(queue) == 0:
        print('Queue is empty')
        return
    print(f'The Queue is {queue}')

def firstElement(queue): # read only function 
    if len(queue) == 0:
        print('queue is empty')
        return
    print('The first element is', queue[0])

def exit_program(queue):
    sys.exit('End of Program')

def get_menu(choice, queue):
   match choice:
       case 1 : enQueue(queue)
       case 2 : deQueue(queue) 
       case 3 : listQueue(queue) 
       case 4 : firstElement(queue)
       case 5 : exit_program(queue)
       case _: print('invalid choice')

def start_app(queue):
    choice = 0
    while True:
        print('1:Insert 2:Delete 3:ListQueue 4:FirstElement 5:Exit')
        choice = int(input('Enter your choice: '))
        get_menu(choice, queue)

queue = [] # this list is gonna work as queue
start_app(queue)