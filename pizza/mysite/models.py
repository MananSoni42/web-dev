import django
from django.db import models
import datetime
from polymorphic.models import PolymorphicModel

def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

# Create your models here.
class Order(PolymorphicModel):
    def get_queryset(self):
        return InheritanceQuerySet(self.model).select_subclasses()

    def get_time(self):
        raise NotImplementedError('Implement me')

    def get_price(self):
        raise NotImplementedError('Implement me')

    def __str__(self):
        return 'Order'

class FinalOrder(models.Model):
    order_num = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=30)
    finished = models.BooleanField(default=False)
    orders = models.ManyToManyField(Order)

    def get_time(self):
        try:
            time_list = [o.get_time() for o in self.orders.all()]
            return max(time_list)
        except ValueError:
            return datetime.datetime.now()

    def get_price(self):
        price = 0
        for o in self.orders.all():
            print(o)
            print(o.get_price())
            price += o.get_price()
        return price

    def __str__(self):
        s = f'Final order #{self.order_num} - {self.cust_name} - {self.get_price()}'
        for o in self.orders.all():
            s += f'\n\t{o.__str__()}'
        return s

class Pasta(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pasta - {self.name} - {self.price}'

class PastaOrder(Order):
    time = models.TimeField()
    order = models.ForeignKey(Pasta, on_delete=models.CASCADE)

    @overrides(Order)
    def get_price(self):
        return self.order.price

    @overrides(Order)
    def get_time(self):
        return self.time

    @overrides(Order)
    def __str__(self):
        return f'PastaOrder: {self.get_price()}'

class Salad(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Salad: {self.name} - {self.price}'

class SaladOrder(Order):
    time = models.TimeField()
    order = models.ForeignKey(Salad, on_delete=models.CASCADE)

    @overrides(Order)
    def get_price(self):
        return self.order.price

    @overrides(Order)
    def get_time(self):
        return self.time

    @overrides(Order)
    def __str__(self):
        return f'SaladOrder: {self.get_price()}'

class Platter(models.Model):
    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Platter: {self.name} - {self.small_price} | {self.large_price}'

class PlatterOrder(Order):
    time = models.TimeField()
    order = models.ForeignKey(Platter, on_delete=models.CASCADE)
    size_small = models.BooleanField(default=False)

    @overrides(Order)
    def get_price(self):
        if self.size_small:
            return self.order.small_price
        else:
            return self.order.large_price

    @overrides(Order)
    def get_time(self):
        return self.time

    @overrides(Order)
    def __str__(self):
        return f'PlatterOrder: {self.get_price()}'

class SubExtra(models.Model):
    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'SubExtra: {self.name} - {self.small_price} | {self.large_price}'

class Sub(models.Model):
    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Sub: {self.name} - {self.small_price} | {self.large_price}'

class SubOrder(Order):
    time = models.TimeField()
    order = models.ForeignKey(Sub, on_delete=models.CASCADE)
    size_small = models.BooleanField(default=False)
    extra = models.ManyToManyField(SubExtra, blank=True)

    @overrides(Order)
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

    @overrides(Order)
    def get_time(self):
        return self.time

    @overrides(Order)
    def __str__(self):
        s = f'SubOrder: {self.get_price()}'
        for extra in self.extra.all():
            s += f'\n\t{extra.__str__()}'
        return s

class PizzaTopping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'PizzaTopping: {self.name}'

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)
    num_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.small_price} | {self.large_price}'

class RegularPizza(Pizza):
    def __str__(self):
        return f'RegularPizza: {self.name} - {self.small_price} | {self.large_price}'

class SicilianPizza(Pizza):
    def __str__(self):
        return f'SicilianPizza: {self.name} - {self.small_price} | {self.large_price}'

class PizzaOrder(Order):
    time = models.TimeField()
    order = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size_small = models.BooleanField(default=False)
    toppings = models.ManyToManyField(PizzaTopping)

    @overrides(Order)
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

    @overrides(Order)
    def get_time(self):
        return self.time

    @overrides(Order)
    def __str__(self):
        s = f'PizzaOrder: {self.get_price()}'
        for t in self.toppings.all():
            s += f'\n\t{t.name}'
        return s
