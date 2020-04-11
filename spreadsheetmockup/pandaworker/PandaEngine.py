import pandas as pd
import numpy as np

import os
import re
from django.conf import settings
import django


class PandaEngine:
    def __init__(self):
        self.blankDF = pd.DataFrame.empty

    def loadColumns(self, file):
        self.filexrevolver(file)
        column_list = self.blankDF.columns.values
        column_string = str()
        for c in column_list:
            column_string += str(c) + ','

        self.blankDF = pd.DataFrame.empty
        return column_string

    def load_columns(self, file):
        self.filexrevolver(file)
        df_string = self.blankDF.to_string(index=False)
        df_list = list(df_string.split('\n'))
        pre_columns = df_list[0].strip()
        pre_columns_list = list(pre_columns.split())
        deliminator = ','
        self.blankDF = pd.DataFrame.empty
        return deliminator.join(pre_columns_list)


    def filexrevolver(self, locs):
        path, name = os.path.split(locs.name)
        head, tail = os.path.splitext(locs.name)
        if tail == '.csv':
            self.blankDF = pd.read_csv(locs)
        elif tail == '.xlsx':
            self.blankDF = pd.read_excel(locs)


if __name__ == "__main__":
    home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    media_dir = os.path.join(home_dir, 'media')
    print(os.path.join(home_dir, 'media'))
    onlyfiles = [f for f in os.listdir(media_dir) if os.path.isfile(os.path.join(media_dir, f))]
    print(onlyfiles[0])
    f = os.path.join(media_dir, onlyfiles[0])

    my_engine = PandaEngine()
    columns = my_engine.loadColumns(f)
    print(columns)

    formatted_columns = my_engine.load_columns(f)
    print(formatted_columns)

