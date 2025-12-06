from django.contrib import admin
from .models import Category,productinfo, offerinfo  
# import your model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(productinfo)
admin.site.register(offerinfo)