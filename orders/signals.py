from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail


@receiver(post_save, sender=Order)
def send_order_confirmation(sender, instance, created, **kwargs):
    if created:
        subject = 'Order Confirmation'
        message = f'Thank you for your order! Your order details are:\nFood: {instance.food}\nDrink: {instance.drink} \nprice: {instance.food.price + instance.drink.price}'
        from_email = 'shreks@delivery.ge'
        recipient_list = [instance.costumer_email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)


