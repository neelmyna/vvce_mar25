import sys

def insertRecord():
    print('Record Inserted')

def deleteRecord():
    print('Record Deleted')

def updateRecord():
    print('Record Updated')

def searchRecord():
    print('Record Found')

def listAllRecords():
    print('All records Listed')

def exit_program():
    sys.exit('End of Program')

def invalid_choice():
    print('Invalid choice entered')

def get_menu():
    menu = {
        1 : insertRecord,
        2 : deleteRecord,
        3 : updateRecord,
        4 : searchRecord,
        5 : listAllRecords,
        6 : exit_program
    }
    return menu

def start_app():
    choice = 0
    while True:
        print('1:Create 2:Delete 3:Update 4:Search 5:ListAll 6:Exit')
        choice = int(input('Enter your choice: '))
        menu = get_menu()
        menu.get(choice, invalid_choice)()

start_app()