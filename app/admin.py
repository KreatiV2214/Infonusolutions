from django.contrib import admin
from .models import productinfo, offerinfo  
# import your model

admin.site.register(productinfo)
admin.site.register(offerinfo)