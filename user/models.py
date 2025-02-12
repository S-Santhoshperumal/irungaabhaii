from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)  # Store hashed password
    emailid = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username
