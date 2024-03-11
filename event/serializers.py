from rest_framework import serializers
from .models import User, Organization, Event


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class OrganizationSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['title']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['title', 'description', 'address', 'postcode']


class OrganizationDetailSerializer(serializers.ModelSerializer):
    users = UserSimpleSerializer(many=True, read_only=True)
    full_address = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ['title', 'description', 'full_address', 'users']

    @staticmethod
    def get_full_address(obj):
        return f'{obj.address}, {obj.postcode}'


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'image')


class EventSerializer(serializers.ModelSerializer):
    organizations = OrganizationSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'image', 'organizations')


class EventDetailSerializer(serializers.ModelSerializer):
    organizations = OrganizationDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'image', 'organizations')
