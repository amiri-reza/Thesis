from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUsersManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError("You must provide a username")
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)


class Users(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)



    

