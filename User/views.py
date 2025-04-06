from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from . forms import UserTypeForm
# Create your views here.

def authorize(request):

    message=''

    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        print('username:',username,'\npassword:',password)

        if 'login' in request.POST.dict():
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                if not hasattr(request.user, 'usertype'):
                    return redirect('usertype')
                return redirect("teacherhome")
            else:
                message="Invalid Credentials, try again"
        else:
            if User.objects.filter(username=username).exists():
                message="Username already exists, try a different one!!"
            else:
                user=User.objects.create_user(username=username,password=password)
                message='Successfully registered on the app!!'
                auth_login(request,user)
                if not hasattr(request.user, 'usertype'):
                    return redirect('usertype')
                return redirect("teacherhome")



    return render(request,"auth.html",{'message':message})

def logout(request):
    auth_logout(request)
    return redirect('auth')


def usertype(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_valid():
            user_type = form.save(commit=False)
            user_type.user = request.user
            user_type.save()
            return redirect('teacherhome')  
    else:
        form = UserTypeForm()
    return render(request, 'usertype_form.html', {'form': form})
