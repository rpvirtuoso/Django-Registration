from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from users.models import CustomUser


@receiver(pre_save, sender=CustomUser)
def pre_save_checker(sender, instance, **kwargs):
    print("The pre-save object is :")
    print(instance)


@receiver(post_save, sender=CustomUser)
def post_save_checker(sender, instance, **kwargs):
    print("The post-save object is :")
    print(instance)
