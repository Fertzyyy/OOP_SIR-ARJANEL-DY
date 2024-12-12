class Phone:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

def display_phones(phones):
    if not phones:
        print("No phones available.")
    for idx, phone in enumerate(phones, start=1):
        print(f"{idx}. {phone}")

def main_menu():
    phones = []
    while True:
        print("\nMain Menu:")
        print("1. Create Phone")
        print("2. Modify Phone")
        print("3. Delete Phone")
        print("4. View Phones")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            year = input("Enter year: ")
            phones.append(Phone(brand, model, year))
            print("Phone added.")

        elif choice == '2':
            display_phones(phones)
            idx = int(input("Enter the number of the phone to modify: ")) - 1
            if 0 <= idx < len(phones):
                brand = input("Enter new brand (leave blank to keep current): ")
                model = input("Enter new model (leave blank to keep current): ")
                year = input("Enter new year (leave blank to keep current): ")
                phone = phones[idx]
                phone.brand = brand if brand else phone.brand
                phone.model = model if model else phone.model
                phone.year = year if year else phone.year
                print("Phone updated.")
            else:
                print("Invalid selection.")

        elif choice == '3':
            display_phones(phones)
            idx = int(input("Enter the number of the phone to delete: ")) - 1
            if 0 <= idx < len(phones):
                phones.pop(idx)
                print("Phone deleted.")
            else:
                print("Invalid selection.")

        elif choice == '4':
            display_phones(phones)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
