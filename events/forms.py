# forms.py
from django import forms
from .models import Event, Schedule, Speaker, Participant, Payment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'location', 'category', 'is_free']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['event_name', 'start_time', 'end_time', 'topic', 'speaker']

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ['name', 'Bio', 'photo', 'email', 'phone', 'linkedin', 'twitter']

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'phone', 'events']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['participant', 'event', 'paid_amount', 'payment_method',  'transaction_id', 'payment_status']
