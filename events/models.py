import datetime
from datetime import timedelta


from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Event(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    Bio = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='events/profile/', null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    linkedin = models.URLField(  null=True, blank=True)
    twitter = models.URLField(  null=True, blank=True)

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    events = models.ManyToManyField('Event')

    def __str__(self):
        return f"{self.name} -- {self.email}"


class Schedule(models.Model):
    event_name = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='schedule')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    topic = models.CharField(max_length=100)
    speaker = models.ForeignKey(Speaker, on_delete= models.CASCADE, null=True, blank= True)

    def __str__(self):
        return self.topic


class Payment(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=2)
    PAYMENT_METHOD_CHOICES =(
        ('MoMo', 'Mobile_Money'),
        ('AITELE_MONEY', 'Aitel_Money'),
        ('BK', 'Bank_of_Kigali'),
        ('Equity', 'Equity_Bank'),
        ('VISA','VISA'),
    )
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)
    PAYMENT_STATUS_CHOICES=(
        ('PAID', 'paid'),
        ('PENDING', 'pending'),
        ('FAILED', 'Failed'),
    )
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS_CHOICES)

    def __str__(self):
        return f"{self.participant.name} "

