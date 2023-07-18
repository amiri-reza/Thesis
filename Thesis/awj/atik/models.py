from django.db import models


class NaturalStones(models.Model):
    name = models.CharField(max_length=40)
    chemical_properties = models.TextField(max_length=255)
    sem_photo = models.ImageField(blank=True, null=True)

    def get_fields(self):
        return [
            (field.name, field.value_to_string(self))
            for field in NaturalStones._meta.fields
        ]

    def __str__(self):
        return f"{self.name}"


class MechanicalProperties(models.Model):
    stone = models.OneToOneField(NaturalStones, on_delete=models.CASCADE)
    density = models.FloatField(blank=True, null=True)
    schmidt_hardness = models.FloatField(blank=True, null=True)
    indirect_tensile = models.FloatField(blank=True, null=True)
    uniaxial_comp_str = models.FloatField(blank=True, null=True)
    bohme = models.FloatField(blank=True, null=True)
    point_load = models.FloatField(blank=True, null=True)
    ultrasonic = models.FloatField(blank=True, null=True)

    def get_fields(self):
        return [
            (field.name, field.value_to_string(self))
            for field in MechanicalProperties._meta.fields
        ]


class PhysicalProperties(models.Model):
    stone = models.OneToOneField(NaturalStones, on_delete=models.CASCADE)
    su_emme_kapasitesi = models.FloatField(blank=True, null=True)
    efektif_su_emme = models.FloatField(blank=True, null=True)
    dogal_su_icerigi = models.FloatField(blank=True, null=True)
    doyma_derecesi = models.FloatField(blank=True, null=True)
    kuru_yogunluk = models.FloatField(blank=True, null=True)
    doymus_yogunluk = models.FloatField(blank=True, null=True)
    tabii_yogunluk = models.FloatField(blank=True, null=True)
    mineral_tane_yogunlugu = models.FloatField(blank=True, null=True)
    efektif_porozite = models.FloatField(blank=True, null=True)
    toplam_porozite = models.FloatField(blank=True, null=True)
    bosluk_orani = models.FloatField(blank=True, null=True)

    def get_fields(self):
        return [
            (field.name, field.value_to_string(self))
            for field in PhysicalProperties._meta.fields
        ]
