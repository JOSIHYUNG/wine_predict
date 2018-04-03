from django.shortcuts import render
from .models import WineData

# Create your views here.
def index(request):
	data=WineData.objects.all()[:50]
	return render(request,'index.html',{'data':data})

def search(request):
	return render(requset,'search.html',{})