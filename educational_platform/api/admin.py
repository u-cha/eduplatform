from django.contrib import admin
from .models import User, Lesson, Product, WatchStatus, Access

# Register your models here.

admin.site.register(User)
admin.site.register(Lesson)
admin.site.register(Product)
admin.site.register(WatchStatus)
admin.site.register(Access)

