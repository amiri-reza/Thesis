from django import forms

CHOICES = [
    ("cutting_depth", "Cutting Depth"),
    ("cd_stddev", "Cutting Depth Standard Deviation"),
    ("cd_max", "Maximum Cutting Depth Point"),
    ("cd_min", "Minimum Cutting Depth Poin"),
    ("wear_zone_depth", "Wear Zone Depth"),
    ("wz_stddev", "Wear Zone Standart Deviation"),
    ("wz_max", "Maximum Depth of Wear Zone Point"),
    ("wz_min", "Minimum Depth of Wear Zone Point"),
    ("cutting_width", "Cutting Width"),
    ("cw_stddev", "Cutting Width Standard Deviation"),
    ("kerf_angle", "Kerf Angle"),
    ("material_removal_rate", "Material Removal Rate (MRR)"),
    ("Ra_surface_roughness", "Surface Roughness (Ra)"),
    ("Ra_stddev", "Surface Roughness (Ra) Standard Deviation"),
    ("Rq_surface_roughness", "Surface Roughness (Rq)"),
    ("Rq_stddev", "Surface Roughness (Rq) Standard Deviation"),
    ("Rz_surface_roughness", "Surface Roughness (Rz)"),
    ("Rz_stddev", "Surface Roughness (Rz) Standard Deviation")

]



class PlotSelectorForm(forms.Form):
    cutting_parameter = forms.CharField(
        label="Select the cutting result you want to see: ",
        widget=(forms.Select(choices=CHOICES)),
        required=True
    )
