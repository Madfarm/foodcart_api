from django.db import models





# Note to future Anthony, migrations have not been made



# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey('Cart', related_name='menu', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)