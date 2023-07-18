from django import forms


class NaturalStoneForm(forms.Form):
    name = forms.CharField(max_length=40)
    density = forms.FloatField(required=False)
    schmidt_hardness = forms.FloatField(required=False)
    indirect_tensile = forms.FloatField(required=False)
    uniaxial_comp_str = forms.FloatField(required=False)
    bohme = forms.FloatField(required=False)
    point_load = forms.FloatField(required=False)
    ultrasonic = forms.FloatField(required=False)
    su_emme_kapasitesi = forms.FloatField(required=False)
    efektif_su_emme = forms.FloatField(required=False)
    dogal_su_icerigi = forms.FloatField(required=False)
    doyma_derecesi = forms.FloatField(required=False)
    kuru_yogunluk = forms.FloatField(required=False)
    doymus_yogunluk = forms.FloatField(required=False)
    tabii_yogunluk = forms.FloatField(required=False)
    mineral_tane_yogunlugu = forms.FloatField(required=False)
    efektif_porozite = forms.FloatField(required=False)
    toplam_porozite = forms.FloatField(required=False)
    bosluk_orani = forms.FloatField(required=False)
    chemical_properties = forms.CharField(widget=forms.Textarea, required=False)
    sem_photo = forms.ImageField(label="SEM Image", required=False)
