from django.shortcuts import render,redirect
from .models import animate_user


def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        animate = animate_user.objects.create(
            username=username,
            password=password,
        )
        animate.save()
        return redirect('home')

    return render(request, 'component.html')