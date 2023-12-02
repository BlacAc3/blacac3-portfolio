from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Book_shelf),
admin.site.register(Collection_name),
admin.site.register(Collection),
admin.site.register(Notes),
admin.site.register(Book_reviews),