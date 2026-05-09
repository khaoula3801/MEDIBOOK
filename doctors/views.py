from django.shortcuts import render, get_object_or_404
from .models import Doctor, Specialty

def doctor_list(request):
    doctors = Doctor.objects.filter(is_active=True).select_related('user')
    specialties = Specialty.objects.all()
    q = request.GET.get('q', '')
    specialty_id = request.GET.get('specialty', '')
    if q:
        doctors = doctors.filter(user__first_name__icontains=q) | \
                  doctors.filter(user__last_name__icontains=q)
    if specialty_id:
        doctors = doctors.filter(specialties__id=specialty_id)
    return render(request, 'doctors/list.html', {
        'doctors': doctors, 'specialties': specialties, 'q': q
    })

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk, is_active=True)
    return render(request, 'doctors/detail.html', {'doctor': doctor})