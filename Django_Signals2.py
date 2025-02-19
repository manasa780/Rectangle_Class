# Question 2: Django signals run in the same thread as the caller
# Proof:
import threading
def signal_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# Connecting the signal handler to the post_save signal of User model
post_save.connect(signal_handler, sender=User)

# Printing the main thread name before creating a user
print(f"Main thread: {threading.current_thread().name}")
user = User.objects.create(username="test_user")  # The signal should run in the same thread
