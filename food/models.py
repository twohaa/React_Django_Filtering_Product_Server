from django.db import models


class Food(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    # image = models.ImageField(upload_to='food/images', default="")
    pub_date = models.DateField()
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
