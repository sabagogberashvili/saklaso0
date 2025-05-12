from django.contrib import admin
from .models import Food, Drink, Order

class OrderInline(admin.TabularInline):
    model = Order
    fields = ('food', 'drink', 'costumer_email')
    readonly_fields = ('food', 'drink', 'costumer_email')
    can_delete = False
    extra = 0
    show_change_link = True

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj =None):
        return False
    

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    inlines = [OrderInline]

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    inlines = [OrderInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('food', 'drink', 'costumer_email')
    list_filter = ('food', 'drink', 'costumer_email')

