import django
from django.db import models

# Create your models here.
class Order(models.Model):
    def __str__(self):
        return f'order: time - {self.get_time()}'

class FinalOrder(models.Model):
    order_num = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=30)
    finished = models.BooleanField(default=False)
    orders = models.ManyToManyField(Order)

    def get_time(self):
        pass

    def get_price(self):
        price = 0
        for o in orders.objects.all():
            price += o.get_price()
        return price

    def __str__(self):
        return f'final order - {self.get_time()} - {self.get_price()}'

class Pasta(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price}'

class PastaOrder(Order):
    time = models.TimeField()
    order = models.ForeignKey(Pasta, on_delete=models.CASCADE)

    def get_price(self):
        return self.order.price

    def __str__(self):
        return f'order: {self.get_price()}'

class Salad(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price}'

class SaladOrder(Order):
    time = models.TimeField()
    order = models.ForeignKey(Salad, on_delete=models.CASCADE)

    def get_price(self):
        return self.order.price

    def __str__(self):
        return f'order: {self.get_price()}'

class Platter(models.Model):
    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.small_price} | {self.large_price}'

class PlatterOrder(Order):
    time = models.TimeField()
    order = models.ForeignKey(Platter, on_delete=models.CASCADE)
    size_small = models.BooleanField(default=False)

    def get_price(self):
        if self.size_small:
            return self.order.small_price
        else:
            return self.order.large_price

    def __str__(self):
        return f'order: {self.get_price()}'

class SubExtra(models.Model):
    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'sub: {self.name} - {self.small_price} | {self.large_price}'

class Sub(models.Model):
    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.small_price} | {self.large_price}'

class SubOrder(Order):
    time = models.TimeField()
    order = models.ForeignKey(Sub, on_delete=models.CASCADE)
    size_small = models.BooleanField(default=False)
    extra = models.ManyToManyField(SubExtra, blank=True)

    def get_price(self):
        price = 0
        if self.size_small:
            price = self.order.small_price
            for extra in self.extra.all():
                price += extra.small_price
        else:
            price =  self.order.large_price
            for extra in self.extra.all():
                price += extra.large_price
        return price

    def __str__(self):
        return f'order: {self.get_price()}'

class PizzaTopping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'pizza: {self.name}'

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)
    num_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.small_price} | {self.large_price}'

class RegularPizza(Pizza):
    def __str__(self):
        return f'reg: {self.name} - {self.small_price} | {self.large_price}'

class SicilianPizza(Pizza):
    def __str__(self):
        return f'sic: {self.name} - {self.small_price} | {self.large_price}'

class PizzaOrder(Order):
    time = models.TimeField()
    order = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size_small = models.BooleanField(default=False)
    toppings = models.ManyToManyField(PizzaTopping)

    def get_price(self):
        if self.size_small:
            return self.order.small_price
        else:
            return self.order.large_price

    def verify_num_toppings(self):
        if self.order.num_toppings == len(self.toppings.all()):
            return True
        else:
            return False

    def __str__(self):
        return f'order: {self.get_price()}'
