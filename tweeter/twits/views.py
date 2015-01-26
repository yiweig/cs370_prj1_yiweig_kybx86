from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def index(request):
	#return HttpResponse("Hello, cs370! You're at the twits index.")
	template = loader.get_template("twits/index_yiwei.html")
	return HttpResponse(template.render())

