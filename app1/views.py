from django.shortcuts import render
from .forms import contactForm
# Create your views here.


def home(request):
    if request.method == 'POST':
        fm = contactForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = contactForm()    
            return render(request, 'index.html', {"form": fm})
    else:
        fm = contactForm()    
    return render(request, 'index.html', {"form": fm})
