#############################################
# Name: Abby Lende
# Submission Date: 12/1/2020
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 27
#############################################

class Phone_Book: 
    def __init__(self, contactName, number): 
        self.contactName = contactName 
        self.number = number 


def readFile(fileName):
    lista = [] 
    file1 = open(fileName, 'r') 

    lines = file1.readlines()

    for line in lines:
        lista_num = []
        lista_num.append(line)
            

        lista.append(lista_num)
        # except ValueError: print(f'Invalid data found at line {} in the file.\n') 

    return lista

# print('Data Imported Successfully') 
"""
def writeFile(fileName): 
    file1 = open(fileName, 'w') 
    for obj in list: 
        file1.write(obj.contactName + ',' + obj.number) 

# print('Data Written Successfully') 

def printEntries(): 
    print('The Phone Book Details are as follows :\n\t\tName\t\tNumber') 
    for obj in list: 
        print('{0:<20}{1:>10}'.format(obj.contactName, obj.number)) 

    print('-------------- End of Contact List -------------\n\n') 


def searchPhonebook(): 
    name = input('Enter a name to search : ') 
    for obj in list: 
        if obj.contactName == name: 
            print('Name : ' + obj.contactName) 
            print('Phone : ' + obj.number) 

def addToPhonebook(): 
    name = input('Enter Contact name : ') 
    number = input('Enter Contact number : ') 
    list.append(Phone_Book(name, number)) 
    writeFile('phone_book.txt') 
    print('Contact Added Successfully') 


def deleteFromPhonebook(): 
    name = input('Enter Contact name : ') 
    for obj in list: if obj.contactName == name: 
        list.remove(obj) writeFile('phone_book.txt') 
    
    print('Contact Removed Successfully') 
"""

def count_words(filename):

    file = open(filename, "rt")
    reader = file.read()
    reader = reader.lower()

    lista = reader.split()

    dic = {}
    for x in lista:
        num = 0
        for y in lista:
            dic[x] = num

            if x == y:
                num += 1
                dic.update({x: num})

    return dic


def main(): 

    lista = readFile('phone.txt') 
    print('----------- Phone book Menu Driven Program -----------') 

    print(lista)
    """while True: 
        print('Enter your choice : \n\t1. for Phone book Search\n\t2. for Add contact to Phone book\n\t3. for Delete ' 'contact from Phone book\n\t4. for Printing the Contact List from Phone book\n\t5. for Exit') 
    
    print(lista)
    
    choice = input('Enter your choice : ') 
    if choice == '1': 
        searchPhonebook() 
    elif choice == '2': 
        addToPhonebook() 
    elif choice == '3': 
        deleteFromPhonebook() 
    elif choice == '4': 
        printEntries() 
    elif choice == '5': 
        exit(0) 
    else: 
        print('Wrong Choice inputted. Please try Again') 
    """

if __name__ == "__main__":    
    main()