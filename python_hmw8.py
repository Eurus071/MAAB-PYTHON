"""
Farm Model Implementation
"""

class Animal:
    
    def __init__(self, name, age, species, sound):
        self.name = name
        self.age = age
        self.species = species
        self.sound = sound
        self.is_hungry = True
        self.is_asleep = False
    
    def eat(self, food):
     
        if not self.is_asleep:
            self.is_hungry = False
            return f"{self.name} the {self.species} is eating {food}."
        return f"{self.name} is sleeping and can't eat right now."
    
    def sleep(self):
        self.is_asleep = True
        return f"{self.name} the {self.species} is now sleeping."
    
    def wake_up(self):
        self.is_asleep = False
        return f"{self.name} the {self.species} has woken up."
    
    def make_sound(self):
        if not self.is_asleep:
            return f"{self.name} says: {self.sound}!"
        return f"Shhh... {self.name} is sleeping."
    
    def __str__(self):
        status = "sleeping" if self.is_asleep else "awake"
        hunger = "hungry" if self.is_hungry else "full"
        return f"{self.name} ({self.species}, {self.age} years old) - Status: {status}, Hunger: {hungry}"


class Cow(Animal):
    
    def __init__(self, name, age, milk_production):
        super().__init__(name, age, "Cow", "Moo")
        self.milk_production = milk_production  
        self.has_been_milked = False
    
    def produce_milk(self):
        if not self.has_been_milked and not self.is_hungry:
            self.has_been_milked = True
            return f"{self.name} produced {self.milk_production} liters of milk!"
        elif self.is_hungry:
            return f"{self.name} is too hungry to produce milk. Feed her first!"
        return f"{self.name} has already been milked today."
    
    def graze(self):
        if not self.is_asleep:
            self.is_hungry = False
            return f"{self.name} is grazing in the pasture."
        return f"{self.name} is sleeping and can't graze."


class Chicken(Animal):
    def __init__(self, name, age, egg_production):
        super().__init__(name, age, "Chicken", "Cluck cluck")
        self.egg_production = egg_production  # eggs per week
        self.eggs_today = 0
    
    def lay_egg(self):
        if not self.is_asleep and not self.is_hungry:
            self.eggs_today += 1
            return f"{self.name} laid an egg! Total today: {self.eggs_today}"
        elif self.is_hungry:
            return f"{self.name} needs to eat before laying eggs!"
        return f"{self.name} is sleeping and can't lay eggs."
    
    def scratch_ground(self):
        if not self.is_asleep:
            return f"{self.name} is scratching the ground for worms and seeds."
        return f"{self.name} is sleeping and can't scratch."


class Sheep(Animal):
    
    def __init__(self, name, age, wool_length):
        super().__init__(name, age, "Sheep", "Baa")
        self.wool_length = wool_length  # in centimeters
        self.has_been_sheared = False
    
    def grow_wool(self):
        if not self.is_hungry:
            self.wool_length += 0.5
            return f"{self.name}'s wool grew to {self.wool_length:.1f} cm."
        return f"{self.name} needs to eat for wool to grow!"
    
    def shear(self):
        if not self.has_been_sheared and self.wool_length >= 5:
            wool_amount = self.wool_length
            self.wool_length = 0
            self.has_been_sheared = True
            return f"Sheared {self.name}! Got {wool_amount:.1f} cm of wool."
        elif self.wool_length < 5:
            return f"{self.name}'s wool is only {self.wool_length:.1f} cm. Too short to shear!"
        return f"{self.name} has already been sheared this season."


class Pig(Animal):
    
    def __init__(self, name, age, weight):
        super().__init__(name, age, "Pig", "Oink oink")
        self.weight = weight  # in kilograms
        self.is_muddy = False
    
    def roll_in_mud(self):
        if not self.is_asleep:
            self.is_muddy = True
            return f"{self.name} is happily rolling in the mud!"
        return f"{self.name} is sleeping and can't roll in mud."
    
    def get_clean(self):
        if self.is_muddy:
            self.is_muddy = False
            return f"{self.name} has been cleaned and is no longer muddy."
        return f"{self.name} is already clean."


