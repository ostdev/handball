from django.shortcuts import render
from django.http import HttpResponse
from .forms import HandballScoreForm
from .models import Teams

def home_page_view(request):
	result = ""
	teams = Teams()
	if request.method == 'POST':
		form = HandballScoreForm(request.POST)
		if form.is_valid():
			text = str(form.cleaned_data['text'])
			print(text)
			lines = text.split("\n")
			for line in lines:
				data = list(map(str.strip, line.split("|")))
				teams.add_match(*data)
				result = teams.html()
	else:
		form = HandballScoreForm()	
	return render(request,'views/form.html',{'form':form,'result':result})
