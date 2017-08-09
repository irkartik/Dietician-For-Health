from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.models import *
from notification.models import Notification
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, Http404
from django.views.decorators.http import condition


def homeview(request):
	testimonial_list = Testimonial.objects.all()
	video_list = Video.objects.all()
	ad_list = TopAdBar.objects.order_by('order')
	banner_list = Banner.objects.order_by('order')
	context = {
		'testimonial_list' : testimonial_list,
		'video_list': video_list,
		'ad_list': ad_list,
		'banner_list': banner_list}
	return render(request, "home/home.html", context)

def user_signup(request):
	context = {}
	return render(request, "after_login/user/user_signup.html", context)

def session_login(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.user_type == 'CM':
					login(request, user)
					return redirect('core:user_dashboard')
				elif user.user_type == 'DM':
					login(request, user)
					return HttpResponse('dietician panel')
				elif user.user_type == 'PM':
					login(request, user)
					return HttpResponse('docters and neuropath module')
				else:
					return HttpResponse('You have a separate admin panel login there!')		
			else:
				return render(request, 'after_login/login.html', {'error_message': 'Invalid Login Credentials'})
		return render(request, 'after_login/login.html')
	else:
		if request.user.user_type == 'CM':
			return redirect('core:user_dashboard')
		elif request.user.user_type == 'DM':
			return HttpResponse('dietician panel')
		elif request.user.user_type == 'PM':
			return HttpResponse('docters and neuropath module')
		else:
			return HttpResponse('You have a separate admin panel login there!')

@login_required(login_url="core:session_login")
def session_logout(request):
	logout(request)
	return redirect('core:home')

@login_required(login_url="core:session_login")
@user_passes_test(lambda u: u.user_type=='CM', redirect_field_name='/login')
def user_dashboard(request):
	notification_list = Notification.objects.filter(notification_for=request.user, viewed=False).order_by('-created_at')[:40]
	context = {
		'notification_list' : notification_list,
		'notification_count' : notification_list.count(),
		}
	return render(request, "after_login/user/user_dashboard.html", context)

@login_required(login_url="core:session_login")
@user_passes_test(lambda u: u.user_type=='CM', redirect_field_name='/login')
def user_profile(request):
	context = {}
	return render(request, "after_login/user/user_profile.html", context)


