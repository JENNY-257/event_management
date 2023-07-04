from django.shortcuts import render, redirect
from django.db.models import Count, Sum
from django.utils import timezone
from .models import Event, Category, Speaker, Participant, Payment, Schedule
from .forms import EventForm, ScheduleForm, SpeakerForm,  ParticipantForm, PaymentForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events/events')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def create_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = ScheduleForm()
    return render(request, 'create_schedule.html', {'form': form})

def create_speaker(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events/speakers')
    else:
        form = SpeakerForm()
    return render(request, 'create_speaker.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def speaker_list(request):
    speakers = Speaker.objects.all()
    return render(request, 'speaker_list.html', {'speakers': speakers})

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})

def create_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events/participants')
    else:
        form = ParticipantForm()
    return render(request, 'create_participant.html', {'form': form})


def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events/payments')
    else:
        form = PaymentForm()
    return render(request, 'create_payment.html', {'form': form})

def participant_detail(request, email):
    participant = (Participant, email==email)
    context = {'participant': participant}
    return render(request, 'participant_detail.html', context)

def schedule_list(request):
    schedules = Schedule.objects.all()
    context = {'schedules': schedules}
    return render(request, 'schedules.html', context)

def speaker_detail(request, name):
    speaker = (Speaker, name==name)
    return render(request, 'speaker_detail.html', {'speaker': speaker})

def upcoming_events(request):
    current_date = timezone.now().date()
    upcoming_events = Event.objects.filter(start_date__gte=current_date)
    return render(request, 'upcoming_events.html', {'upcoming_events': upcoming_events})

def free_events(request):
    free_events = Event.objects.filter(is_free=True)
    return render(request, 'free_events.html', {'free_events': free_events})

def payment_by_participant(request, email):
    participant = Participant.objects.get(email=email)
    payments = Payment.objects.filter(participant=participant)
    return render(request, 'payment_by_participant.html', {'participant': participant, 'payments': payments})


def paid_events(request):
    paid_events = Event.objects.filter(is_free=False)
    return render(request, 'paid_events.html', {'paid_events': paid_events})

def participant_count_per_event(request):
    participant_counts = Event.objects.annotate(num_participants= Count('participant'))
    return render(request, 'participant_count_per_event.html', {'participant_counts': participant_counts})


def schedule_count_per_event(request):
    schedule_counts = Event.objects.annotate(num_schedules=Count('schedule'))
    return render(request, 'schedule_count_per_event.html', {'schedule_counts': schedule_counts})

def total_amount_paid_for_event(request, title):
    event = Event.objects.get(title=title)
    total_amount_paid = event.payment.aggregate(total_amount=Sum('amount_paid'))['total_amount']
    return render(request, 'total_amount_paid_for_event.html', {'event': event, 'total_amount_paid': total_amount_paid})

def participants_attended_all_events(request):
    all_events = Event.objects.all()
    participants_attended_all = []
    for participant in Participant.objects.all():
        if all(participant in event.participants.all() for event in all_events):
            participants_attended_all.append(participant)
    return render(request, 'participants_attended_all_events.html', {'participants_attended_all': participants_attended_all})
