from django.db import models


class Table(models.Model):
    total = models.FloatField(default=0, verbose_name="Table Total Amount", null=True)
    rezerve = models.BooleanField(default=False)
