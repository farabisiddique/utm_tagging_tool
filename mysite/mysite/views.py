from django.shortcuts import render
from .forms import InputForm
from selenium import webdriver
from bs4 import BeautifulSoup
import time

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

def scrape_linkedin(request):
	# Creating a webdriver instance
	# driver = webdriver.Chrome("C:/Users/Win 10 Pro/Desktop/chromedriver.exe")
	# This instance will be used to log into LinkedIn

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-gpu")	
	driver = webdriver.Chrome(options=chrome_options)

	# Opening linkedIn's login page
	driver.get("https://www.linkedin.com/login")

	# waiting for the page to load
	time.sleep(5)

	# entering username
	username = driver.find_element_by_id("username")

	# In case of an error, try changing the element
	# tag used here.

	# Enter Your Email Address
	username.send_keys("data@digitaluncut.com")

	# entering password
	pword = driver.find_element_by_id("password")
	# In case of an error, try changing the element
	# tag used here.

	# Enter Your Password
	pword.send_keys("YnsttgAx97iFoPBKDx")		

	# Clicking on the log in button
	# Format (syntax) of writing XPath -->
	# //tagname[@attribute='value']
	driver.find_element_by_xpath("//button[@type='submit']").click()
	# In case of an error, try changing the
	# XPath used here.
	profile_url = "https://www.linkedin.com/campaignmanager/accounts/503389130/campaign-groups"
  
	driver.get(profile_url)        # this will open the link

	campaign_row_class = driver.find_elements_by_class_name("u-color__blue7")

	x = []
	for element in campaign_row_class:
		y = element.get_attribute('href')
		x.append(y)
	context = {'hey': x,}

	
	return render(request, "scraperesult.html", context)

def scrape_google(request):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-gpu")
	browser = webdriver.Chrome(options=chrome_options)
	try:
	    browser.get("https://www.google.com")
	    print("Page title was '{}'".format(browser.title))
	finally:
	    browser.quit()
	return render(request, "home.html")