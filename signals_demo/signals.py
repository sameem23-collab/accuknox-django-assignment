import threading
import time

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Student


@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):

    if created:
        print("Signal started")

        # Q1: Check synchronous execution
        print("Signal is executing synchronously")

        # Q2: Check thread ID
        print("Receiver thread ID:", threading.get_ident())

        # Q3: Check transaction status
        print(
            "Signal transaction:",
            transaction.get_connection().in_atomic_block
        )

        time.sleep(3)

        print("Signal completed")