#main function for sending email 
from django.core.mail import send_mail
from django.conf import settings

#----------------------------->   this the main function for sending mail.anywhere we can use this function 
send_mail(
        'Verify  Email',                               #-->  subject
        f'Click to verify the email\n{verify_url}',    #-->  content or message
        settings.EMAIL_HOST_USER,                      #-->  email host_user
        [mail]                                         #-->  to (reciver mail id)
)
