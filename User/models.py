from django.db import models
from django.contrib.auth.models import User

class UserType(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    usertype = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usertype')

    def __str__(self):
        return f"{self.user.username} - {self.usertype}"
