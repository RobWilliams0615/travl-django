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

    class Meta:
        model = Facility
        fields = ('id', 'facility_url', 'name',
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
        fields = ('id', 'facility', 'facility_id', 'country', 'state', 'city')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    facilities = serializers.HyperlinkedRelatedField(
        view_name='facility_detail',
        read_only=True
    )
    facility_url = serializers.ModelSerializer.serializer_url_field(
        view_name='facility_detail'
    )

    class Meta:
        model = User
        fields = ('id', 'facility', 'facility_url', 'first_name',
                  'last_name', 'email', 'password', '')
