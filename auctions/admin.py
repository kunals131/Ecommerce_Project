from django.contrib import admin

from .models import User, Comment, Category, Item_Listing, Bid
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item_Listing)
admin.site.register(Comment)