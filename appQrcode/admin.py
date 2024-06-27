from django.contrib import admin
from .models import Qrcode

# Register your models here.
@admin.register(Qrcode)
class QrcodeModelAdmin(admin.ModelAdmin):
    list_display = ('data', 'qr_code')