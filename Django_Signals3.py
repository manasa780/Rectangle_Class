# Question 3: Django signals run in the same database transaction as the caller
# Proof:
from django.db import transaction
def signal_handler(sender, instance, **kwargs):
    # Checking if the user exists in the database inside the signal
    print(f"Signal: user exists in DB? {User.objects.filter(id=instance.id).exists()}")

# Connecting the signal handler to the post_save signal of User model
post_save.connect(signal_handler, sender=User)

# Using a database transaction block
with transaction.atomic():
    user = User.objects.create(username="test_user")
    # Checking if the user exists in the database in the caller context
    print(f"Caller: user exists in DB? {User.objects.filter(id=user.id).exists()}")
