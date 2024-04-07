from abc import *


class Costumer(ABC):
    def __init__(self, name, payment, id, bank_name, credit_card_number, amount_of_money):
        self.name = name
        self.payment = payment
        self.id = id
        self.bank_name = bank_name
        self.credit_card_number = credit_card_number
        self.amount_of_money = amount_of_money

    @abstractmethod
    def get_payment(self, salary):
        if salary >= 1:
            self.amount_of_money += salary
        else:
            print(f"Your salary is bellow the permitted amount for deposit. "
                  f"your current balance is "
                  f"{self.amount_of_money}")
