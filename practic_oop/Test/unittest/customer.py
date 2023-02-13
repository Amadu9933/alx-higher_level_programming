#!/usr/bin/env python3



class Customer:

    discount = 0.95



    def __init__(self, first_name, last_name, purchase):

        self.first_name = first_name

        self.last_name = last_name

        self._purchase = purchase



    @property

    def customer_mail(self):

        return f'{self.first_name}.{self.last_name}@email.com'



    @property

    def customer_full_name(self):

        return f"{self.first_name} {self.last_name}"



    @property

    def purchase(self):

        return self._purchase



    @purchase.setter

    def purchase(self, value):

        self._purchase = int(value * self.discount)


