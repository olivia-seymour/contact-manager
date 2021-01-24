# CONTACT MANAGER
# Olivia Seymour
# Jan 2021

import json

# read in contacts --------------------------
def read():

    # open file
    textFile = open("contacts.txt")

    # read file
    content = textFile.read()

    # close file
    textFile.close()

    # reformat content as a dictionary
    contacts = json.loads(content)

    # return contacts
    return contacts


# display contact in correct format ------------
def displayContact(contact):
    print("\n" + contact[0])
    print("\tPhone: " + contact[1])
    print("\tEmail: " + contact[2])


# view contacts -----------------------------------
def view(contacts):

    # print all contacts
    for i in contacts:
        displayContact(contacts[i])

    print("\n")


# check if a key is inside the dictionary -------------
def checkKey(contacts, key):
    if key in contacts.keys():
        return True
    else:
        return False
  


# add contact -------------------------------------------
def add(contacts):

    # get name, phone, and email
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    # add to dictionary
    contacts[name] = [name, phone, email]

    # display new contact
    print("\nNew contact:")
    displayContact(contacts.get(name))
    print("\n")



# delete contact --------------------------------------
def delete(contacts):

    # get name
    print("\n")
    name = input("Enter name: ")

    # make sure the name is valid
    if checkKey(contacts, name) == False:
        print("\nName not in contacts.\n")
        return

    # double check
    displayContact(contacts.get(name))
    print("\n")

    check = input("Are you sure you want to delete this contact? (y/n): ")
    print("\n")

    # delete the chosen contact if confirmed
    if check == "y" or check == "Y":
        del contacts[name]
        print("Contact deleted.\n")
    else:
        print("Contact not deleted.\n")


# edit contact ---------------------------------------------
def edit(contacts):

    # which contact?
    print("\n")
    name = input("Enter name: ")

    # check that the name is valid
    if checkKey(contacts, name) == False:
        print("\nName not in contacts.\n")
        return

    # what changes?
    print("\n")
    detail = input("Enter 'p' to change the phone number or 'e' to change the email :")

    # make sure input was valid
    if not(detail == "e" or detail == "E" or detail == "p" or detail == "P"):
        print("\nInvalid input; no changes made.\n")
        return

    # new value?
    print("\n")
    value = input("What should it be changed to?: ")

    # make the switch
    if detail == "e" or detail == "E":
        contacts.get(name)[2] = value
    elif detail == "p" or detail == "P":
        contacts.get(name)[1] = value
    else:
        print("\nNo changes made.\n")
        return

    #display new contact
    print("\nUpdated contact:\n")
    displayContact(contacts.get(name))
    print("\n")


# write contacts ---------------------------------------
def write(contacts):

    # open file
    textFile = open("contacts.txt", 'w')
    
    # write contacts
    json.dump(contacts, textFile)

    # close file
    textFile.close()
     

# MAIN ----------------------------------------------

print("Welcome!")

# read in contacts
contacts = read()

response = -1

while response != 5:

    # print options and get response

    print("Please select an action:")
    print("1 - View Contacts")
    print("2 - Add a Contact")
    print("3 - Delete a Contact")
    print("4 - Edit a Contact")
    print("5 - Quit\n")

    response = int(input("Enter a number: "))

    if response == 1:
        view(contacts)

    if response == 2:
        add(contacts)

    if response == 3:
        delete(contacts)

    if response == 4:
        edit(contacts)

# write the contacts to the text file
write(contacts)

print("Goodbye!")

