from django.shortcuts import render

# Create your views here.

def profile(request):
   
    context = {
        'name': 'Amr',
        'bio': 'I am a student studing engineering who loves building simple web projects with Django.',
        'skills': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
    }
    return render(request, 'profileapp/profile.html', context)
