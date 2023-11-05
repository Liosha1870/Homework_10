from collections import UserDict

class Field:
    
    def __init__(self, value:str)-> None:
        self.value = value
        self.fl = None    
    
    def __str__(self) -> str:
        return self.value
    
class Name(Field):
    fl = True
    
class Phone(Field):
    def __init__(self, phone: str) -> None:
        new_phone = phone.strip()
        for c in '+( )-.':
            new_phone = new_phone.replace(c, "")
        if len(new_phone) == 10 and new_phone.isdigit():
            super().__init__(phone)
        else:
            raise ValueError(f"{phone} - incorrect phone number")
            
    def __str__(self):
        return self.value
    
    fl = False
class Record:

    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []    
    
    def __str__(self):
        return f'{self.name} - {self.list_phones}'    
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return 
        raise ValueError(f"Number {old_phone} not found") 
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None


class AddressBook(UserDict):
    
    def add_record(self, record:Record):
        self.data[record.name.value] = record
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def find(self, name):
        return self.data.get(name)

def parse_command(user_input, address_book):
    if user_input.startswith("/add"):
        name = input("Enter contact name: ")
        record = Record(Name(name))
        while True:
            phone_number = input("Enter phone number (or press Enter to finish): ")
            if not phone_number:
                break
            phone = Phone(phone_number)
            if phone.is_valid():
                record.add_phone(phone)
            else:
                print("Invalid phone number. Please enter a 10-digit number.")
        address_book.add_record(record)
        print(f"Contact {name} added.")

    elif user_input.startswith("/edit"):
        name = input("Enter contact name: ")
        if name not in address_book.data:
            print(f"Contact {name} not found.")
            return
        record = address_book.data[name]
        phone_number = input("Enter the phone number to edit: ")
        new_phone_number = input("Enter the new phone number: ")
        result = record.edit_phone(Phone(phone_number), Phone(new_phone_number))
        if result:
            print(result)

    elif user_input.startswith("/find"):
        name = input("Enter contact name: ")
        result = address_book.find(name)
        if "not found" in result:
            print(result)
        else:
            print(result)

    elif user_input.startswith("/delete"):
        name = input("Enter contact name: ")
        result = address_book.delete(name)
        print(result)

    elif user_input.startswith("/list"):
        for name, record in address_book.data.items():
            print(record)

    elif user_input.startswith("/exit"):
        return True

    return False

def main():
    address_book = AddressBook()
    print("Address Book Program")
    print("Commands:")
    print("/add - Add a new contact")
    print("/edit - Edit an existing contact")
    print("/find - Find a contact")
    print("/delete - Delete a contact")
    print("/list - List all contacts")
    print("/exit - Exit the program")
    while True:
        user_input = input("Enter a command: ")
        exit_program = parse_command(user_input, address_book)
        if exit_program:
            break

if __name__ == "__main__":
    main()


