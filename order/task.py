from django.core.mail import send_mail
from .models import Order

def order_create(order_id):
    """
    send an email notification when an order is
    successfully created
    """
    order = Order.objects.get(id = order_id)
    subject = f'Order Number {order.id}'
    message = f'Dear {order.first_name}\n You have successfully placed an order.\n Your order id is {order.id}'
    mail_sent = send_mail(subject,message,"admin@admin.com",[order.email])

    return mail_sent