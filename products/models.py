from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max field must be declared
    description = models.TextField(blank=True, null=True) #can be null or blank
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default='This is summary')
    featured = models.BooleanField(default=True) #null = True , default = True

    def get_absolute_url(self):
        return f"/product/{self.id}/"