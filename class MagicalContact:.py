class MagicalContact:
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def describe(self):
        print(f"Name: {self.__name}, Email: {self.__email}, Phone: {self.__phone_number}")


class WizardOrWitch(MagicalContact):
    def __init__(self, name, email, phone_number, wand, house):
        super().__init__(name, email, phone_number)
        self.__wand = wand
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.__house = house

    def get_wand(self):
        return f"{self.__wand['length']} inches, {self.__wand['wood']}, {self.__wand['core']}"

    def get_house(self):
        return self.__house

    def describe(self):
        super().describe()
        print(f"Wand: {self.get_wand()}")
        print(f"House: {self.__house}")


class MagicalCreature(MagicalContact):
    def __init__(self, name, email, phone_number, species, is_tame):
        super().__init__(name, email, phone_number)
        self.__species = species
        self.__is_tame = is_tame

    def get_species(self):
        return self.__species

    def is_tame(self):
        return self.__is_tame

    def describe(self):
        super().describe()
        print(f"Species: {self.__species}")
        print(f"Tame: {self.__is_tame}")


class MagicalContactBook:
    def __init__(self):
        self.__contacts = []

    def add_contact(self, contact):
        self.__contacts.append(contact)

    def list_contacts(self):
        for contact in self.__contacts:
            contact.describe()

    def find_contact(self, name):
        for contact in self.__contacts:
            if contact.get_name() == name:
                return contact.describe()
        return "Contact not found"



if __name__ == "__main__":
    contact_book = MagicalContactBook()

  
    harry_potter = WizardOrWitch("Harry Potter", "harry@hogwarts.edu", "123-456-7890", {"core": "phoenix feather", "wood": "holly", "length": "11 inches"}, "Gryffindor")
    hermione_granger = WizardOrWitch("Hermione Granger", "hermione@hogwarts.edu", "987-654-3210", {"core": "dragon heartstring", "wood": "vine", "length": "10.75 inches"}, "Gryffindor")
    buckbeak = MagicalCreature("Buckbeak", "buckbeak@hogwarts.edu", "555-555-5555", "Hippogriff", False)

    
    contact_book.add_contact(harry_potter)
    contact_book.add_contact(hermione_granger)
    contact_book.add_contact(buckbeak)


    contact_book.list_contacts()


    print(contact_book.find_contact("Harry Potter"))