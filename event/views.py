from rest_framework import generics, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Prefetch

from .serializers import OrganizationSerializer, EventSerializer, EventCreateSerializer, EventDetailSerializer
from .models import Organization, Event
from .tasks import event_sleep_60


class OrganizationViewSet(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class EventViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ordering_fields = ['date']
    search_fields = ['title']

    def get_queryset(self):
        queryset = Event.objects.all()
        if self.action == 'retrieve':
            queryset = queryset.prefetch_related(
                Prefetch(
                    'organizations',
                    queryset=Organization.objects.prefetch_related('users'),
                )
            )
        return queryset

    def get_serializer_class(self):
        if self.action == 'create':
            event_sleep_60.delay()
            return EventCreateSerializer
        elif self.action == 'retrieve':
            return EventDetailSerializer
        return EventSerializer
