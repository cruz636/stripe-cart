from django.db import models
from django_lifecycle import LifecycleModel, hook, BEFORE_CREATE

from .helpers import authorization, create_product

# Create your models here.


class Item(LifecycleModel, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="365 Item.")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stripe_url = models.CharField(blank=True, max_length=250)
    authorized = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    @hook(BEFORE_CREATE)
    def set_stripe_payment_link(self):
        if self.stripe_url != "":
            self.authorized = True
            return
        self.stripe_url = create_product(name=self.name, price=self.price)
        self.authorized = False
