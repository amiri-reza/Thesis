from django import forms

class EmailForm(forms.Form):
    sender_name = forms.CharField(max_length=100)
    sender_email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