def demonstrate_farm():
    """Demonstrate the farm model with various animals and their behaviors"""
    print("=" * 50)
    print("FARM DEMONSTRATION")
    print("=" * 50)
    
    daisy = Cow("Daisy", 4, 8.5)
    cluckers = Chicken("Cluckers", 2, 5)
    wooly = Sheep("Wooly", 3, 7.2)
    piggy = Pig("Piggy", 1, 50)
    
    animals = [daisy, cluckers, wooly, piggy]
    
    print("\nAnimals on the farm:")
    for animal in animals:
        print(f"  - {animal}")
    print("\n--- Morning Activities ---")
    
    for animal in animals:
        print(animal.wake_up())
    
    print("\nFeeding time:")
    print(daisy.eat("grass"))
    print(cluckers.eat("grains"))
    print(wooly.eat("hay"))
    print(piggy.eat("slop"))
    
    print("\n--- Animal-specific Activities ---")
    print(daisy.produce_milk())
    print(cluckers.lay_egg())
    print(cluckers.lay_egg())
    print(wooly.grow_wool())
    print(piggy.roll_in_mud())
    
    print("\n--- Farm Sounds ---")
    for animal in animals:
        print(animal.make_sound())
    
    print("\n--- Evening Activities ---")
    print(daisy.sleep())
    print(wooly.sleep())
    
    print("\nFarm status:")
    for animal in animals:
        print(f"  - {animal}")


if __name__ == "__main__":
    demonstrate_farm()

###################################################################################################
###################################################################################################


"""
Bank Application Implementation
"""
import json
import os
import random


class Account:
    
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def to_dict(self):
        return {
            'account_number': self.account_number,
            'name': self.name,
            'balance': self.balance
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['account_number'], data['name'], data['balance'])
    
    def __str__(self):
        return f"Account: {self.account_number}\nHolder: {self.name}\nBalance: ${self.balance:.2f}"


class Bank:
    
    def __init__(self, filename='accounts.json'):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()
    
    def generate_account_number(self):
        while True:
            account_num = str(random.randint(10000000, 99999999))
            if account_num not in self.accounts:
                return account_num
    
    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            return None, "Initial deposit cannot be negative"
        
        account_number = self.generate_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        return account_number, f"Account created successfully! Your account number is: {account_number}"
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account, None
        return None, "Account not found!"
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            return False, "Account not found!"
        
        if amount <= 0:
            return False, "Deposit amount must be positive!"
        
        if account.deposit(amount):
            self.save_to_file()
            return True, f"Successfully deposited ${amount:.2f}. New balance: ${account.balance:.2f}"
        return False, "Deposit failed!"
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            return False, "Account not found!"
        
        if amount <= 0:
            return False, "Withdrawal amount must be positive!"
        
        if amount > account.balance:
            return False, "Insufficient funds!"
        
        if account.withdraw(amount):
            self.save_to_file()
            return True, f"Successfully withdrew ${amount:.2f}. New balance: ${account.balance:.2f}"
        return False, "Withdrawal failed!"
    
    def save_to_file(self):
        try:
            data = {
                'accounts': {
                    acc_num: account.to_dict()
                    for acc_num, account in self.accounts.items()
                }
            }
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False
    
    def load_from_file(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                
                self.accounts = {
                    acc_num: Account.from_dict(account_data)
                    for acc_num, account_data in data.get('accounts', {}).items()
                }
                return True
        except Exception as e:
            print(f"Error loading from file: {e}")
        
        return False
    
    def get_total_balance(self):
        return sum(account.balance for account in self.accounts.values())


class BankApp:
    
    def __init__(self):
        self.bank = Bank()
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "=" * 40)
        print("BANK APPLICATION")
        print("=" * 40)
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. View All Accounts")
        print("6. Bank Statistics")
        print("7. Exit")
        print("=" * 40)
    
    def create_account_flow(self):
        print("\n--- Create New Account ---")
        name = input("Enter your full name: ").strip()
        
        while True:
            try:
                initial_deposit = float(input("Enter initial deposit amount: $"))
                if initial_deposit >= 0:
                    break
                print("Initial deposit cannot be negative!")
            except ValueError:
                print("Please enter a valid number!")
        
        account_number, message = self.bank.create_account(name, initial_deposit)
        print(f"\n{message}")
    
    def view_account_flow(self):
        print("\n--- View Account ---")
        account_number = input("Enter account number: ").strip()
        
        account, error = self.bank.view_account(account_number)
        if error:
            print(f"Error: {error}")
        else:
            print("\nAccount Details:")
            print("-" * 30)
            print(account)
    
    def deposit_flow(self):
        print("\n--- Deposit Money ---")
        account_number = input("Enter account number: ").strip()
        
        while True:
            try:
                amount = float(input("Enter deposit amount: $"))
                if amount > 0:
                    break
                print("Amount must be positive!")
            except ValueError:
                print("Please enter a valid number!")
        
        success, message = self.bank.deposit(account_number, amount)
        print(f"\n{message}")
    
    def withdraw_flow(self):
        print("\n--- Withdraw Money ---")
        account_number = input("Enter account number: ").strip()
        
        while True:
            try:
                amount = float(input("Enter withdrawal amount: $"))
                if amount > 0:
                    break
                print("Amount must be positive!")
            except ValueError:
                print("Please enter a valid number!")
        
        success, message = self.bank.withdraw(account_number, amount)
        print(f"\n{message}")
    
    def view_all_accounts(self):
        print("\n--- All Accounts ---")
        
        if not self.bank.accounts:
            print("No accounts found!")
            return
        
        total_balance = 0
        for account_number, account in self.bank.accounts.items():
            print("\n" + "-" * 30)
            print(f"Account #: {account_number}")
            print(f"Holder: {account.name}")
            print(f"Balance: ${account.balance:.2f}")
            total_balance += account.balance
        
        print("\n" + "=" * 30)
        print(f"Total Accounts: {len(self.bank.accounts)}")
        print(f"Total Bank Balance: ${total_balance:.2f}")
    
    def bank_statistics(self):
        print("\n--- Bank Statistics ---")
        print(f"Total Accounts: {len(self.bank.accounts)}")
        print(f"Total Bank Balance: ${self.bank.get_total_balance():.2f}")
        
        if self.bank.accounts:
            avg_balance = self.bank.get_total_balance() / len(self.bank.accounts)
            print(f"Average Account Balance: ${avg_balance:.2f}")
            
            # Find richest account
            richest = max(self.bank.accounts.values(), key=lambda acc: acc.balance)
            print(f"\nRichest Account Holder: {richest.name}")
            print(f"Balance: ${richest.balance:.2f}")
    
    def run(self):
        self.clear_screen()
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-7): ").strip()
                
                if choice == '1':
                    self.create_account_flow()
                elif choice == '2':
                    self.view_account_flow()
                elif choice == '3':
                    self.deposit_flow()
                elif choice == '4':
                    self.withdraw_flow()
                elif choice == '5':
                    self.view_all_accounts()
                elif choice == '6':
                    self.bank_statistics()
                elif choice == '7':
                    print("\nThank you for using our banking services!")
                    print("Goodbye!")
                    break
                else:
                    print("\nInvalid choice! Please enter a number between 1 and 7.")
                
                input("\nPress Enter to continue...")
                self.clear_screen()
                
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                break
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                input("\nPress Enter to continue...")
                self.clear_screen()


