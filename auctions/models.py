from typing import List
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import FloatField
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"

class Item_Listing(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to = "images/")
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    desc = models.CharField(null = True, max_length=120)
    startingbid = models.FloatField()
    currentbid = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Similar_names")
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name="All_created_listings")
    watcher = models.ManyToManyField(User, blank=True, related_name="watched_listings")
    buyer = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.title} : {self.startingbid}"

class Bid(models.Model):
    item = models.ForeignKey(Item_Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.FloatField()
    date = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="All_Comments")
    created_date = models.DateTimeField(auto_now=True)
    listing = models.ForeignKey(Item_Listing, on_delete=models.CASCADE,related_name="get_comments")

    

