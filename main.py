from contactlist import ContactList

def main():
    contact_list = ContactList()
    while True:
        option = int(input("Do you want to: 1) Add 2) Remove 3) Change Phone# 4) Print Contacts 5) Quit?\n"))
        if option == 5:
            break
        if option == 1:
            new_name = input("Enter name: ").capitalize()
            new_number = input("Enter number: ")
            contact_list.add(new_name, new_number)
        if option == 2:
            delete_name = input("Enter the name to remove: ").capitalize()
            contact_list.remove(delete_name)
        if option == 3:
            target_name = input("Enter name: ")
            updated_number = input("Enter new number: ")
            contact_list.change_phone_number(target_name, updated_number)
        if option == 4:
            print(contact_list)

main()