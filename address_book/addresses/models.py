from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField('Client Email')
    phone = models.CharField('Phone Number', blank=True, max_length=20)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Address(models.Model):
    address = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE)
    street_name = models.CharField('Street Name', max_length=100)
    street_number = models.CharField('Street Number', max_length=10)
    city = models.CharField('City', max_length=50)
    zip_code = models.CharField('Zip Code', max_length=15)
    country = models.CharField('Country', max_length=50)

    def __str__(self):
        return self.street_name + ' ' + self.city
