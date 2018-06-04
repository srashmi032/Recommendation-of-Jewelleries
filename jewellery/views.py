from django.shortcuts import render

# Create your views here.
from .models import Jewellery,color,dress
from django.template import loader
from django.http import HttpResponse
from jewellery.forms import ProfileForm


	
def upload_form(request):
	return render(request, 'jewellery/upload.html')

def upload(request):
	saved = False
   
	if request.method == "POST":
		MyProfileForm = ProfileForm(request.POST, request.FILES)

		if MyProfileForm.is_valid():
			profile = dress()
			#profile.name = MyProfileForm.cleaned_data["name"]
			profile.picture = MyProfileForm.cleaned_data["picture"]
			profile.save()
			saved = True
		else:
			MyProfileForm = ProfileForm()

		context={'saved':saved}

	
	#return HttpResponse("Upload an image file")
	return render(request, 'jewellery/saved.html',context)
