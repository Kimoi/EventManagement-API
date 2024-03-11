from django.contrib import admin
from .models import User, Organization, Event


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'phone_number', 'organization',
                    'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'organization')
    search_fields = ('email', 'username', 'phone_number', 'organization__title')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'address', 'postcode')
    search_fields = ('title', 'description', 'address', 'postcode')


class OrganizationInline(admin.TabularInline):
    model = Event.organizations.through
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [OrganizationInline]
    list_display = ('id', 'title', 'description', 'date', 'display_image')
    list_filter = ('date', 'organizations')
    search_fields = ('title', 'description', 'date')

    @staticmethod
    def display_image(obj) -> str:
        return obj.image.url if obj.image else 'No image'

    display_image.short_description = 'Image'
