from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Product, Review

# Unregister and re-register User (if customizing)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register Product with custom admin display
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)

# Register Review with custom admin display
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'rating', 'created_at')
    search_fields = ('product__name', 'user__username')
    list_filter = ('rating', 'created_at')
