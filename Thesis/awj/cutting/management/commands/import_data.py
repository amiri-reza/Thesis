from django.core.management.base import BaseCommand, CommandError
from cutting.models import Cut
from atik.models import NaturalStones
from abrasive.models import Abrasives
import pandas as pd


class Command(BaseCommand):
    help = 'Imports data from "static/csv/data.csv" path.'

    def handle(self, *args, **kwargs):
        df = pd.read_csv("static/csv/data.csv", sep=",")
        row_iter = df.iterrows()
        # breakpoint()
        for index, row in row_iter:
            Cut.objects.create(
                stone=NaturalStones.objects.get(id=row["stone"]),
                abrasive=Abrasives.objects.get(id=row["abrasive"]),
                kesme_hizi=row["kesme_hizi"],
                kesme_derinligi=row["kesme_derinligi"],
                kesme_asinma=row["kesme_asinma"],
                kd_max=row["kd_max"],
                kd_min=row["kd_min"],
                ka_max=row["ka_max"],
                ka_min=row["ka_min"],
                kesme_genisligi=row["kesme_genisligi"],
                yuzey_puruzlulugu=row["yuzey_puruzlulugu"],
                kerf_acisi=row["kerf_acisi"],
                plaka_agirlik_kaybi=row["plaka_agirlik_kaybi"],
            )

            # print(row['stone'])

        self.stdout.write(self.style.SUCCESS("Data successfully imported"))
