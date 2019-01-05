from django.contrib import admin
from mainsite import models

# Register your models here.

admin.site.register(models.Location_set)
admin.site.register(models.Job_list)
admin.site.register(models.User)