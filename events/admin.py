from django.contrib import admin
from events.models import Category, Event, Speaker, Participant, Schedule, Payment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name']


class EventAdmin(admin.ModelAdmin):
    list_display=['title', 'description', 'start_date', 'end_date', 'location', 'category', 'is_free']


class SpeakerAdmin(admin.ModelAdmin):
    list_display=['name', 'Bio', 'photo', 'email', 'phone', 'linkedin', 'twitter']


class ParticipantAdmin(admin.ModelAdmin):
    list_display= ['name', 'email', 'phone', 'events']


class ScheduleAdmin(admin.ModelAdmin):
    list_display=['event_name', 'start_time', 'end_time', 'topic', 'speaker']


class PaymentAdmin(admin.ModelAdmin):
    list_display=['participant', 'event', 'paid_amount', 'payment_method', 'payment_date', 'transaction_id', 'payment_status']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Participant)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Payment, PaymentAdmin)