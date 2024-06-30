from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from .models import *

# @receiver(post_save, sender=Login)
# def delete_rejected_records(sender, instance, **kwargs):
#     if instance.approval_status == 'rejected':
#         instance.delete()

@receiver(post_save, sender=User)
def delete_rejected_user(sender, instance, **kwargs):
    if instance.approval_status == 'rejected':
        instance.delete()

@receiver(post_save, sender=Photographer)
def delete_rejected_photographer(sender, instance, **kwargs):
    if instance.approval_status == 'rejected':
        instance.delete()

@receiver(post_save, sender=Portfolio)
def delete_rejected_portfolio(sender, instance, **kwargs):
    if instance.approval_status == 'rejected':
        instance.delete()

@receiver(post_save, sender=Hire)
def delete_rejected_hire(sender, instance, **kwargs):
    if instance.approval_status == 'rejected':
        instance.delete()

@receiver(post_save, sender=BookingForm)
def delete_rejected_bookingform(sender, instance, **kwargs):
    if instance.approval_status == 'rejected':
        instance.delete()