from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.mail import send_mail

# Create your models here.
class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
    gender = models.CharField(max_length=50, default=Gender.MALE, choices=Gender.choices)
    is_online = models.BooleanField(default=False)
    image = models.FileField(upload_to='products/' , null=True, blank=True)
    @property
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    def __str__(self):
        return self.get_full_name
    
    def __str__(self) -> str:
        
        return super().__str__()