from django.core.management.base import BaseCommand, CommandError
from cutting_performance.models import CuttingData, NaturalStone, Abrasive
import pandas as pd


class Command(BaseCommand):
    help = 'Imports data from "static/csv/data.csv" path.'

    def handle(self, *args, **kwargs):
        df = pd.read_csv("static/csv/cutting_data.csv", sep=";")
        row_iter = df.iterrows()
        for index, row in row_iter:
            CuttingData.objects.create(
                sample_number = row["sample_number"], 
                cutting_speed = row["cutting_speed"], 
                natural_stone = NaturalStone.objects.get(stone=row["stone"]),
                abrasive = Abrasive.objects.get(abrasive=row["abrasive"]),
                cutting_depth = row["cutting_depth"], 
                cd_stddev = row["cd_stddev"], 
                cd_max = row["cd_max"], 
                cd_min = row["cd_min"], 
                wear_zone_depth = row["wear_zone_depth"], 
                wz_stddev = row["wz_stddev"], 
                wz_max = row["wz_max"], 
                wz_min = row["wz_min"], 
                cutting_width = row["cutting_width"], 
                cw_stddev = row["cw_stddev"], 
                kerf_angle = row["kerf_angle"], 
                material_removal_rate = row["material_removal_rate"], 
                Ra_surface_roughness = row["Ra_surface_roughness"], 
                Ra_stddev = row["Ra_stddev"], 
                Rq_surface_roughness = row["Rq_surface_roughness"], 
                Rq_stddev = row["Rq_stddev"], 
                Rz_surface_roughness = row["Rz_surface_roughness"], 
                Rz_stddev = row["Rz_stddev"],

            )

        self.stdout.write(self.style.SUCCESS("Stone Data successfully imported"))