from rest_framework import serializers
from .models import PlayAreaDB,VendorDB,UserDB,BookingDB,AdminDB
from django.conf import settings  # Import Django settings

class PlayAreaSerializer(serializers.ModelSerializer):
    # Add a new field 'playAreaImageUrl' to the serialized representation
    playAreaImageUrl = serializers.SerializerMethodField()

    class Meta:
        model = PlayAreaDB
        fields = ('id', 'playAreaName', 'playAreaSports', 'playAreaLocation', 'playAreaPrice', 'playAreaImageUrl')

    def get_playAreaImageUrl(self, instance):
    # Ensure that 'instance.id' is not None
        if instance.id is not None:
        # Construct and return the image URL
            return settings.MEDIA_URL + str(instance.playAreaImageUrl)
        else:
            return None 
        
class VendorSerializer(serializers.ModelSerializer):
    # Add a new field 'playAreaImageUrl' to the serialized representation
    VendorPlayAreaImageOne= serializers.SerializerMethodField()
    VendorPlayAreaImageTwo= serializers.SerializerMethodField()

    def get_vendorPlayAreaImageOne(self, instance):
    # Ensure that 'instance.id' is not None
        if instance.id is not None:
        # Construct and return the image URL
            return settings.MEDIA_URL + str(instance.VendorPlayAreaImageOne)
        else:
            return None 
        
    def get_vendorPlayAreaImageTwo(self, instance):
    # Ensure that 'instance.id' is not None
        if instance.id is not None:
        # Construct and return the image URL
            return settings.MEDIA_URL + str(instance.VendorPlayAreaImageTwo)
        else:
            return None 

    class Meta:
        model = VendorDB
        fields = ('id', 'VendorName', 'VendorPhoneNo', 'VendorPlayAreaName','VendorEmail', 'VendorPassword','VendorPlayAreaSports','VendorPlayAreaLocation', 'VendorPlayAreaPrice','VendorPlayAreaImageOne','VendorPlayAreaImageTwo')

class UserSerializer(serializers.ModelSerializer):
    # Add a new field 'playAreaImageUrl' to the serialized representation
    # VendorPlayAreaImageOne= serializers.SerializerMethodField()
    # VendorPlayAreaImageTwo= serializers.SerializerMethodField()

    class Meta:
        model = UserDB
        fields = ('id', 'userName', 'userPhoneNo', 'userEmail', 'userFavSportsOne','userFavSportsTwo', 'userLocation','userAge')

class BookingSerializer(serializers.ModelSerializer):
    # Add a new field 'playAreaImageUrl' to the serialized representation
    # VendorPlayAreaImageOne= serializers.SerializerMethodField()
    # VendorPlayAreaImageTwo= serializers.SerializerMethodField()

    class Meta:
        model = BookingDB
        fields = ('id', 'bookingPlayAreaName', 'bookingPlayAreaLocation', 'bookingPlayAreaDate', 'bookingPlayAreaFromTime','bookingPlayAreaToTime', 'bookingPlayAreaVendor','bookingPlayAreaUser','bookingPlayAreaUserPhoneNo')


class AdminSerializer(serializers.ModelSerializer):
    # Add a new field 'playAreaImageUrl' to the serialized representation
    # VendorPlayAreaImageOne= serializers.SerializerMethodField()
    # VendorPlayAreaImageTwo= serializers.SerializerMethodField()

    class Meta:
        model = AdminDB
        fields = ('id', 'adminUserName', 'adminUserEmail', 'adminUserPhoneNo', 'adminUserPassword','adminUserLocation',)

