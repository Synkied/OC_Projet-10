#!/bin/bash

sudo /usr/bin/wget https://fr.openfoodfacts.org/data/fr.openfoodfacts.org.products.csv -O /media/pi/my_passport/nutellove_project/fr.openfoodfacts.org.products.csv && cd /media/pi/my_passport/nutellove_project && /home/pi/berryconda3/envs/nutellove/bin/python3 /media/pi/my_passport/nutellove_project/csv_cleaner.py && cd /media/pi/my_passport/nutellove_project && /home/pi/berryconda3/envs/nutellove/bin/python3 /media/pi/my_passport/nutellove_project/db_feeding.py
