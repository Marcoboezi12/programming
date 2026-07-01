class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def change_phone(self, new_phone):
        self.phone = new_phone
    
    def change_email(self, new_email):
        self.email = new_email
    
    def show_info(self):
         print("name:", self.name)
         print("phone:", self.phone)
         print("email:", self.email)

marco = Contact("Marco", "8099496372", "marco@email.com")
marco.change_phone("8291112222")
marco.change_email("marqquitos@email.com")
marco.show_info()



ariel = Contact("Ariel", "8099710001", "ariel@email.com")
ariel.show_info()


