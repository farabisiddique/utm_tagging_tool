from django.shortcuts import render
from .forms import InputForm

# Create your views here.
def home_view(request):
	context ={}
	context['form']= InputForm()
	return render(request, "home.html", context)


def show_utm(request):
	ad_url = request.POST.get("ad_url", "")
	utm_source = '&utm_source='+request.POST.get("utm_source", "")
	utm_medium = '&utm_medium='+request.POST.get("utm_medium", "")
	utm_campaign = '&utm_campaign='+request.POST.get("utm_campaign", "")
	utm_content = '&utm_content='+request.POST.get("utm_content", "")
	utm_term = '&utm_term='+request.POST.get("utm_term", "")
	final_url = ad_url + utm_source + utm_medium + utm_campaign + utm_content + utm_term
	context ={}
	if ad_url:
		context = {'final_url': final_url,}
	context['form']= InputForm()
	return render(request, "home.html", context)
