from django.db import models

class NaturalStone(models.Model):
    stone = models.CharField(max_length=32) 
    water_absorbance = models.FloatField(null=True, blank=True) 
    effective_water_absorbance = models.FloatField(null=True, blank=True) 
    natural_water_content = models.FloatField(null=True, blank=True) 
    degree_of_saturation = models.FloatField(null=True, blank=True) 
    dry_density = models.FloatField(null=True, blank=True) 
    saturated_density = models.FloatField(null=True, blank=True) 
    natural_density = models.FloatField(null=True, blank=True) 
    mineral_grain_density = models.FloatField(null=True, blank=True) 
    effective_porosity = models.FloatField(null=True, blank=True) 
    total_porosity = models.FloatField(null=True, blank=True) 
    void_ratio = models.FloatField(null=True, blank=True) 
    ucs = models.FloatField(null=True, blank=True) 
    its = models.FloatField(null=True, blank=True) 
    plt = models.FloatField(null=True, blank=True) 
    bohme = models.FloatField(null=True, blank=True) 
    schmidt = models.FloatField(null=True, blank=True) 
    ultrasonic_wave = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.stone



class Abrasive(models.Model):
    abrasive = models.CharField(max_length=32) 
    density = models.FloatField(null=True, blank=True) 
    hardness_mohs = models.FloatField(null=True, blank=True) 

    def __str__(self):
        return self.abrasive


class CuttingData(models.Model):
    sample_number = models.IntegerField(null=True, blank=True) 
    cutting_speed = models.IntegerField(null=True, blank=True) 
    natural_stone = models.ForeignKey(NaturalStone, on_delete=models.CASCADE)
    abrasive = models.ForeignKey(Abrasive, on_delete=models.CASCADE) 
    cutting_depth = models.FloatField(null=True, blank=True) 
    cd_stddev = models.FloatField(null=True, blank=True) 
    cd_max = models.FloatField(null=True, blank=True) 
    cd_min = models.FloatField(null=True, blank=True) 
    wear_zone_depth = models.FloatField(null=True, blank=True) 
    wz_stddev = models.FloatField(null=True, blank=True) 
    wz_max = models.FloatField(null=True, blank=True) 
    wz_min = models.FloatField(null=True, blank=True) 
    cutting_width = models.FloatField(null=True, blank=True) 
    cw_stddev = models.FloatField(null=True, blank=True) 
    kerf_angle = models.FloatField(null=True, blank=True) 
    material_removal_rate = models.FloatField(null=True, blank=True) 
    Ra_surface_roughness = models.FloatField(null=True, blank=True) 
    Ra_stddev = models.FloatField(null=True, blank=True) 
    Rq_surface_roughness = models.FloatField(null=True, blank=True) 
    Rq_stddev = models.FloatField(null=True, blank=True) 
    Rz_surface_roughness = models.FloatField(null=True, blank=True) 
    Rz_stddev = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"cutting speed: {self.cutting_speed}, abrasive: {self.abrasive}, natural stone: {self.natural_stone}"