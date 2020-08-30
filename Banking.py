
class Banking():
    def __init__(self, balance=100):
        self.balance = balance
        print("\nWelcome to the ATM Deopsit and Withdrawal Machine!")
    def machine(self):
        data=self.usage()
        if data == True:
            self.deposit()
            self.display()
        else:
            self.withdraw()    
            self.display()
       
            
    def usage(self):
        print('\nDo you want to Deposit (Press d) or Withdraw (Press w)??')
        return input().lower().startswith('d')
        
    def withdraw(self):
        try:
            amount = float(input("the amount you like withdraw: "))
            if self.balance >= amount:
                self.balance -= amount
                print("\n The amount you withdrawed is " + str(amount))
            else:
                print("\n Insufficient fund!")
        except ValueError:
            print("Please Enter a Valied Number")    
            self.withdraw()    

    def deposit(self):
        try:
            amount = float(input("the amount you like to Deposit: "))
            self.balance += amount
            print ("\n The amount you Deposited is: " + str (amount))
        except ValueError:
            print("Please Enter a Valied Number")    
            self.deposit()    
    def display(self):
        print("\n The amount balance is: ", self.balance)

if __name__ == "__main__":
    g=Banking()
    g.machine()
