from django.shortcuts import render
from .models import Course

def home(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(title__icontains=query)
    else:
        courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})
