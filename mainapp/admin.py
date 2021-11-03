from django.contrib import admin
from django.db.models.lookups import In
from .models import (
    Inqury,
    Feedback,
    Response
)

# Register your models here.
admin.site.register(Inqury)
admin.site.register(Feedback)
admin.site.register(Response)