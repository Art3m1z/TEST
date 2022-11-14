from django.contrib.auth.models import AbstractUser
from django.db import models


class Manager(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)

    USERNAME_FIELD = ['username']
    REQUIRED_FIELDS = []

    def get_full_name(self):
        if self.middle_name is not None:
            return f'{self.last_name} {self.first_name} {self.middle_name}'
        else:
            return f'{self.last_name} {self.first_name}'
