from django.shortcuts import render
from django.contrib.auth.models import User


def custom_invitations(request):
    email = "karan@gmail.com"
    try:
          user = User.objects.get(email=email)
    except User.DoesNotExist:
            user = User.objects.create(email=email,
                password=User.objects.make_random_password())
            user.is_active = False
            user.save()
            send_invitation(user)
       
