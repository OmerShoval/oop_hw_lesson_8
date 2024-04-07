from models.Customer import *
from overrides import overrides


class PersonalCustomer(Costumer):
    def __init__(self, name, payment, id, bank_name, credit_card_number, amount_of_money):
        super().__init__(name, payment, id, bank_name, credit_card_number, amount_of_money)

    def make_payment(self, amount):
        if amount <= self.amount_of_money:
            self.amount_of_money -= amount
            return True
        return False

    def get_payment(self, salary):
        if salary >= 1:
            self.amount_of_money += salary
        else:
            print(f"Your salary is bellow the permitted amount for deposit. "
                  f"your current balance is "
                  f"{self.amount_of_money}")
