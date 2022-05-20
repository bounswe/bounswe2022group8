from django import forms

class TagForm(forms.Form):
    tag=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter tag name'}), max_length=100)

class QuestionTagForm(forms.Form):
    tag=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Question tag'}), max_length=100)    