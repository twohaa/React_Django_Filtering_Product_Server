from django.db import models


class User(models.Model):
    id = models.AutoField
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=50, default="")
    status = models.BooleanField(default=True)
    # image = models.ImageField(upload_to='food/images', default="")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
