from django import forms

class HandballScoreForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)