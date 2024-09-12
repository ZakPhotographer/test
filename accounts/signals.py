from .tasks import send_new_student_email, send_new_lecturer_email

def post_save_account_receiver(sender, instance=None, created=False, *args, **kwargs):
    """
    Send email notification without generating a username or password.
    """
    if created:
        if instance.is_student:
            send_new_student_email.delay(instance.pk)  # No password argument needed

        if instance.is_lecturer:
            send_new_lecturer_email.delay(instance.pk)  # No password argument needed
