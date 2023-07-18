from django.db import models


class Abrasives(models.Model):
    name = models.CharField(max_length=40)
    chemical_properties = models.TextField(max_length=255)
    sem_photo = models.ImageField(blank=True, null=True)

    def get_fields(self):
        return [
            (field.name, field.value_to_string(self))
            for field in Abrasives._meta.fields
        ]

    def __str__(self):
        return f"{self.name}"


class AbrasiveProperties(models.Model):
    abrasive = models.OneToOneField(Abrasives, on_delete=models.CASCADE)
    density = models.FloatField(blank=True, null=True)
    hardness = models.FloatField(blank=True, null=True)

    def get_fields(self):
        return [
            (field.name, field.value_to_string(self))
            for field in AbrasiveProperties._meta.fields
        ]
