from django.core.management.base import BaseCommand, CommandError
from cutting_performance.models import Abrasive
import pandas as pd


class Command(BaseCommand):
    help = 'Imports data from "static/csv/data.csv" path.'

    def handle(self, *args, **kwargs):
        df = pd.read_csv("static/csv/abrasive_data.csv", sep=";")
        row_iter = df.iterrows()
        # breakpoint()
        for index, row in row_iter:
            Abrasive.objects.create(
                abrasive = row["abrasive"],
                density = row["density"],
                hardness_mohs = row["hardness_mohs"]
            )

        self.stdout.write(self.style.SUCCESS("Stone Data successfully imported"))