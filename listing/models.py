from django.db import models

# Create your models here. this is from the django admin that you create a table from there
class Listing(models.Model):
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    sqrt = models.IntegerField()
    # image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('-created_at', )

    # constructor
    def __str__(self):
        return self.address