def demo_bank_app():
    print("=" * 50)
    print("BANK APPLICATION DEMONSTRATION")
    print("=" * 50)
    
    bank = Bank('demo_accounts.json')
    
    print("\nCreating sample accounts...")
    bank.create_account("John Doe", 1000.00)
    bank.create_account("Jane Smith", 2500.50)
    bank.create_account("Bob Johnson", 500.00)
    
    print("\n--- Demonstrating Operations ---")
    
    john_account = None
    for acc_num, account in bank.accounts.items():
        if account.name == "John Doe":
            john_account = acc_num
            break
    
    if john_account:
        print(f"\n1. Viewing John's account:")
        account, _ = bank.view_account(john_account)
        print(account)
        
        print(f"\n2. John deposits $500:")
        success, message = bank.deposit(john_account, 500)
        print(message)
        
        print(f"\n3. John withdraws $200:")
        success, message = bank.withdraw(john_account, 200)
        print(message)
        
        print(f"\n4. Final account status:")
        account, _ = bank.view_account(john_account)
        print(account)
    
    print("\n5. All accounts in the bank:")
    for acc_num, account in bank.accounts.items():
        print(f"\nAccount #{acc_num}:")
        print(f"  Holder: {account.name}")
        print(f"  Balance: ${account.balance:.2f}")
    
    print(f"\nTotal bank balance: ${bank.get_total_balance():.2f}")

if __name__ == "__main__":
    print("Which application would you like to run?")
    print("1. Farm Model")
    print("2. Bank Application (Interactive)")
    print("3. Bank Application (Demonstration)")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '1':
        demonstrate_farm()
    elif choice == '2':
        app = BankApp()
        app.run()
    elif choice == '3':
        demo_bank_app()
    else:
        print("Invalid choice! Running farm model...")
        demonstrate_farm()