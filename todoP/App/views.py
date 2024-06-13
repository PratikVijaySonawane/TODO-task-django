from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import TODOForm
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user # will save the request.user object to user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority') #this will fetch the data with user object
        return render(request,"home.html",context={'form':form, 'todos':todos})

#Function to add the Task
@login_required(login_url='login')
def addtodo(request):
    if request.user.is_authenticated:
        user = request.user # will save the request.user object to user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect('home')
        else:
            return render(request,'home.html',context={'form':form})    
        
#Function for the Delete
def deletetodo(request,id):
    TODO.objects.get(pk=id).delete()
    return redirect('home')


#Function for the Login
def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            'form' : form1,
        }
        return render(request,'login.html',context=context)
    else:
        #Condition for the POST
           form = AuthenticationForm(data = request.POST)
           #Check Validation
           if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username , password=password)
                if user is not None:
                    loginUser(request,user)
                    return redirect('home')
           else:
                context = {
                   'form' : form
               }
                return render(request,"login.html",context=context)

#Function for the Signup
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form' : form,
        }
        return render(request,"signup.html",context=context)
    else:
        #creadted the object of the [UserCreationForm]
        form = UserCreationForm(request.POST)
        context ={
            'form' : form,
        }
        # Validation checked
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request,'signup.html',context=context)
        
#Function for the Logout
def signout(request):
    logout(request)
    return redirect('login')

#Function for changetodo
def changetodo(request,id,status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')



