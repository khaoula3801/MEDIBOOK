from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .ml_model import get_specialty_recommendations

@login_required
def orientation_view(request):
    recommendations = []
    symptom_text = ''

    if request.method == 'POST':
        symptom_text = request.POST.get('symptoms', '')
        if symptom_text.strip():
            recommendations = get_specialty_recommendations(symptom_text)

    return render(request, 'ai_orientation/form.html', {
        'recommendations': recommendations,
        'symptom_text': symptom_text
    })