from django.db import models
from django.urls import reverse

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=120) # max_length= required
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=True) # null=True, default=True

    def get_absoulte_url(self):
        return  reverse("products:product-detail", kwargs={"my_id":self.id}) #f"/products/{self.id}/"