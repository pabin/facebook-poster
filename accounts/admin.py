from django.contrib import admin

from .models import (
    FacebookPageID,
    FacebookAccessToken,
)


admin.site.register(FacebookPageID)
admin.site.register(FacebookAccessToken)
