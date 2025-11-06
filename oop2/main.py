# инкапсуляция выполнение практических заданий от AI
class BankAccount:

    def __init__(self,account_Number: int, initial_balance: float = 0):
        self.__balance = initial_balance
        self.__account_number = account_Number
        self.__is_active = True

    def get_balance(self):
        return f"баланс: {self.__balance} RUB"

    def deposit(self, amount: float):
        if self.__is_active:
            if amount >= 0:
                self.__balance += amount
                print(f"Пополнение на {amount} руб. \nНовый баланс: {self.__balance} руб.")
        else:
            print("счёт не доступен!!!")

    def withdraw(self, amount: float):
        if self.__is_active == True and amount >= 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"снятие средств на {amount} руб. \nНовый баланс: {self.__balance} руб.")
            else:
                print("сумма превышает количество средств на счету!!!")
        else:
            print("не возможно снять средства")


if __name__ == '__main__':
    purse = BankAccount(account_Number=1, initial_balance=10)
    print(purse.get_balance())
    purse.withdraw(10)


