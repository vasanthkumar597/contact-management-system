#contact book


class contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}..."
class contact_book:
    def __init__(self):
        self.contacts=[]
    def add_contact(self):
        name=input("enter the name: ")
        phone=input("enter the phone: ")
        email=input("enter teh mail-id: ")

        contacts=contact(name,phone,email)
        self.contacts.append(contacts)
        print("contact added")
    def view_contacts(self):
        if  len(self.contacts)==0:
            print("no contacts found")
        else:
            for contact in self.contacts:
                print(contact)
    
    def search_contact(self,name):
        for c in self.contacts:
            if c.name==name:
                print(c)
                return
        print("not found")
    def update_contact(self,name,new_name,new_phone,new_email):
        for c in self.contacts:
            if c.name==name:
                c.name=new_name
                c.phone=new_phone
                c.email=new_email
                print("contact updated")
                return
        print("contact not found")
    def delete_contact(self,name):
        for c in self.contacts:
            if c.name==name:
                self.contacts.remove(c)
                print("contact deleted")
                return
        print("contact not found")

        
book=contact_book()

while True:
    print("--------contact book menu-------")
    print("1.add contact")
    print("2.view contact")
    print("3.search contact")
    print("4.update contact")
    print("5.delete contact")
    print("6.exit")
    
    choice=input("enter your choice: ")

    if choice=="1":
        book.add_contact()
    elif choice=="2":
        book.view_contacts()
    elif choice=="3":
        name=input("enter the name: ")
        book.search_contact(name)
    elif choice=="4":
        name=input("enter the name you want to update: ")
        new_name=input("enter the new name: ")
        new_phone=input("enter the new phone: ")
        new_email=input("enter the new_mail: ")
        book.update_contact(name,new_name,new_phone,new_email)
    elif choice =="5":
        name=input("enter the name: ")
        book.delete_contact(name)
    elif choice=="6":
        print("thank you")
    else:
        print("invalid choice")


        


            


    

       
    

