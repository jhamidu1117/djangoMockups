from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from UPCendpoint.models import HandSet
import os
import re
import pandas as pd
from PIL import Image


class Command(BaseCommand):
    help = 'Displays current loads csv into database as Handset models'

    def handle(self, *args, **kwargs):
        home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        home_dir = os.path.dirname(home_dir)
        home_dir = os.path.dirname(home_dir)
        raw_data_file = os.path.join(home_dir, 'RawData', 'samupc.csv')
        image_dir = os.path.join(home_dir, 'RawData', 'img')
        data_df = pd.read_csv(raw_data_file, nrows=10)
        only_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
        for index, row in data_df.iterrows():
            upc = re.sub("'", "", row['UPC'])
            print(upc)
            for img in only_files:
                img_upc = re.sub('.jp*e*g', "", img)
                if upc == img_upc:
                    print(upc + "==" + img_upc)
                    # correct_img = Image.open(os.path.join(image_dir, img))
                    correct_img_path = os.path.join(image_dir, img)
                    # print(correct_img)
                    check_db = HandSet.objects.get(upc=row['UPC'])
                    # breakpoint()
                    if not check_db:
                        print(check_db, ' Dose not exist')
                        hand_set = HandSet(model_id=row['Model'], title=row['Title'],
                                           category=row['CategoryName'],
                                           upc=row['UPC'], img=correct_img_path)
                    else:
                        print(check_db, ' Upc Exists')
                        new_file = FileSystemStorage()
                        # correct_img.close()
                        with open(correct_img_path, 'rb', buffering=0) as f:
                            myfile = File(f)
                            filename = new_file.save('handsets/' + img_upc + '.jpg', myfile)
                        check_db.img = filename
                        hand_set = check_db
                        # breakpoint()
                    try:
                        hand_set.full_clean(exclude=None)
                        print(hand_set.model_id, hand_set.title, hand_set.category, hand_set.upc, hand_set.img)
                        hand_set.save()
                    except ValidationError as e:
                        print(e, 'will update model instead')

                        pass

