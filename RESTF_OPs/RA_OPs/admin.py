from django.contrib import admin
from .models import Crudp, address, job


admin.site.register(Crudp)
admin.site.register(job)
admin.site.register(address)
