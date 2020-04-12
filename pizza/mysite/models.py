from django.db import models

# Create your models here.
class Order(models.Model):
    cust_id = models.IntegerField()
    cust_name = models.CharField(max_length=30)
    time = models.TimeField()

    def get_price(self,size):
        pass

class Pasta(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price}'

class PastaOrder(Order):
    order = models.ForeignKey(Pasta, on_delete=models.CASCADE)

    def get_price(self):
        pass

    def __str__(self):
        return f'order: {self.name} - {self.get_price()}'

class Salad(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price}'

class SaladOrder(Order):
    order = models.ForeignKey(Salad, on_delete=models.CASCADE)

    def get_price(self):
        pass

    def __str__(self):
        return f'order: {self.name} - {self.get_price()}'

class Platter(models.Model):
    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.small_price} | {self.large_price}'

class PlatterOrder(Order):
    order = models.ForeignKey(Platter, on_delete=models.CASCADE)
    size_small = models.BooleanField(default=False)

    def get_price(self):
        pass

    def __str__(self):
        return f'order: {self.name} - {self.get_price()}'

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
    order = models.ForeignKey(Sub, on_delete=models.CASCADE)
    size_small = models.BooleanField(default=False)
    extra = models.ManyToManyField(SubExtra, blank=True)

    def get_price(self,size):
        pass

    def __str__(self):
        return f'order: {self.name} - {self.get_price()}'

class PizzaTopping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'pizza: {self.name}'

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.small_price} | {self.large_price}'

class RegularPizza(Pizza):
    def __str__(self):
        return f'reg: {self.name} - {self.small_price} | {self.large_price}'

class SicilianPizza(Pizza):
    def __str__(self):
        return f'sic: {self.name} - {self.small_price} | {self.large_price}'

class PizzaOrder(Order):
    order = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size_small = models.BooleanField(default=False)
    cheese = models.BooleanField()
    toppings = models.ManyToManyField(PizzaTopping)

    def get_price(self,size):
        pass

    def __str__(self):
        return f'order: {self.name} - {self.get_price()}'
