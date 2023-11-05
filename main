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
    def __init__(self, value: str) -> None:
        super().__init__(value)
        if not self.is_valid():
            raise ValueError("Номер телефону повинен складатися з 10 цифр")

    def is_valid(self):
        return len(self.value) == 10 and self.value.isdigit()
    
    fl = False
class Record:

    def __init__(self, name:Name)->None:
        self.name = name
        self.list_phones = []    
    
    def __str__(self):
        return f'{self.name} - {self.list_phones}'    
    
    def add_phone(self, phone:Phone):
        if phone.isvalid():
            self.list_phones.append(phone)
        else:
            return 'Invalid phone number'
    
    def edit_phone(self, phone:Phone, new_phone:Phone)-> str:
        temp_list_phone = []
        str_result =''
        for ph in self.list_phones:
            if ph != phone:
                temp_list_phone.append(ph)
            else:
                temp_list_phone.append(new_phone)
                str_result += f'Phone {phone} updated to {new_phone}\n'
        self.list_phones = temp_list_phone
        if not str_result:
            return f'Phone {phone} not found'
        return str_result   
        
    def remove_phone(self, phone:Phone):
        temp_list_phone = []
        str_result =''
        for ph in self.list_phones:
            if ph!= phone:
                temp_list_phone.append(ph)
            else:
                str_result += f'{phone} is removed'
        self.list_phones = temp_list_phone
        if not str_result:
            return f'Phone {phone} not found'
        return str_result
    
    def find_phone(self, phone: Phone):
        found_phones = [str(ph) for ph in self.list_phones if str(ph) == str(phone)]
        if found_phones:
            return ", ".join(found_phones)
        else:
            return f"Phone {phone} not found"


class AddressBook(UserDict):
    
    def add_record(self, record:Record):
        self.data[record.name.value] = record
    
    def delete(self, name:str)-> str:
        if name in self.data:
            del self.data[name]
            return f'Contact {name} is deleted'
        else:
            return f'Contact {name} not found'

    def find(self, name:str)-> str:
        if name in self.data:
            return self.data[name]
        else:
            return f'Contact {name} not found'

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

