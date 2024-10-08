from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages


# Create your views here.
def home(request):
	# if the user is trying to login ,aka do "POST"request. Otherwise, they're just getting info or doing a "GET" request
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		#authenticate the person trying to log in
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"logged in")
			return redirect('home')
		else:
			messages.success(request,"There was an error trying to log you in")
			return redirect('home')
	
	else:
		return render(request,'home.html',{})


def logout_user(request):
	logout(request)
	messages.success(request,"logged out")
	return redirect('home')
def register_user(request):
	return render(request,'register.html',{})