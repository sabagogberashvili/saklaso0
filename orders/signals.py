from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, send_mass_mail
from .models import Order, Food, Drink

@receiver(post_save, sender=Order)
def send_order_confirmation(sender, instance, created, **kwargs):
    if created:
        subject = 'Order Confirmation'
        message = f'Thank you for your order!\n\nOrder Details:\nFood: {instance.food}\nDrink: {instance.drink}\nPrice: {instance.price}'
        from_email = 'shreks@delivery.ge'
        recipient_list = [instance.customer_email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

@receiver(post_save, sender=Food)
def notify_new_food(sender, instance, created, **kwargs):
    if created:
        orders = Order.objects.all()
        recipients = set(order.customer_email for order in orders)
        if recipients:
            from_email = 'shreks@delivery.ge'
            subject = 'New Food Added!'
            message = f'New food added: {instance.name} for {instance.price} '

            datatuple = [
                (subject, message, from_email, [email]) for email in recipients
            ]
            send_mass_mail(datatuple, fail_silently=True)

@receiver(post_save, sender=Drink)
def notify_new_drink(sender, instance, created, **kwargs):
    if created:
        orders = Order.objects.all()
        recipients = set(order.customer_email for order in orders)
        if recipients:
            from_email = 'shreks@delivery.ge'
            subject = 'New Drink Added!'
            message = f'New drink added: {instance.name} for {instance.price}'

            datatuple = [
                (subject, message, from_email, [email]) for email in recipients
            ]
            send_mass_mail(datatuple, fail_silently=True)
