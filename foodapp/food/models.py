from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.TextField(max_length=1000)
    item_price = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name + ' ' + self.item_desc + ': ' + str(self.item_price)
