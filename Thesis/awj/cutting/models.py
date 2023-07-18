from django.db import models
from atik.models import NaturalStones
from abrasive.models import Abrasives


class Cut(models.Model):
    stone = models.ForeignKey(NaturalStones, on_delete=models.CASCADE)
    abrasive = models.ForeignKey(Abrasives, on_delete=models.CASCADE)
    kesme_hizi = models.IntegerField(null=True, blank=True)
    kesme_derinligi = models.FloatField(null=True, blank=True)
    kesme_asinma = models.FloatField(null=True, blank=True)
    kd_max = models.FloatField(null=True, blank=True)
    kd_min = models.FloatField(null=True, blank=True)
    ka_max = models.FloatField(null=True, blank=True)
    ka_min = models.FloatField(null=True, blank=True)
    kesme_genisligi = models.FloatField(null=True, blank=True)
    yuzey_puruzlulugu = models.FloatField(null=True, blank=True)
    kerf_acisi = models.FloatField(null=True, blank=True)
    plaka_agirlik_kaybi = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}. {self.abrasive} cut {self.stone} with {self.kesme_hizi} mm/min speed."
