from celery import shared_task
from django.contrib.auth import get_user_model
from core.utils import send_html_email


from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_new_student_email(student_id):
    """
    Sends a welcome email to the new student.
    """
    student = User.objects.get(pk=student_id)
    subject = 'Welcome to Our Platform'
    message = f'Hello {student.first_name},\n\nYou have successfully registered as a student.'
    send_mail(subject, message, 'admin@yourdomain.com', [student.email])

@shared_task
def send_new_lecturer_email(lecturer_id):
    """
    Sends a welcome email to the new lecturer.
    """
    lecturer = User.objects.get(pk=lecturer_id)
    subject = 'Welcome to Our Platform'
    message = f'Hello {lecturer.first_name},\n\nYou have successfully registered as a lecturer.'
    send_mail(subject, message, 'admin@yourdomain.com', [lecturer.email])



@shared_task
def send_new_lecturer_email(user_pk, password):
    user = get_user_model().objects.get(pk=user_pk)
    send_html_email(
        subject="Your Dj LMS account confirmation and credentials",
        recipient_list=[user.email],
        template="accounts/email/new_lecturer_account_confirmation.html",
        context={"user": user, "password": password},
    )
