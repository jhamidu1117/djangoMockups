import pandas as pd
import os
from django.core.management.base import BaseCommand, CommandError


class AddUPCs(BaseCommand):
    help = 'adds a sample set of handset data to the database'

    def handle(self, *args, **options):
        home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        raw_data = os.path.join(home_dir, 'RawData/samupc.csv')
        raw_df = pd.read_csv(raw_data, nrows=10)
        print(raw_df)