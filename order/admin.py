from django.contrib import admin
from .models import Order,OrderItem
# Register your models here.

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['email','city','postal_code','created_at','updated_at','paid']
    list_filter = ['created_at','updated_at']
    list_per_page = 100
    list_editable = ['paid']
    list_display_links = ['email']
    inlines = [OrderItemAdmin]


