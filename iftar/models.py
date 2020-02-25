from django.db import models
from django.urls import reverse
import datetime
import uuid

# Create your models here.
class Need (models.Model):
#    id= models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    description = models.CharField(max_length=300)
    display_order = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class Donation (models.Model):
#    id= models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    description = models.CharField(max_length=300)
    display_order = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class Donor (models.Model):
    need = models.OneToOneField(Need, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    donation = models.ForeignKey('Donation', on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('iftar:index')

class Mosque(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    donor_page_message = models.CharField(max_length=500)
    schedule_page_message = models.CharField(max_length=500)
    schedule_page_title = models.CharField(max_length=100)
    donor_page_title = models.CharField(max_length=100)
    donor_menu_button = models.CharField(max_length=20)
    schedule_menu_button = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Mosque'


    def __str__(self):
        return self.name

