from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'name':' Anurag Pathak'}
    return render(request, 'home.html', context=context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def hobbies(request):
    context = { "hobbies": ["Python", "Django", "Gaming", "Music"] }
    return render(request, 'hobbies.html', context=context)