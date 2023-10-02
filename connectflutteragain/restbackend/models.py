import os
from django.db import models


def play_area_image_upload(instance, filename):
    # Use the instance's id to create a unique upload path
    return os.path.join('play_areas', str(instance.id), filename)


class PlayAreaDB(models.Model):
    playAreaName = models.CharField(max_length=50)
    playAreaSports = models.CharField(max_length=20)
    playAreaLocation = models.CharField(max_length=100)
    playAreaPrice = models.PositiveIntegerField(default=999.0)
    playAreaVendor = models.CharField(max_length=100,default="Play Connect")
    playAreaImageUrl = models.ImageField(upload_to=play_area_image_upload)

    def __str__(self):
        return f"{self.playAreaName} ({self.playAreaLocation})"

class VendorDB(models.Model):
    VendorName = models.CharField(max_length=50)
    VendorPhoneNo = models.IntegerField()
    VendorEmail=models.EmailField(default="playconnect@gmail.com")
    VendorPassword=models.CharField(max_length=30,default="login123")
    VendorPlayAreaName=models.CharField(max_length=100)
    VendorPlayAreaSports = models.CharField(max_length=20)
    VendorPlayAreaLocation = models.CharField(max_length=100)
    VendorPlayAreaPrice = models.PositiveIntegerField(default=999.0)
    VendorPlayAreaImageOne = models.ImageField(upload_to=play_area_image_upload)
    VendorPlayAreaImageTwo = models.ImageField(upload_to=play_area_image_upload)

    def __str__(self):
        return f"{self.VendorName} ({self.VendorPlayAreaName})"
    
class UserDB(models.Model):
    userName = models.CharField(max_length=100)
    userPhoneNo = models.IntegerField()
    userEmail=models.EmailField()
    userFavSportsOne = models.CharField(max_length=20)
    userFavSportsTwo = models.CharField(max_length=20)
    userLocation = models.CharField(max_length=100)
    userAge = models.SmallIntegerField()

    def __str__(self):
        return f"{self.userName} ({self.userLocation})"
    
class BookingDB(models.Model):
    bookingPlayAreaName = models.CharField(max_length=100)
    bookingPlayAreaDate=models.DateField()
    bookingPlayAreaTime=models.CharField(max_length=100,default=['12AM-1AM'])
    bookingPlayAreaVendor=models.CharField(max_length=100)
    bookingPlayAreaUser=models.CharField(max_length=100)
    bookingPlayAreaUserPhoneNo = models.IntegerField(),
    bookingPlayAreaSports=models.CharField(max_length=50,default="Cricket")
    

    def __str__(self):
        return f"{self.bookingPlayAreaName} ({self.bookingPlayAreaDate},booked by:{self.bookingPlayAreaUser})"
    
    
class AdminDB(models.Model):
    adminUserName = models.CharField(max_length=100)
    adminUserEmail=models.EmailField()
    adminUserPhoneNo=models.IntegerField()
    adminUserPassword = models.CharField(max_length=100)
    adminUserLocation=models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.adminUserName} ({self.adminUserEmail})"
    

