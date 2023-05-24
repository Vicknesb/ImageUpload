

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

from Configurations.config import Config
from Configurations.logger import log_error
from .forms import ImageForm
from django.db.models import Q
from .models import Image


DISPLAY_HTML = "display.html"
configObj = Config()
logger = log_error()


def register(request):
    try:
        if (request.method == 'POST'):
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "User Already Exist")
                    return redirect(register)
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.set_password(password)
                    user.save()
                    return redirect('login_user')
                                    
        else: 
            return render(request, "register.html")
        
    except Exception as e:
        logger.error(f"Not valid data in register user : {e}")
        

def login_user(request):
    try:        
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                data = Image.objects.all()
                context = {
                'data': data
                }
                return render(request, DISPLAY_HTML, context)
            else:
                messages.info(request, "Invalid Username or Password")
                return redirect('login_user')
        else:
            return render(request, "login.html")
    except Exception as e:
        logger.error(f"Invalid login entry : {e}")


def logout_user(request):
    auth.logout(request)
    return redirect("login_user")


def upload(request):
    try:
        data = Image.objects.all()
        context = {
            'data': data
        }

        if request.method == 'POST':            
            form = ImageForm(request.POST, request.FILES)
            
            if form.is_valid():
                form = Image()
                encoded_string = request.FILES['binary_image']
                form = Image(title= request.POST.get('title'),
                                description = request.POST.get('description'),
                                binary_image = encoded_string.read())
                form.save()
                return render(request, DISPLAY_HTML, context)
        else:
            form = ImageForm()
        return render(request, 'upload.html', {'form': form})
    except Exception as e:
        logger.error(f"Not valid image uploaded : {e}")

def success():
    return HttpResponse('successfully uploaded')


def display(request):
    try:
        data = Image.objects.all()
        context = {
            'data': data
        }
        return render(request, DISPLAY_HTML, context)
    except Exception as e:
        logger.error(f"Not valid data found : {e}")


def searchImage(request):
    try:
        query = request.GET.get('q')
        images = Image.objects.filter(Q(image__icontains=query) | Q(title__icontains=query))
        context = {
            'data': images
        }
        return render(request, DISPLAY_HTML, context)
    except Exception as e:
        logger.error(f"Not valid data found : {e}")
