from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    costumer_email = models.EmailField()

    def __str__(self):
        return f"{self.costumer_email} - {self.food.name} + {self.drink.name}"
    
    def price(self):
        return self.food.price + self.drink.price
    price.short_description = 'Total Price'