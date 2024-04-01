# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from main.forms.userforms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return redirect('signup.html')
                #return render(request, 'levanta.html', {'form': form, 'error': 'Usuario o contraseña incorrectos.'})
    else:
        form = LoginForm()
    return render(request, 'levanta.html', {'form': form})
