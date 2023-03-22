from django.shortcuts import render

# Create your views here.
def testing(request):
	return render(request,'apps/sample.html')

def description(request):
	return render(request,'apps/description.html')

def images(request):
	return render(request,'apps/images.html')

def cost(request):
	return render(request,'apps/cost.html')


