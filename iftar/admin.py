from django.contrib import admin
from .models import Donor, Need, Donation, Mosque
# Register your models here.

admin.site.register(Donor)
admin.site.register(Donation)
admin.site.register(Need)
admin.site.register(Mosque)