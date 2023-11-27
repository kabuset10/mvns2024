from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import ReadingForm, UserForm, ChangePassForm
from .models import Reading
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .decorators import unauthenticated_user
# Create your views here.

'''
    def index(request, *args, **kwargs):
    context = {
        'page_title': 'Home',
    }
    return render(request, "MVNSweb/index.html", context)
'''

@login_required(login_url='MVNS-login')
def view(request, *args, **kwargs):
    reading = Reading.objects.all()
    context = {
        'Reading' : reading,
        'page_title': 'View',
    }
    return render(request, "MVNSweb/mvns_view.html", context)

@csrf_exempt
def add_data(request, *args, **kwargs):
    addForm = ReadingForm(request.POST or None)
    if addForm.is_valid():
        addForm.save()
        addForm = ReadingForm()
    if request.method == 'POST':
        #return HttpResponse(request.POST)
        return redirect('/view')
    
    context = {
        'page_title': 'Add',
        'addForm': addForm,
    }
    return render(request, "MVNSweb/mvns_add_data.html", context)

@login_required(login_url='MVNS-index')
def edit_data(request, pk, *args, **kwargs):
    reading = Reading.objects.get(id = pk)
    editForm = ReadingForm(instance=reading)

    if request.method == 'POST':
        editForm = ReadingForm(request.POST, instance=reading)
        if editForm.is_valid():
            editForm.save()
            return redirect('/view')
    
    context = {
        'editForm' : editForm,
        'page_title': 'Edit',
    }
    return render(request, "MVNSweb/mvns_edit_data.html", context)

@unauthenticated_user
def delete_data(request, pk, *args, **kwargs):
    reading = Reading.objects.get(id = pk)
    if request.method == 'POST':
        reading.delete()
        return redirect ('/view')


def loginUser(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/view')
        else:
            messages.info(request, 'Username OR Password is incorrect.')
        
    context = {
        'page_title': 'Login',
    }
    return render(request, "MVNSweb/index.html", context)

def logoutUser(request, *args, **kwargs):
    logout(request)
    return redirect('MVNS-login')

def register(request, *args, **kwargs):
    registrationForm = UserForm()
    if request.method == "POST":
        registrationForm = UserForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.save() 
            user = registrationForm.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('/view')
    
    context = {
        'registrationForm': registrationForm,
        'page_title': 'Register',
    }
    return render(request, "MVNSweb/mvns_register.html", context)

@login_required(login_url='MVNS-index')
def profile(request, *args, **kwargs):
    context = {
        'page_title': 'Profile',
    }
    return render(request, "MVNSweb/mvns_profile.html", context)

class changepass(PasswordChangeView):
    form_class = ChangePassForm
    success_url = reverse_lazy('MVNS-password-change-success')
    

def password_change_success(request, *args, **kwargs):
    messages.info(request, 'Password Changed Successfully')
    context = {
        'page_title': 'Profile',
    }
    return render(request, "MVNSweb/mvns_profile.html", context)

def user_list(request, *args, **kwargs):
    all_users = User.objects.values()
    context = {
        'all_users': all_users,
        'page_title': 'User List',
    }
    return render(request, "MVNSweb/mvns_user_list.html", context)

def user_list_profile(request, pk, *args, **kwargs):
    user = User.objects.get(id = pk)
    context = {
        'user': user,
        'page_title': 'Edit',
    }
    return render(request, "MVNSweb/mvns_user_list_profile.html", context)

def delete_user(request, pk, *args, **kwargs):
    user = User.objects.get(id = pk)
    if request.method == 'POST':
        user.delete()
        return redirect ('/view')

def reset_password(request, pk, *args, **kwargs):
    user = User.objects.get(id = pk)
    return redirect('/view')