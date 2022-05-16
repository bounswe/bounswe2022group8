from django import forms

class TagForm(forms.Form):
    tag=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter tag name'}), max_length=100)