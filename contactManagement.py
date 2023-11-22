contacts = []

def add_contact(name, phone, mail):
    contact = {
        "Name": name, 
        "Phone": phone ,
          "Mail" : mail
          }
    contacts.append(contact)
    print(f"COntact {name} added\n")

def view_contacts():
    if not contacts:
        print("No contact to display.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']},  Mail: {contact['Mail']}") 

def search_contact(name):
    con_found= False
    for contact in contacts:
        if contact['Name']== name:
             print("Contact Found: ")
             print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Mail: {contact['Mail']}") 
             con_found= True
             break
        else:
            print("There is no contact in this name")

            

        
if __name__ == "__main__":
    print("Welcome to the Contact Management System!\n")

    while True:
        print("Options:")
        print("1. Add contact")
        print("2.View Contact List")
        print("3. Search")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter Your name: ")
            phone = input("ENter your Phone Number: ")
            mail= input("ENter your Mail: ")
            add_contact(name, phone, mail)
        
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("Enter your Name: ")
            search_contact(name)

            
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3 or 4.\n")