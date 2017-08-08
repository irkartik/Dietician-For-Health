from django.shortcuts import render
from .forms import QuestionnaireForm
from django.http import HttpResponse
from core.models import Client
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="core:session_login")
def questionnaire_new(request):
	if request.method == 'POST':
		form = QuestionnaireForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.client_name = Client.objects.get(user_name__username=request.user.username)
			instance.save()
			return HttpResponse('saved')
	else:
		form = QuestionnaireForm
	return render(request, 'questionnaire.html', {'form': form})
