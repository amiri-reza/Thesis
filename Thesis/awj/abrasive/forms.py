from django import forms


class AbrasivesForm(forms.Form):
    name = forms.CharField(max_length=40)
    density = forms.FloatField(required=False)
    hardness = forms.FloatField(required=False)
    chemical_properties = forms.CharField(widget=forms.Textarea, required=False)
    sem_photo = forms.ImageField(label="SEM Image", required=False)
