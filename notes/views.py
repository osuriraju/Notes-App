from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import forms
from .models import Newnote
from django.contrib import messages
# Create your views here.


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.info(request, user)
            return redirect('home')
        else:
            return render(request, 'account/signin.html')
    return render(request, 'account/signin.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        
        user = User.objects.create_user(username=username, first_name = first_name, last_name = last_name, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('/home')
    else:
        return render(request, 'account/signup.html')




@login_required(login_url='/signin')
def index(request):
    form = forms.NotesForm()
    notes = Newnote.objects.all()
    context = {
        'form':form,
        'notes':notes
    }
    return render(request, 'home/index.html', context)


def newnote(request):
    if request.method == "POST":
        form = forms.NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse('Hello world')
    else:
        return HttpResponse('Hello world')



def delete_note(request, note_id):
    event = Newnote.objects.get(pk=note_id)
    event.delete()
    return redirect('index')


