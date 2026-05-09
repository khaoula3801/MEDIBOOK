from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from doctors.models import Doctor
from .models import Appointment
from .utils import get_available_slots
from datetime import date, timedelta

@login_required
def book_appointment(request, doctor_pk):
    doctor = get_object_or_404(Doctor, pk=doctor_pk, is_active=True)
    slots_by_date = {}
    for i in range(1, 15):
        d = date.today() + timedelta(days=i)
        slots = get_available_slots(doctor, d)
        if slots:
            slots_by_date[d] = slots

    if request.method == 'POST':
        selected_date = request.POST.get('date')
        selected_time = request.POST.get('time')
        reason = request.POST.get('reason', '')
        Appointment.objects.create(
            patient=request.user,
            doctor=doctor,
            specialty=doctor.specialties.first(),
            date=selected_date,
            time=selected_time,
            reason=reason,
            status='pending'
        )
        messages.success(request, "Rendez-vous réservé avec succès !")
        return redirect('dashboard:patient')

    return render(request, 'appointments/book.html', {
        'doctor': doctor,
        'slots_by_date': slots_by_date
    })

@login_required
def cancel_appointment(request, pk):
    apt = get_object_or_404(Appointment, pk=pk, patient=request.user)
    if apt.status in ['pending', 'confirmed']:
        apt.status = 'cancelled'
        apt.save()
        messages.success(request, "Rendez-vous annulé.")
    return redirect('dashboard:patient')