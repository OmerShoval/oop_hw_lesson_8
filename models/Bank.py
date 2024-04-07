from enum import Enum
from abc import *
from overrides import *

from models import Customer


class Bank(ABC):
    def __init__(self, bank_id, bank_name, bank_number_of_employees,
                 bank_amount_of_revenue, bank_amount_of_expenses):
        self.bank_id = bank_id
        self.bank_name = bank_name
        self.bank_number_of_employees = bank_number_of_employees
        self.bank_amount_of_revenue = bank_amount_of_revenue
        self.bank_amount_of_expenses = bank_amount_of_expenses
        self.customer = []

    @abstractmethod
    def add_customer(self, customer):
        self.customer.append(customer)

    @abstractmethod
    def take_payment(self, customer: Customer):
        pass

    @abstractmethod
    def increase_revenue(self, revenue):
        pass

    @abstractmethod
    def increase_expense(self, expenses_to_add):
        self.bank_amount_of_expenses += expenses_to_add
        print(f"the expenses are {self.bank_amount_of_expenses}")

    @abstractmethod
    def calculate_customer_money(self):
        pass
