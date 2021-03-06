from rest_framework import serializers
from .models import Facility, Location, User


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    locations = serializers.HyperlinkedRelatedField(
        view_name='location_detail',
        many=True,
        read_only=True
    )
    facility_url = serializers.ModelSerializer.serializer_url_field(
        view_name='facility_detail'
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    class Meta:
        model = Facility
        fields = ('id', 'facility_url', 'user_id', 'name',
                  'details', 'photo_url', 'address', 'phone', 'email', 'parking_info', 'acc_entrance', 'acc_restroom', 'open_now', 'locations',)


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    facilities = serializers.HyperlinkedRelatedField(
        view_name='facility_detail',
        read_only=True
    )

    facility_id = serializers.PrimaryKeyRelatedField(
        queryset=Facility.objects.all(),
        source='facility'
    )

    class Meta:
        model = Location
        fields = ('id', 'facilities', 'facility_id',
                  'country', 'state', 'city',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    facilities = serializers.HyperlinkedRelatedField(
        view_name='facility_detail',
        many=True,
        read_only=True
    )
    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail'
    )

    class Meta:
        model = User
        fields = ('id', 'user_url', 'first_name',
                  'last_name', 'email', 'password', 'facilities',)
