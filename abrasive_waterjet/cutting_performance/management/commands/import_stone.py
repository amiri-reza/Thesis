from django.core.management.base import BaseCommand, CommandError
from cutting_performance.models import NaturalStone
import pandas as pd


class Command(BaseCommand):
    help = 'Imports data from "static/csv/data.csv" path.'

    def handle(self, *args, **kwargs):
        df = pd.read_csv("static/csv/stone_data.csv", sep=";")
        row_iter = df.iterrows()
        # breakpoint()
        for index, row in row_iter:
            NaturalStone.objects.create(
                stone = row["stone"],  
                water_absorbance = row["water_absorbance"], 
                effective_water_absorbance = row["effective_water_absorbance"], 
                natural_water_content = row["natural_water_content"], 
                degree_of_saturation = row["degree_of_saturation"], 
                dry_density = row["dry_density"], 
                saturated_density = row["saturated_density"], 
                natural_density = row["natural_density"], 
                mineral_grain_density = row["mineral_grain_density"], 
                effective_porosity = row["effective_porosity"], 
                total_porosity = row["total_porosity"], 
                void_ratio = row["void_ratio"], 
                ucs = row["ucs"], 
                its = row["its"], 
                plt = row["plt"], 
                bohme = row["bohme"], 
                schmidt = row["schmidt"], 
                ultrasonic_wave = row["ultrasonic_wave"],
            )

        self.stdout.write(self.style.SUCCESS("Stone Data successfully imported"))
