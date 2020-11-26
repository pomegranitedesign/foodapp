from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    item_name = models.CharField(max_length=200)
    item_desc = models.TextField(max_length=1000)
    item_price = models.IntegerField(default=0)
    item_image = models.CharField(
        max_length=500, default='https://shahpourpouyan.com/wp-content/uploads/2018/10/orionthemes-placeholder-image-1.png')

    def __str__(self):
        return self.item_name + ' ' + self.item_desc + ': ' + str(self.item_price)

    def get_absolute_url(self):
        return reverse("food:item_detials", kwargs={"pk": self.pk})
