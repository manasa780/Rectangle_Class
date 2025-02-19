# Question 1: Django signals are executed synchronously
# Proof:
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
def signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)  # Simulating a delay to observe synchronous execution
    print("Signal finished")

# Connecting the signal handler to the post_save signal of User model
post_save.connect(signal_handler, sender=User)

# Creating a user instance
user = User.objects.create(username="test_user")  # Execution will wait for signal completion
print("User creation complete")  # This will execute only after the signal completes

