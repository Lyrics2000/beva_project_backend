from django.contrib import admin
from django.db.models.lookups import In
from .models import (
    Inqury,
    Feedback,
    Response,
    ComplaintsDetails,
    FollowUpEmailss
)

# Register your models here.
admin.site.register(Inqury)
admin.site.register(Feedback)
admin.site.register(Response)
admin.site.register(ComplaintsDetails)
admin.site.register(FollowUpEmailss)