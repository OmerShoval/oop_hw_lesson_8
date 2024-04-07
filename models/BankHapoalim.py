from abc import *
from models.Bank import *
from overrides import overrides


class BankHapoalim(Bank):

    def __init__(self, bank_id, bank_name, bank_number_of_employees,
                 bank_amount_of_revenue, bank_amount_of_expenses,
                 revenue):

        super().__init__(bank_id, bank_name, bank_number_of_employees,
                         bank_amount_of_revenue, bank_amount_of_expenses)

        self.customer = []
        self.revenue = revenue

    @overrides
    def add_customer(self, customer):
        self.customer.append(customer)

    @overrides
    def take_payment(self, customer: Customer):
        if customer in self.customer:
            print(f"Customer needs to pay {customer.payment}")

    @overrides
    def increase_revenue(self, revenue):
        self.revenue += revenue
        print(f"the current revenue is {self.revenue}")

    @overrides
    def increase_expense(self, expenses_to_add):
        self.bank_amount_of_expenses += expenses_to_add
        print(f"the expenses are {self.bank_amount_of_expenses}")

    @overrides
    def calculate_customer_money(self):
        total_customer_payments = sum(customer.payment for customer in self.customer)
        total_revenue = self.revenue + total_customer_payments
        print(f"The total revenue including customer payments is: {total_revenue}")
        return total_revenue







